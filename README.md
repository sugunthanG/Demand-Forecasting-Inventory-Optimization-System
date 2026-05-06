# Demand Forecasting & Inventory Optimization System

## Overview

The Demand Forecastin & Inventory Optimization System is and end-to-end machine learning application to predict future retail sales demand and provide intelligent stock allocation recommmendations.

This project uses historical store sales data, customer traffic patterns, promotional activity, and seasonal trends to forecast expected sales and optimize inventory planning.

The system helps businesses:

- Predict future demand
- Prevent stock shortages
- Reduce Overstocking
- Improve operational efficiency
- Support data-driven inventory decisions

----

## Problem statement

Retail businesses often face two major challenges:

## Understocking
Insufficient inventory lead to:

- Lost sales
- Customer dissatisfaction
- Revenue loss

## Overstocking
Excess inventory causes:

- Increased storage cost
- Product wastage
- Capital blockage

This project solves these challenges using machine learning-based forecasting.

---

## Business Objective

Build an intelligent demand forecasting system capable of:

- Predicting future sales demand
- Recommending optimal inventory levels
- Providing safety stock recommendations
- Helping managers make better operational decisions

---

# Dataset

### Dataset used
Rossmann Store Sales Dataset

## Source 
Kaggle

## Files Used

- train.csv
- store.csv
- processed_data.csv

---

## Features Used

| Feature       | Description             |
|---------------|-------------------------|
| Store         | Store identifier        |
| Customers     | Expected customer count |
| Promo         | Promotion activity      |
| SchoolHoliday | School holiday indicator|
| DayOfWeek     | Day of week             |
| Month         | Month                   |
| Year          | Year                    |
| Day           | Day of month            |
| WeekOfYear    | Week number             |
| Lag_1         | Previous day sales      |
| Lag_7         | Sales from 7 days ago   |


---

## Machine Learning Workflow

## 1. Data Preprocessing

performed:

- missing value handling
- Date conversion
- Feature extraction
- Store metadate merging
- Closed store removal
- Lag feature creation

---

## 2. Exploratory Data Analysis

Conducted detailed EDA to analyze:

- Daily sales trends
- Monthly seasonality
- Promotion impact
- Store Performmance
- Sales distribution
- Holiday effects

---

## 3. Feature Engineering

created time-based features:
 
- year
- Month
- Day
- Week of year
- Day of week

Created lag features:

- lag_1
- Lag_7

These capture temporal sales dependencies.

---
## 4. Model Building

### Model Used

Random Forest Regressor

### Why Random Forest?

Chosen because it:

- Handles nonlinear relationships
- Captures feature  interactions
- Performs well on structured tabular data
- Requires minimal scaling

---

## Model Evaluation

### Performance Metrics

**Mean Absolute Error (MAE)**
759.14

**Root Mean Squared Erro (RSME)**
1338506.70

---

## Key Feature Drivers

The most influential features:

- Customer traffic
- Promotional activity
- Previous day sales
- Weekly sales trends

---

## Inventory Optimization Logic

The system recommends inventory using:

Recommended Stock = Predicted Demand x Safety Factor

Safety factor used:

1.2

This adds a 20% safety buffer to handle unexpected demand spikes.

---

## Application Development

Built an interactive dashboard using Streamlit.

---

## Dashboard Features

### Demand Prediction

Forecasts expected sales units.

---

### Inventory Recommendation

Suggests stock allocation.

---

### Safety Buffer Calculation

Calculates reserve inventory.

---

### Sales Trend Visualization

Displays:

- 7 days ago sales
- Previous day sales
- Predicted sales

---

### Inventory Planning Chart

Visual comparison of:

- Predicted demand
- Safety stock
- Recommended inventory

---

### Feature Impact Analysis

Shows influence of:

- Customers
- Recent sales
- Weekly trends

---

### Business Insights

Provides:

- Demand classification
- Promotion impact analysis
- Operational recommendations

---

## Tech Stack

### Programming Language
Python

### Libraries
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib
- Streamlit

---

## Project Structure

```bash
Demand_Forecasting_Project/
│
├── app/
│   └── app.py
│
├── data/
│   ├── train.csv
│   ├── store.csv
│   └── processed_data.csv
│
├── models/
│   ├── demand_forecast_model.pkl
│   └── features.pkl
│
├── notebooks/
│   └── Demand_Forecasting_Final.ipynb
│
└── README.md
```

---
## Installation

Clone repository

```bash
git clone <repository-url>
cd Demand_Forecasting_Project
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run application

```bash
streamlit run app/app.py
```

---

## How It Works

### Input

User enters:

- Store details
- Customer expectations
- Promotion status
- Recent sales data

---

### Processing

Model evaluates input using trained Random Forest model.

---

### Output

System generates:

- Predicted sales
- Recommended inventory
- Safety buffer
- Operational insights

---

## Sample Output

### Forecast Results

Expected Sales: 9,791 units

Recommended Inventory: 11,749 units

Safety Buffer: 1,958 units

Demand Status: High

---

## Business Impact

This solution enables retailers to:

- Reduce stockouts
- Improve stock efficiency
- Increase operational readiness
- Support strategic planning

---

## Future Improvements

Planned upgrades:

- XGBoost implementation
- LSTM-based forecasting
- Multi-store forecasting
- Real-time sales API integration
- Automated inventory alerts
- Cloud deployment

---

## Learning Outcomes

This project demonstrates expertise in:

- Data preprocessing
- Exploratory data analysis
- Feature engineering
- Machine learning modeling
- Model deployment
- Dashboard development
- Business analytics

---

## Author

Sugunthan

Machine Learning Engineer | Data Scientist | AI Developer 

---

## Project Status

Completed and production-ready