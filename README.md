# Enterprise ETL Pipeline IN Palantir Foundry

over all process
# NYC Food-Only Restaurant Data Engineering project (Palantir Foundry Project)

## 📌 Project Overview

This project demonstrates an end-to-end data engineering workflow built in Palantir Foundry using:

- Pipeline Builder
- Medallion Architecture (Raw → Silver → Gold)
- Data Filtering Logic (Food-only restaurants)
- Ontology Workshop Modeling
- Object Relationships & Preview
- Git Version Control

- ## 🎯 Business Objective

NYC restaurant inspection data includes various establishment types such as:
- Full-service restaurants
- Grocery stores
- Alcohol-only establishments

The goal of this project was to:
- Identify and retain only food-serving restaurants
- Exclude non-restaurant entities
- Produce a clean, analytics-ready dataset
- Model entities using Foundry Ontology for relationship-based analysis

---

## 🏗 Pipeline Architecture

## 🏗 End-to-End Architecture

This project follows a Medallion architecture pattern:

Raw (Bronze) → Cleaned (Silver) → Aggregated (Gold) → Ontology Modeling → Object Validation

<p align="center">
  <img src="docs/screenshots/pipeline_builder_raw_silver_gold_overview.png" width="900"/>
</p>

This pipeline follows Medallion Architecture principles:
- Raw layer ingestion
- Silver layer cleaning & filtering
- Gold layer aggregation


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
