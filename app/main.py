import streamlit as st
import plotly.graph_objects as go
import joblib
import numpy as np
import os

# ==============================================================================
# 1. APPLICATION ARCHITECTURE & CONFIGURATION
# ==============================================================================
# Initialize the Streamlit application context with specific viewport settings.
# Layout is set to 'wide' to optimize screen real estate for the dashboard view.
st.set_page_config(
    page_title="InsureAI | Predictive Analytics",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# 2. ARTIFACT DESERIALIZATION & RESOURCE MANAGEMENT
# ==============================================================================
@st.cache_resource
def load_artifacts():
    """
    Deserializes and loads machine learning artifacts (Model & Scaler) from the disk.
    Implements a Singleton pattern via Streamlit's resource caching decorator 
    to optimize memory allocation and prevent reload latency on interaction.
    
    Returns:
        dict: A dictionary containing the 'model' (RandomForest) and 'scaler' (StandardScaler).
    """
    artifacts = {}
    try:
        # Load the pre-trained Random Forest Regressor
        if os.path.exists('models/champion_random_forest.pkl'):
            artifacts['model'] = joblib.load('models/champion_random_forest.pkl')
        
        # Load the feature scaler for normalization consistency
        if os.path.exists('models/scaler.pkl'):
            artifacts['scaler'] = joblib.load('models/scaler.pkl')
    except Exception as e:
        # Error handling could be expanded for logging in production environments
        return None
    return artifacts

# Initialize system artifacts
assets = load_artifacts()
model = assets['model'] if assets else None
scaler = assets['scaler'] if assets else None

# ==============================================================================
# 3. FRONTEND CONTROLLER & UI ORCHESTRATION
# ==============================================================================
def main():
    """
    Main execution entry point. Renders the UI components and handles the 
    synchronous execution of the inference pipeline upon user trigger.
    """
    
    # Header & Meta Information
    st.title("InsureAI Estimate")
    st.markdown("### Enterprise-Grade Insurance Cost Estimation Engine")
    st.markdown("---")

    # Grid System Initialization: Establishing a 1:1 dual-column layout
    col_input, col_result = st.columns([1, 1], gap="large")

    # --------------------------------------------------------------------------
    # COLUMN 1: DATA INGESTION INTERFACE
    # --------------------------------------------------------------------------
    with col_input:
        st.subheader("User Profile Configuration")
        
        # Containerization: Encapsulating inputs in a native border container for visual separation
        with st.container(border=True):
            # Form Encapsulation: Batches input updates to prevent premature re-runs
            with st.form("prediction_form", border=False):
                
                # Feature: Age (Discrete Integer)
                st.write("**Age**")
                age = st.slider("Years", 18, 100, 35, label_visibility="collapsed")
                
                # Feature: BMI (Continuous Float)
                # Usage of Number Input allows for high-precision float entry required for BMI
                st.write("**BMI (Body Mass Index)**")
                bmi = st.number_input(
                    "BMI Value", 
                    min_value=10.0, 
                    max_value=60.0, 
                    value=30.0, 
                    step=0.1,
                    format="%.1f", # Precision enforcement
                    label_visibility="collapsed"
                )
                
                # Grid Nesting for compact layout of categorical features
                col_gen, col_child = st.columns(2)
                with col_gen:
                    st.write("**Biological Sex**")
                    sex = st.radio("Gender", ["Male", "Female"], label_visibility="collapsed", horizontal=True)
                with col_child:
                    st.write("**Dependents**")
                    children = st.number_input("Count", 0, 5, 0, label_visibility="collapsed")
                
                # Feature: Smoking Status (Binary)
                st.write("**Risk Factor: Smoking**")
                smoker = st.toggle("Active Smoker", value=False)
                
                # Feature: Region (Categorical)
                st.write("**Geographic Region**")
                region = st.selectbox("Select Region", ['Southeast', 'Northwest', 'Southwest', 'Northeast'], label_visibility="collapsed")
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                # Trigger Mechanism: Primary Action Button
                submitted = st.form_submit_button("Execute Prediction", type="primary", use_container_width=True)

    # --------------------------------------------------------------------------
    # COLUMN 2: VISUALIZATION & RESULT RENDERING
    # --------------------------------------------------------------------------
    with col_result:
        st.subheader("Analytical Report")
        
        with st.container(border=True):
            if submitted:
                # Initialize default prediction state
                prediction = 0.0
                
                # --- INFERENCE PIPELINE EXECUTION ---
                if model and scaler:
                    # 1. Feature Encoding (Categorical -> Numerical)
                    sex_val = 0 if sex == 'Male' else 1
                    smoker_val = 1 if smoker else 0
                    
                    # One-Hot Encoding for Region
                    r_nw = 1 if region == 'Northwest' else 0
                    r_se = 1 if region == 'Southeast' else 0
                    r_sw = 1 if region == 'Southwest' else 0
                    
                    # 2. Logic Layer: Dynamic Cluster Assignment
                    # Heuristic: Smokers assigned to High-Risk Cluster (2), others to Baseline (1)
                    cluster = 2 if smoker_val == 1 else 1
                    
                    # 3. Feature Normalization (Scaling)
                    # Note: Scaler expects raw vector shape: [Age, BMI, Children, Cluster]
                    input_raw = np.array([[age, bmi, children, cluster]])
                    input_scaled = scaler.transform(input_raw)[0]
                    
                    # 4. Vector Assembly (Dense Input Construction)
                    # Final Vector Shape: [Age(s), Sex, BMI(s), Child(s), Smoker, NW, SE, SW, Cluster(s)]
                    final_vec = np.array([[
                        input_scaled[0], sex_val, input_scaled[1], input_scaled[2],
                        smoker_val, r_nw, r_se, r_sw, input_scaled[3]
                    ]])
                    
                    # 5. Model Inference
                    prediction = model.predict(final_vec)[0]
                else:
                    # Fallback Logic for development/debugging contexts
                    prediction = 0.0
                
                # --- POST-PROCESSING & VISUALIZATION ---
                
                # 1. Logic-Based Alerts (Threshold Analysis)
                if prediction > 30000:
                    st.error("⚠️ High Risk Profile Detected: Premium exceeds standard thresholds.")
                elif prediction < 10000:
                    st.success("✅ Low Risk Profile: Optimal health markers identified.")
                else:
                    st.info("ℹ️ Standard Risk Profile: Aligns with market averages.")

                # 2. Key Performance Indicator (KPI) Display
                st.metric(label="ESTIMATED ANNUAL PREMIUM", value=f"$ {prediction:,.2f}")
                
                # 3. Data Visualization: Gauge Chart (Plotly)
                # Visualizes the prediction relative to min/max domain boundaries
                fig = go.Figure(go.Indicator(
                    mode = "gauge+number",
                    value = prediction,
                    number = {'prefix': "$ "},
                    gauge = {
                        'axis': {'range': [2000, 60000]}, # Domain boundaries
                        'bar': {'color': "rgba(0,0,0,0)"}, # Transparent needle background
                        'steps': [
                            {'range': [2000, 15000], 'color': "#00b894"},  # Safe Zone
                            {'range': [15000, 35000], 'color': "#fdcb6e"}, # Caution Zone
                            {'range': [35000, 60000], 'color': "#ff7675"}  # Danger Zone
                        ],
                        'threshold': {'line': {'color': "black", 'width': 4}, 'thickness': 0.75, 'value': prediction}
                    }
                ))
                fig.update_layout(height=250, margin=dict(l=20, r=20, t=20, b=20))
                st.plotly_chart(fig, use_container_width=True)

            else:
                # Idle State UI
                st.info("Awaiting Input: Adjust parameters and execute prediction to view results.")

if __name__ == '__main__':
    main()