# Project: Taxi Order Prediction

## Project Description

Taxi company has collected historical data on taxi orders at airports. To attract more drivers during peak hours, it is necessary to forecast the number of taxi orders for the next hour. The goal of this project is to build a machine learning model for such a prediction.

**Success criterion:** the RMSE metric on the test set should be **no more than 48**.

---

## Project Steps

1. Load and preprocess data:
   - Resample the data to hourly intervals;
   - Analyze the time series.

2. Train models:
   - Train multiple models with different hyperparameters;
   - Split the dataset: 10% — test set.

3. Evaluate performance:
   - Test the model on the test set;
   - Draw conclusions and interpret the results.

---

## Data Description

The dataset is located in the file: `/datasets/taxi.csv`.

- **num_orders** — number of orders (target feature);
- Timestamp (datetime index) is used as the index.

---

## Technologies Used

- Pandas
- Scikit-learn
- Matplotlib / Seaborn
- Time Series Analysis
- Machine Learning Models: Linear Regression, Random Forest, Gradient Boosting, etc.