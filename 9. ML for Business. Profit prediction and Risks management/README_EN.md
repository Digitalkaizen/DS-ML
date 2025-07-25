# Project: Selecting a Region for a New Oil Well

## Project Overview

An oil extraction company needs to decide where to drill a new well. The goal of the project is to build a model to determine which of the three provided regions will bring the highest profit. Using historical data, we will analyze features, train a linear regression model, and assess expected profit and risks using bootstrap.

## Project Steps

### 1. Data Loading and Preparation
- Import data from three regions.
- Check for missing values and duplicates.
- Split into features and target variable.

### 2. Model Training
- Split data into training and validation sets (75:25).
- Train linear regression model.
- Make predictions and evaluate metrics (RMSE, mean reserves).

### 3. Profit Preparation
- Calculate the break-even reserve volume.
- Compare with average reserves in each region.

### 4. Profit Calculation
- Select top 200 wells based on model predictions.
- Calculate profit from the selected wells.

### 5. Bootstrap Analysis
- Perform 1000 bootstrap iterations.
- Calculate confidence interval and average profit.
- Assess loss risk.

## Business Constraints

- Only linear regression is allowed.
- 200 out of 500 wells are selected for development.
- Budget: 10 billion rubles.
- Profit per 1,000 barrels: 450,000 rubles.
- Maximum acceptable loss risk: 2.5%.

## Conclusion

Bootstrap analysis results allow identifying the region with the highest expected profit and acceptable risk level. This region is recommended for development.