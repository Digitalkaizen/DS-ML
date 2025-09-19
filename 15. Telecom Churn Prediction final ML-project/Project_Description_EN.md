# Project & Task Description (EN)

## Project: Predicting Customer Churn for Telecom Operator “TeleDom”

**Goal:** build a model that predicts if a subscriber will terminate the contract in advance, enabling timely retention actions (promo codes, special offers).  
**Context:** the company provides personal, contract, and service data. Contract information is current as of **2020‑02‑01**.

---

## Services Overview

Two core lines:
- **Telephony:** landline, **multiple lines** can be enabled.
- **Internet:** **DSL** (over phone line) and **Fiber optic** connections.

Additional services:
- **Security:** `DeviceProtection` (antivirus), `OnlineSecurity` (malicious site blocking);
- **TechSupport:** dedicated support line;
- **OnlineBackup:** cloud backups;
- **StreamingTV`** and **`StreamingMovies`: TV and movie catalog.

Payments: **month‑to‑month** or **1–2 year** contracts, multiple payment methods, electronic billing (`PaperlessBilling`).

---

## Data Description

Four tables to be joined by `customerID`:

### 1) `contract_new.csv` — contract
- `customerID` — subscriber ID
- `BeginDate` — contract start date
- `EndDate` — contract end date
- `Type` — contract type (Month‑to‑month / One year / Two year)
- `PaperlessBilling` — electronic billing (Yes/No)
- `PaymentMethod` — payment method
- `MonthlyCharges` — monthly charges
- `TotalCharges` — total charges to date

### 2) `personal_new.csv` — personal info
- `customerID`
- `gender`
- `SeniorCitizen` (0/1)
- `Partner` (Yes/No)
- `Dependents` (Yes/No)

### 3) `internet_new.csv` — internet services
- `customerID`
- `InternetService` (DSL/Fiber/No)
- `OnlineSecurity` (Yes/No/No internet service)
- `OnlineBackup` (Yes/No/No internet service)
- `DeviceProtection` (Yes/No/No internet service)
- `TechSupport` (Yes/No/No internet service)
- `StreamingTV` (Yes/No/No internet service)
- `StreamingMovies` (Yes/No/No internet service)

### 4) `phone_new.csv` — telephony
- `customerID`
- `MultipleLines` (Yes/No/No phone service)

> All tables are linked by `customerID`. Snapshot date is **2020‑02‑01**. Data are also available in cloud folder `/datasets/`.

---

## Work Plan

**Step 1 — Load data**  
Import files, initial inspection, check types and missing values.

**Step 2 — EDA & preprocessing (per table)**  
Explore distributions, handle business‑driven missing values (e.g., *No internet/No phone service* instead of `NaN`). Decide which features are useful for modeling.

**Step 3 — Join**  
Build a single dataset by `customerID` from selected features.

**Step 4 — EDA of the unified dataset**  
Visualize distributions, perform correlation analysis (including PHIK for categorical), engineer features (e.g., `contract_duration`, service aggregates), check multicollinearity.

**Step 5 — Data preparation**  
Train/test split. Preprocessing pipelines: categorical encoding (OHE/Ordinal/native CatBoost), numeric scaling where needed, robust imputation (`TotalCharges=0` if `tenure=0`, otherwise median).

**Step 6 — Model training**  
Train at least two models (e.g., Logistic Regression, RandomForest, CatBoost). Tune ≥2 hyperparameters for at least one model (RandomizedSearchCV/GridSearchCV).

**Step 7 — Model selection**  
Cross‑validated **AUC‑ROC** (target metric), **threshold tuning** on out‑of‑fold predictions, then a single final evaluation on **test** only.

**Step 8 — Summary & business recommendations**  
Report quality of the best model, interpret drivers (Permutation Importance/SHAP), provide actionable guidance for retention (operating threshold, campaign strategy, error‑cost trade‑offs).

---

## Expected Outcome

- Reproducible repo with code and report;
- A model achieving **AUC‑ROC ≥ 0.85** on the test set;
- Practical, business‑ready recommendations (threshold policy, prioritized customer segments).
