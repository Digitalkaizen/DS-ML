# Project: Car Market Price Prediction

## Project Description

Client is a used car sales service developing a web application that allows users to estimate the market value of their car.

You are provided with historical data including vehicle specifications, configuration, and prices. The goal is to build a model that accurately predicts car prices.

## Goals and Business Requirements

Key client priorities:
- Prediction quality
- Training time
- Prediction time

## Workflow

1. Load and inspect the dataset (`/datasets/autos.csv`);
2. Handle missing values and anomalies; remove non-informative features;
3. Prepare training and test datasets;
4. Train multiple models:
    - at least one must be a gradient boosting model (LightGBM);
    - at least one must be a non-boosting model;
5. Tune hyperparameters;
6. Analyze training time, prediction time, and model quality (RMSE);
7. Select the best model based on client criteria;
8. Final evaluation on the test set.

## Requirements

- Metric: RMSE ≤ 2500;
- Use LightGBM;
- Compare models by training/prediction time and quality.

## Dataset Description

**Target Feature:**
- `Price` — car price (in euros)

**Features:**
- `DateCrawled` — date when listing was scraped
- `VehicleType` — vehicle body type
- `RegistrationYear` — year of registration
- `Gearbox` — transmission type
- `Power` — horsepower
- `Model` — model name
- `Kilometer` — mileage (km)
- `RegistrationMonth` — registration month
- `FuelType` — fuel type
- `Brand` — car brand
- `Repaired` — whether the car was repaired
- `DateCreated` — ad creation date
- `NumberOfPictures` — number of pictures
- `PostalCode` — seller's postal code
- `LastSeen` — date of last user activity

## Notes

- Use Jupyter Notebook cell timing commands to measure performance;
- If needed, free up memory using `del`.