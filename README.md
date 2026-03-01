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


over all process
# NYC Food-Only Restaurant ETL Pipeline (Palantir Foundry Project)

## 📌 Project Overview

This project demonstrates an end-to-end data engineering workflow built in Palantir Foundry using:

- Pipeline Builder
- Medallion Architecture (Raw → Silver → Gold)
- Data Filtering Logic (Food-only restaurants)
- Ontology Workshop Modeling
- Object Relationships & Preview
- Git Version Control

---

## 🏗 Pipeline Architecture

<p align="center">
  <img src="docs/screenshots/pipeline_builder_raw_silver_gold_overview.png" width="900"/>
</p>

This pipeline follows Medallion Architecture principles:
- Raw layer ingestion
- Silver layer cleaning & filtering
- Gold layer aggregation

---

## 🧹 Silver Layer – Food Only Filtering

<p align="center">
  <img src="docs/screenshots/pipeline_silver_nyc_food_only_filter.png" width="900"/>
</p>

Business rule implemented:
- Exclude alcohol-focused establishments
- Retain only food-serving restaurants

---

## 📊 Gold Layer Aggregation

<p align="center">
  <img src="docs/screenshots/pipeline_silver_food_only_filter_v2.png" width="900"/>
</p>

Aggregations include:
- Restaurant counts by borough
- Cleaned analytical dataset

---

## 🧠 Ontology Modeling

<p align="center">
  <img src="docs/screenshots/restaurants_ontology_model.png" width="900"/>
</p>

Modeled entities:
- Restaurant
- Borough
- Relationships between them

---

## 🏛 Borough Object Model

<p align="center">
  <img src="docs/screenshots/boroughRestaurant_ontology_model.png" width="900"/>
</p>

---

## 🔎 Object Preview & Validation

<p align="center">
  <img src="docs/screenshots/preview_object_borough_ontology.png" width="900"/>
</p>

---

## 🛠 Tech Stack

- Palantir Foundry
- Pipeline Builder
- Ontology Workshop
- Data Modeling
- Git / GitHub