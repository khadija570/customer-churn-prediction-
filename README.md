# Customer Churn Prediction

## Overview
Customer churn prediction is an important problem for many companies, especially in the telecommunications sector. The goal of this project is to use machine learning techniques to predict whether a customer is likely to leave a service provider.

By identifying customers at risk of churn, companies can take proactive actions to improve customer retention and reduce revenue loss.

This project uses the **Telco Customer Churn dataset** and applies several machine learning models to analyze and predict churn behavior.

---

## Dataset
The dataset used in this project is the **Telco Customer Churn Dataset** from Kaggle.

It contains information about telecom customers including:

- Customer demographics
- Services subscribed
- Account information
- Monthly charges
- Contract type
- Churn status (target variable)

Target variable:

- **Churn**
  - 0 → Customer stays
  - 1 → Customer leaves

Total number of samples: **7043 customers**

---

## Machine Learning Pipeline

The project follows a standard machine learning workflow:

### 1. Data Loading
The dataset is loaded using **Pandas**.

### 2. Data Cleaning
- Removal of the `customerID` column
- Conversion of `TotalCharges` to numeric
- Handling missing values

### 3. Data Preprocessing
- Encoding categorical variables using **LabelEncoder**
- Feature scaling using **StandardScaler**

### 4. Train-Test Split
The dataset is split into:

- **80% training data**
- **20% testing data**

using stratified sampling.

### 5. Model Training
Three machine learning models are trained:

- Logistic Regression
- Random Forest
- XGBoost

### 6. Model Evaluation
Models are evaluated using several performance metrics:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

---

## Results

The models are compared using multiple evaluation metrics and visualizations.

The script automatically generates the following figures:

- Confusion matrices
- ROC curves
- Model performance comparison

Generated files:

```
confusion_matrices.png
roc_curves.png
metric_comparison.png
```

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- XGBoost
- Matplotlib

---

## Project Structure

```
customer-churn-prediction
│
├── customer_churn_prediction.py
├── WA_Fn-UseC_-Telco-Customer-Churn.csv
├── confusion_matrices.png
├── roc_curves.png
├── metric_comparison.png
├── README.md
└── LICENSE
```

---

## How to Run the Project

### Clone the repository

```bash
git clone https://github.com/khadija570/customer-churn-prediction-.git
cd customer-churn-prediction-
```

### Install dependencies

```bash
pip install pandas scikit-learn matplotlib xgboost
```

### Run the script

```bash
python customer_churn_prediction.py
```

The script will train the models and generate the evaluation plots.

---

