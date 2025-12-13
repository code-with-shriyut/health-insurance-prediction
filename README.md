# health-insurance-prediction
"Machine Learning project to predict insurance costs using various models."
# 🏥 Insurance Premium Prediction Project

### 🚀 Project Status: Phase 1 Completed (Champion Model Selected)

This project applies Machine Learning techniques to predict health insurance premiums based on personal attributes such as age, BMI, smoking habits, and region. The goal was to build a highly accurate regression model to assist in automated premium estimation.

---

## 🏆 Champion Model: Random Forest Regressor

After rigorous testing and comparison of multiple algorithms (Linear Regression, Lasso, Decision Tree, KNN, and Random Forest), we have selected the **Random Forest Regressor** as our production-grade model.

### 📊 Performance Metrics (Verified)
| Metric | Score | Status |
| :--- | :--- | :--- |
| **R² Score (Accuracy)** | **97.89%** | ✅ Excellent |
| **MAE (Avg Error)** | **847.67** | ✅ Acceptable |
| **Model Artifact** | `models/champion_random_forest.pkl` | 💾 Saved |

> **Architect's Note:** The model was optimized using `max_depth=7` and feature engineering (K-Means Clustering) to achieve this high accuracy, significantly outperforming the baseline linear models.

---

## 🥇 Model Leaderboard (Comparison)

Below is the final evaluation of all models developed by the team.

| Rank | Model Name | R² Score | MAE | Developer |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **Random Forest** | **97.89%** | **847.67** | **Pritilata** |
| 2 | Decision Tree | 96.10%* | 1250.50* | Dhrubajit |
| 3 | Lasso Regression | 81.75%* | 3500.70* | Shriyut |
| 4 | Linear Regression | 81.76%* | 3480.10* | Shriyut |
| 5 | KNN Regressor | 78.90%* | 4200.00* | Subhadip |

*(Note: Competitor scores are approximate based on development phase results)*

---

## 📂 Project Structure
├── data/ │ ├── processed/ # Cleaned data and Final Comparison CSV │ ├── raw/ # Original dataset │ ├── X_train.csv, y_train.csv... # Split datasets ├── models/ │ ├── champion_random_forest.pkl # The Final Deployment Ready Model ├── notebooks/ │ ├── model_RF_pritilata.ipynb # Champion Model Training │ ├── model_Verification_FINAL.ipynb # Final Quality Check Code │ ├── model_Comparison_FINAL.ipynb # Benchmarking Code ├── README.md # Project Documentation ├── requirements.txt # Project Dependencies
## 🛠️ How to Run the Project

1. **Clone the Repository**
   ```bash
   git clone <your-repo-link>

2. Install Dependencies

Bash

pip install -r requirements.txt

3. Verify the Champion Model Run the verification script to confirm the 97.89% accuracy:

Bash

jupyter notebook notebooks/model_Verification_FINAL.ipynb

# 👥 Contributors & Roles

Shriyut: Project Orchestration, Data Preprocessing, Pipeline Design, Linear/Lasso Models, Final Review.

Pritilata: Random Forest Model Development (Champion Model).

Dhrubajit: Decision Tree Implementation.

Subhadip: KNN Regressor Model.
