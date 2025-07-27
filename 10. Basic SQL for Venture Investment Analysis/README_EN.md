
# Project: Venture Investment Analysis

## Project Description

This project investigates a database containing information about venture capital funds and investments in startups. The database is based on the "Startup Investments" dataset from Kaggle.

## Project Goal

To analyze the venture investment market: identify funding sources, highlight successful companies and funds, and explore relationships between players in the investment process.

## Database Structure

The database contains the following tables:

- `acquisition`: company acquisition deals
- `company`: startup information
- `education`: employee education data
- `fund`: venture capital funds
- `funding_round`: investment rounds
- `investment`: fund investments in startups
- `people`: startup employees

## Key Fields

For example, the `company` table includes:
- `id` — unique company identifier
- `name` — company name
- `status` — company status (operating, acquired, closed, ipo)
- `founded_at`, `closed_at` — foundation and closure dates
- `funding_total` — total amount of raised funding

## Tools Used

- PostgreSQL
- Python (pandas, SQLAlchemy, matplotlib/seaborn)
- Jupyter Notebook

## Tasks

- Build ER-diagram
- Explore database structure
- SQL queries to analyze investments, rounds, company status, and fund activity
- Visualizations and conclusions

## Author

Project completed as part of a Data Analytics course.
