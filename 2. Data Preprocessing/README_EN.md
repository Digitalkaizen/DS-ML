# Analysis of the Impact of Family Status and Number of Children on Loan Repayment

## Project Overview

The client is the credit department of a bank. The objective is to determine whether a client's family status and number of children influence the likelihood of repaying a loan on time. The findings will be used to improve the credit scoring model — a system that assesses a borrower's ability to repay a loan.

## Data Description

The dataset contains statistics on client creditworthiness. The table includes the following columns:

- `children` — number of children in the family
- `days_employed` — total work experience in days
- `dob_years` — age of the client in years
- `education` — education level of the client
- `education_id` — identifier of the education level
- `family_status` — marital status
- `family_status_id` — identifier of marital status
- `gender` — gender of the client
- `income_type` — type of employment
- `debt` — whether the client had a debt repayment issue
- `total_income` — monthly income
- `purpose` — purpose of the loan

## Project Stages

### 1. Data Overview

- Load the dataset
- Initial inspection of structure and data types
- Retrieve general information about the dataset

### 2. Data Preprocessing

- Handling missing values:
  - Impute `total_income` using the median per employment type
  - Convert negative values in `days_employed` to positive using `abs()`
  - Fill `days_employed` using median values per `income_type`
- Detecting and removing anomalies:
  - Remove rows with invalid values in `children`
- Type conversion:
  - Convert `total_income` to integer type
- Handling duplicates and inconsistent values:
  - Normalize values in `education` to lowercase
  - Remove full duplicate rows
- Creating new categorical features:
  - Income category (`total_income_category`)
  - Loan purpose category (`purpose_category`)

## Result

Clean and enriched data has been prepared for further analysis to assess the impact of family status and number of children on loan repayment. The study will help determine whether these factors are significant for the credit scoring model.
