# House Price Prediction

A machine learning project built with Python to predict house prices using property features such as area, bedrooms, bathrooms, parking, furnishing status, and location. The project compares Linear Regression and Gradient Boosting models to estimate prices accurately.

# Requirements

  Python
  pandas
  numpy
  matplotlib
  seaborn
  scikit-learn

# Installation

1. Clone or download the project files.

2. Install the required libraries in your terminal:

pip install pandas numpy matplotlib seaborn scikit-learn

3. Place the dataset file `Housing.csv` inside the project folder.

# Usage

Navigate to the project folder and run:

cd House_Price_Prediction
python house_price_prediction.py

The program will train models, evaluate performance, and display graphs.

# Dataset Features

  price (target)
  area
  bedrooms
  bathrooms
  stories
  mainroad
  guestroom
  basement
  hotwaterheating
  airconditioning
  parking
  prefarea
  furnishingstatus

# Features

# Data Preprocessing

  Handles categorical columns using one-hot encoding.
  Splits dataset into training and testing sets.
  Applies feature scaling using StandardScaler.

# Models Used

  Linear Regression
  Gradient Boosting Regressor

# Evaluation Metrics

  Mean Absolute Error (MAE)
  Root Mean Squared Error (RMSE)
  R² Score

# Results

  Linear Regression gives baseline predictions.
  Gradient Boosting performs better by capturing complex feature relationships.

# Visualizations

  Actual vs Predicted House Prices
  Prediction Error Distribution

# Project Structure

  House_Price_Prediction/
  house_price_prediction.py
  Housing.csv
  README.md

# Final Insights

  Important factors affecting price include area, bathrooms, location, and furnishing status.
  Lower MAE/RMSE and higher R² indicate better model performance.
  Gradient Boosting is the stronger model for accurate house price prediction.

# Notes

  Ensure `Housing.csv` is in the correct folder path.
  If graphs do not appear, run the script in Jupyter Notebook or VS Code.
  You can replace the dataset with another housing dataset by updating the target column name.
