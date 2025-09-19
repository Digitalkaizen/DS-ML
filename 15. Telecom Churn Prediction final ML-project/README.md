# ChurnGuard: Telco Customer Churn Prediction

A production-style ML project to predict customer churn for a telecom company using **CatBoost** as the final model. The notebook contains a complete, reproducible pipeline: data validation, feature engineering, robust categorical correlation analysis (PHIK), model selection (LR / RF / CatBoost), hyperparameter tuning, **cross-validated thresholding**, test-only final evaluation, and permutation-based interpretation.

---

## Key Highlights
- **Target metric:** ROC-AUC (insensitive to class imbalance).
- **Final model:** Tuned CatBoost with cross-validated threshold.
- **Test ROC-AUC:** ~0.92 (within the required 0.85–0.95 band).
- **Business-ready:** Clear threshold policy & action playbook for retention.

---

## Dataset (Telco-style)
- Entities: ~7k customers with contract/billing/service info
- Target: `churn` (1 if the contract ended by snapshot date, else 0)
- Snapshot date: `2020‑02‑01`

### Data validation & target definition
- `churn = 1` if `EndDate` is **not null** (including when `EndDate == snapshot`), else `0`.
- Tenure / contract duration in days and months is computed using **effective end date**: `EndDate` for churned clients; snapshot date for active clients.

### Missing values policy
- **Business-missing ≠ data-missing.**
- Internet/phone add-ons: missing → explicit category (“No internet service”, “No phone service”).
- `total_charges`: `0` **only for new clients** (`tenure = 0`); **median** otherwise.
- All encoding via **learned transformers** (no manual mapping).

---

## Final Feature Set (14)
```
payment_group, monthly_charges, total_charges, partner, contract_duration,
multiple_lines, online_backup, device_protection, streaming_movies,
senior_citizen, dependents, type, internet_service, paperless_billing_yes
```
Rationale: covers **payment behavior**, **price/tenure**, **service bundle**, **contract type**, and **basic demographics** while avoiding leakage and heavy multicollinearity.

---

## Modeling
- **Pipelines**
  - LogisticRegression: `OHE(drop='first')` + `StandardScaler` for numeric.
  - RandomForest: `OrdinalEncoder` for categorical.
  - CatBoost: native categorical handling via `cat_features`.
- **Model selection** via 5-fold CV (ROC-AUC).
- **Tuning**: randomized search (fast) for CatBoost on 3-fold → validated on 5-fold.
- **Thresholding**: **cross_val_predict** (OOF) + Youden’s J to choose the operating point.
- **Test evaluation**: **only the best model** (CatBoost).

### Results (typical run)
- CV ROC-AUC (CatBoost tuned): ~0.90
- **TEST ROC-AUC:** ~0.92; **Accuracy:** ~0.86; **F1:** ~0.66 @ threshold ≈ 0.18
- Confusion matrix example (TEST): `TN=1292, FP=194, FN=46, TP=229`

### Interpretation (Permutation Importance on TEST)
Top drivers (ΔAUC):
1) `device_protection` (~0.29–0.31) — strongest signal among add-ons  
2) `multiple_lines` (~0.08–0.13) — telephony availability  
3) `total_charges` (~0.05–0.06) — cumulative payments / lifecycle  
Next: `partner`, `online_backup`, `streaming_movies`

---

## Reproducibility
1. Create environment (Python ≥ 3.9).
2. Install deps:
   ```bash
   pip install -r requirements.txt
   # phik, catboost, scikit-learn, pandas, numpy, matplotlib, seaborn
   ```
3. Run the notebook end-to-end (cells are ordered to avoid leakage and duplication).
4. Results are deterministic with `random_state=80925` where applicable.


## Business Usage
- Use the model’s probability to segment customers by churn risk.
- Current operating point favors **recall** (catch more churners). If budget-limited, raise the threshold to increase precision.
- Prioritize outreach to profiles lacking `device_protection` and telephony (`multiple_lines`), and with low `total_charges`.

---

## License
MIT (unless your org requires a different license).
