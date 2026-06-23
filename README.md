# Sales ETL Pipeline & Mini Data Warehouse

## Overview

This project demonstrates an end-to-end ETL pipeline using Python, Pandas, PostgreSQL, and SQL.

The pipeline extracts sales data from a CSV file, performs cleaning and transformations, loads the data into PostgreSQL, and creates a Star Schema for analytical reporting.

---

## Technologies Used

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- psycopg2
- Git
- GitHub

---

## ETL Workflow

CSV Dataset
↓
Pandas
↓
Data Cleaning
↓
Feature Engineering
↓
PostgreSQL
↓
SQL Analysis
↓
Star Schema

---

## Transformations Performed

- Data Profiling
- Missing Value Analysis
- Duplicate Detection
- Revenue Column Creation
- Profit Margin Calculation
- CSV Export

---

## Data Warehouse Design

### Fact Table

Fact_Sales

Contains:

- Sales
- Profit
- Quantity
- Discount

### Dimension Tables

Customer_Dim

- Customer Name
- Segment
- State
- Region

Product_Dim

- Product Name
- Category
- Sub-Category

---

## SQL Analysis

### Top Revenue States

- California
- New York
- Texas
- Washington
- Pennsylvania

### Top Revenue Categories

- Technology
- Furniture
- Office Supplies

---

## Project Structure

Sales_ETL_Project

├── data

├── output

├── scripts

├── screenshots

└── README.md

---

## Author

Tanushree Ambade

Cyber Security Engineering

Aspiring Data Engineer
