# Linear Models in ML: Regression & Classification tasks for dairy farm

## Project Overview

A farmer from the dairy farm "Volny Lug" plans to expand his herd by purchasing new cows. To do so, he wants to predict:
1. Annual milk yield (kg/year) — regression task.
2. Probability that milk will be tasty — classification task.

The goal is to build machine learning models to help the farmer select cows based on two criteria:
- Milk yield ≥ 6000 kg/year.
- Milk must be tasty.

## Data Used

- `ferma_main.csv` — current herd characteristics.
- `ferma_dad.csv` — fathers of the cows.
- `cow_buy.csv` — cows available for purchase.

## Project Steps

1. Data loading and preprocessing (missing values, types, duplicates).
2. Exploratory Data Analysis (EDA, visualization, outliers, statistics).
3. Correlation analysis and multicollinearity check.
4. Regression modeling:
   - LinearRegression 1: baseline model.
   - LinearRegression 2: fix nonlinear relationships.
   - LinearRegression 3: add father name as a feature.
   - Evaluation using R², MSE, MAE, RMSE.
   - Predict milk yield for new cows.
5. Classification modeling:
   - LogisticRegression.
   - Metrics: Accuracy, Recall, Precision.
   - Tuning classification threshold.
   - Predict milk taste.
6. Final cow selection: yield ≥ 6000 kg and tasty milk.

## Result

The farmer received a ranked list of cows that meet his strict requirements. Risks were evaluated, and model-based recommendations were made. The best regression and classification models were selected and justified.
