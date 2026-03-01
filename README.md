# NYC Food-Only Restaurant Data Pipeline Project

## Project Overview
This project demonstrates a structured data engineering pipeline that processes restaurant inspection data and filters businesses that sell food only (no alcohol or grocery sales).

The goal is to simulate a real-world medallion architecture using Bronze, Silver, and Gold layers.

---

## Architecture

data/
│
├── raw/        → Original dataset (Bronze Layer)
├── curated/    → Cleaned & transformed data (Silver Layer)
└── gold/       → Aggregated & business-ready data (Gold Layer)

---

## Technologies Used

- Python
- Pandas
- Git
- GitHub
- VS Code
- Medallion Architecture Design

---

## Business Use Case

Identify restaurants that:
- Sell only food
- Exclude alcohol-serving establishments
- Exclude grocery stores
- Provide clean datasets for analytics

---

## Pipeline Steps

1. Ingest raw CSV data
2. Clean and filter unwanted categories
3. Remove duplicates
4. Apply business rules
5. Aggregate results for reporting
6. Store final dataset in Gold layer

---

## Author

Mamatha  
Data Engineer | Data Pipeline & Analytics Enthusiast
