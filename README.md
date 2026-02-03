# 🏥 Health Insurance Premium Prediction

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://health-insurance-prediction-6txznqt3mghqyanykyrmdv.streamlit.app/)

Built a regression-based machine learning model to predict health insurance premiums using demographic and lifestyle attributes such as age, BMI, smoking status, and region. The project focuses on model comparison, performance evaluation, and explainability to support automated pricing and risk assessment decisions.

---
## 📌 Business Problem

Insurance providers need accurate premium estimation to balance customer affordability with financial risk. This project predicts expected insurance charges based on individual risk profiles to support data-driven pricing and underwriting decisions.

### 🧠 Approach

- Performed data preprocessing and feature engineering on structured insurance data

- Trained and compared multiple regression models to benchmark performance

- Selected a champion model based on predictive accuracy and error metrics

- Packaged the final model for interactive use through a Streamlit dashboard

---
## 🤖 Models Evaluated

- Linear Regression

- Lasso Regression

- K-Nearest Neighbors (KNN)

- Decision Tree Regressor

- Random Forest Regressor (Champion Model)

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

*Key Insight: Smoking status, BMI, and age were the strongest predictors influencing insurance premium values.*

---

## 🛠️ Tech Stack

- Python

- Pandas, NumPy

- Scikit-learn

- Matplotlib / Seaborn

- Streamlit

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
