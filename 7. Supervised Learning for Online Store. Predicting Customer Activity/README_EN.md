# Supervised Learning: Predicting Customer Activity Drop

## Project Overview

The online store "One Click" noticed a decline in recurring customer activity.  
The goal is to build a machine learning model that predicts whether a customer's activity will drop in the next 3 months.  
Using model predictions and profitability data, we segment customers and propose personalized retention strategies.

## Data Sources

- `market_file.csv` — customer communications, on-site behavior, and product interactions.
- `market_money.csv` — customer revenue data across periods.
- `market_time.csv` — time spent on the site by period.
- `money.csv` — customer profitability over the past 3 months.

## Project Steps

1. **Data loading and structure validation**.
2. **Preprocessing** — handling missing values, data types, filtering active users.
3. **EDA** — exploratory analysis of all features and tables.
4. **Merging datasets** — transforming period columns into features and creating a unified dataset.
5. **Correlation analysis** — check for multicollinearity and remove redundant features.
6. **Model training**:
   - Models: KNN, DecisionTree, LogisticRegression, SVC
   - Use pipelines with multiple encoders and scalers
   - Hyperparameter tuning and selection via ROC-AUC
7. **Feature importance**:
   - SHAP interpretation
   - Identify impactful and negligible features
8. **Customer segmentation**:
   - Focus on high-risk, high-profit segment
   - Graphical and statistical profiling
   - Tailored retention strategies

## Result

- Built a robust classifier (ROC-AUC based).
- Identified key features affecting customer retention.
- Proposed actionable strategies to target at-risk customers with high profitability.
