# NYC Food-Only Restaurant Data Pipeline (Palantir Foundry Project)

## Project Overview

This project was developed using Palantir Foundry to simulate a real-world enterprise data engineering workflow.

The objective was to build a structured data pipeline that filters and processes restaurant inspection data to identify businesses that sell food only (excluding alcohol-serving establishments and grocery stores).

The project demonstrates medallion architecture (Bronze, Silver, Gold layers) using Foundry’s Pipeline Builder and Ontology.

---

## Architecture (Medallion Design)

Bronze Layer (Raw)
- Ingested raw CSV dataset into Foundry
- Automatically generated schema

Silver Layer (Curated)
- Applied data cleaning
- Removed duplicates
- Filtered unwanted categories (alcohol, grocery, etc.)
- Applied business transformation logic

Gold Layer (Business Ready)
- Aggregated results
- Prepared reporting dataset
- Structured final analytics table

---

## Tools & Technologies

- Palantir Foundry
- Pipeline Builder
- Ontology Workshop
- Python (Transform API)
- Git & GitHub
- VS Code

---

## Business Use Case

Designed for stakeholders who want to:

- Identify food-only restaurants
- Exclude alcohol-serving establishments
- Exclude grocery stores
- Enable analytics and reporting on clean restaurant data

---

## Key Skills Demonstrated

- Data pipeline design
- Medallion architecture implementation
- Enterprise data modeling
- Business rule transformation
- Data governance concepts
- Version control with Git

---

## Author

Mamatha  
Data Engineer | Data Platforms & Analytics Enthusiast
