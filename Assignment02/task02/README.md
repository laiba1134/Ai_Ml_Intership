## Objective

Build a reusable and production-ready machine learning pipeline for predicting customer churn using the Scikit-learn Pipeline API.

# Project Overview

This project implements a complete machine learning workflow for customer churn prediction using the IBM Telco Customer Churn dataset.

The project includes:

* Data preprocessing
* Feature scaling
* Categorical encoding
* Machine learning model training
* Hyperparameter tuning
* Model evaluation
* Exporting the trained pipeline using Joblib

The pipeline is designed to automate preprocessing and prediction steps in a reusable and production-ready format.


# Dataset

Dataset Used:
IBM Telco Customer Churn Dataset

The dataset contains customer information such as:

* Demographics
* Internet services
* Account information
* Billing details
* Customer churn status

Target Variable:

* `Churn`

---

# Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Google Colab

---

# Machine Learning Models

The following models were trained and evaluated:

1. Logistic Regression
2. Random Forest Classifier

---

# Pipeline Components

The Scikit-learn Pipeline API was used to automate preprocessing and model training.

## Numerical Preprocessing

* Missing value imputation
* Standard scaling

## Categorical Preprocessing

* Missing value imputation
* One-hot encoding

## Hyperparameter Tuning

* GridSearchCV

---

# Project Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Feature Preprocessing
   ↓
Pipeline Creation
   ↓
Model Training
   ↓
Hyperparameter Tuning
   ↓
Evaluation
   ↓
Export Trained Pipeline
```

---

# Files Included

```text
task02/
│
├── churn_pipeline_v2.ipynb
├── churn_pipeline.pkl
├── README.md
└── telco.csv
```

---

# How to Run

## Install Required Libraries

```bash
pip install pandas numpy scikit-learn joblib
```

## Run Notebook

Open the notebook in Google Colab or Jupyter Notebook and execute all cells.

---

# Exported Model

The trained machine learning pipeline is saved as:

```text
churn_pipeline.pkl
```

This file contains:

* Preprocessing pipeline
* Feature transformations
* Trained model
* Tuned parameters

The model can be loaded directly for prediction without repeating preprocessing steps.

---

# Model Loading Example

```python
import joblib

model = joblib.load("churn_pipeline.pkl")
```

---

# Learning Outcomes

Through this project, the following concepts were learned:

* Scikit-learn Pipeline API
* Data preprocessing automation
* Feature engineering
* Machine learning workflows
* Hyperparameter tuning
* Production-ready ML pipelines
* Model serialization using Joblib

---

# Conclusion

This project successfully demonstrates an end-to-end machine learning pipeline for customer churn prediction using Scikit-learn. The implementation follows a modular and reusable approach suitable for real-world ML deployment workflows.
