# 🏥 Insurance Premium Prediction Project

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://health-insurance-prediction-6txznqt3mghqyanykyrmdv.streamlit.app/)

> **🚀 Project Status:** Phase 1 Completed (Champion Model Selected)

This project applies Machine Learning techniques to predict health insurance premiums based on personal attributes such as age, BMI, smoking habits, and region. The goal was to build a highly accurate regression model to assist in automated premium estimation.

---

## 🏆 Champion Model: Random Forest Regressor

After rigorous testing and comparison of multiple algorithms (Linear Regression, Lasso, Decision Tree, KNN, and Random Forest), we have selected the **Random Forest Regressor** as our production-grade model.

### 📊 Performance Metrics (Verified)

| Metric | Score | Status |
| :--- | :--- | :--- |
| **R² Score (Accuracy)** | **97.89%** | ✅ Excellent |
| **MAE (Avg Error)** | 847.67 | ✅ Acceptable |
| **Model Artifact** | `models/champion_random_forest.pkl` | 💾 Saved |

> **Architect's Note:** The model was optimized using `max_depth=7` and feature engineering (K-Means Clustering) to achieve this high accuracy, significantly outperforming the baseline linear models.

---

## 🥇 Model Leaderboard (Comparison)

Below is the final evaluation of all models developed by the team.

| Rank | Model Name | R² Score | MAE | Developer |
| :---: | :--- | :--- | :--- | :--- |
| 🥇 | **Random Forest** | **97.89%** | **847.67** | **Pritilata** |
| 🥈 | KNN Regressor | 97.24% | 1083.87 | Subhadip |
| 🥉 | Decision Tree | 96.10% | 1250.50 | Dhrubajit |
| 4 | Lasso Regression | 81.75% | 3500.70 | Shriyut |
| 5 | Linear Regression | 81.76% | 3480.10 | Shriyut |

*(Note: Competitor scores are approximate based on development phase results)*

---

## 📂 Project Structure

```bash
health-insurance-prediction/
├── app/
│   └── main.py                  # Streamlit Dashboard App
├── data/
│   ├── processed/               # Cleaned data and Final Comparison CSV
│   └── raw/                     # Original dataset
├── models/
│   ├── champion_random_forest.pkl # The Final Deployment Ready Model
│   └── scaler.pkl               # Feature Scaler
├── notebooks/
│   ├── model_RF_pritilata.ipynb # Champion Model Training
│   ├── model_Verification_FINAL.ipynb # Final Quality Check Code
│   └── model_Comparison_FINAL.ipynb # Benchmarking Code
├── README.md                    # Project Documentation
└── requirements.txt             # Project Dependencies

```

---

## 🛠️ How to Run the Project

### 1. Clone the Repository

```bash
git clone <your-repo-link>
cd health-insurance-prediction

```

### 2. Install Dependencies

```bash
pip install -r requirements.txt

```

### 3. Verify the Champion Model

Run the verification script to confirm the 97.89% accuracy:

```bash
jupyter notebook notebooks/model_Verification_FINAL.ipynb

```

### 4. Run the Dashboard App (New)

To launch the interactive web interface:

```bash
streamlit run app/main.py

```

---

## 👥 Contributors & Roles

| Contributor | Roles & Responsibilities |
| --- | --- |
| **Shriyut(Team Lead)** | Project Orchestration, Data Preprocessing, Pipeline Design, Linear/Lasso Models, UI Developement & Final Review. |
| **Pritilata** | Random Forest Model Development (Champion Model) & **UI Development**. |
| **Dhrubajit** | Decision Tree Implementation. |
| **Subhadip** | KNN Regressor Model. |

```

```
