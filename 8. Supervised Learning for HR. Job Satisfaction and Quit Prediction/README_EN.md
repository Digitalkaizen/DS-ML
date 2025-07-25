
# Project: Supervised Learning — Job Satisfaction and Attrition Prediction

## Description

The company "Careful Work" provides HR data. The goal is to build machine learning models to:

1. Predict employee job satisfaction level (from 0 to 1).
2. Predict employee attrition (`quit`: 1 — left, 0 — stayed).

## Data

### Task 1: Job Satisfaction Prediction

**Target:** `job_satisfaction_rate`  
**Features:**
- `id`
- `dept`
- `level`
- `workload`
- `employment_years`
- `last_year_promo`
- `last_year_violations`
- `supervisor_evaluation`
- `salary`

### Task 2: Attrition Prediction

**Target:** `quit`  
**Features:** same as Task 1 (+ predicted `job_satisfaction_rate`)

## Stages

### Step 1. Data Loading
From files:
- `train_job_satisfaction_rate.csv`, `train_quit.csv`
- `test_features.csv`
- `test_target_job_satisfaction_rate.csv`, `test_target_quit.csv`

### Step 2. Preprocessing
- Handle missing values
- Type conversion
- Imputation in pipeline

### Step 3. EDA
- Feature distributions
- Relationship analysis
- Portrait of an employee likely to leave

### Step 4. Feature Engineering
- Use model from Task 1 to create `job_satisfaction_rate_pred`

### Step 5. Feature Preparation
- ColumnTransformer + pipeline
- Ordinal and OneHot encoding

### Step 6. Modeling

#### Task 1:
- Ridge, DecisionTree, LightGBM
- Metric: SMAPE (≤ 15%)

#### Task 2:
- Logistic Regression, Random Forest, LightGBM
- Metric: ROC-AUC (≥ 0.91)

## Conclusions

- Built job satisfaction prediction model with SMAPE ≤ 15%
- Best attrition model achieved ROC-AUC ≥ 0.91
- Recommendations provided to reduce churn
