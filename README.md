# 📊 Telco Customer Churn Prediction (Industrial ML Path)

## 📌 Project Overview
This project delivers an end-to-end industrial machine learning pipeline to predict customer attrition. By transitioning from a simple baseline to an optimized, balanced model, we provide a robust tool for business decision-making.

## 📁 Project Structure (Modular Architecture)
To meet industrial standards, the project is organized into specialized modules:
- `data/`: Raw and processed datasets.
- `notebooks/`: 
  - `EDA.ipynb`: Exploratory Data Analysis & Visualizations.
  - `experiments.ipynb`: The main modular pipeline execution.
- `models/`: Serialized artifacts (`final_churn_model.pkl`).
- `results/charts/`: Exported evaluation plots (ROC, Confusion Matrix, SHAP).
- `src/`: Core logic:
  - `preprocessing/`: Data cleaning and transformation scripts.
  - `models/`: Evaluation and metric calculation logic.
  - `utils/`: Helper functions for model serialization.
- `Dockerfile`: Containerization setup for platform-independent execution (Bonus).



## 🛠 Preprocessing & Model Improvement
- **Data Cleaning:** Handled missing `TotalCharges` via median imputation and dropped `customerID`.
- **Feature Engineering:** Implemented **One-Hot Encoding** for categorical variables and **StandardScaler** for numerical stability.
- **Handling Imbalance:** Applied **SMOTE** (Synthetic Minority Over-sampling Technique) to balance the target class, significantly improving the **F1-Score** for churners.
- **Optimization:** Utilized **GridSearchCV** for hyperparameter tuning of the final XGBoost model.

## 🤖 Models & Scientific Evaluation
We performed a comprehensive comparison of classical algorithms:
1. **Logistic Regression** (Baseline).
2. **SVM & KNN**.
3. **Random Forest**.
4. **XGBoost** (Final Model).

### Final Performance:
- **ROC-AUC:** 0.84 (High class-separation stability).
- **F1-Score:** ~0.61 (Balanced for both precision and recall).
- **Explainability (SHAP):** Identified **Tenure** and **Contract Type** as the primary drivers of churn.



## 🚀 How to Run

### 1. Local Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Run the pipeline
jupyter notebook notebooks/experiments.ipynb

# Build the container
docker build -t churn-pred .

# Run the container
docker run churn-pred