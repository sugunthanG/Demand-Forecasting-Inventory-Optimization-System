import os
import streamlit as st
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ---------------------------------------------------
# PATH CONFIGURATION
# ---------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "models",
    "demand_forecast_model.pkl"
)

FEATURES_PATH = os.path.join(
    BASE_DIR,
    "..",
    "models",
    "features.pkl"
)


# ---------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------
model = joblib.load(MODEL_PATH)
features = joblib.load(FEATURES_PATH)


# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Demand Forecasting Dashboard",
    layout="wide"
)


# ---------------------------------------------------
# TITLE
# ---------------------------------------------------
st.title("Demand Forecasting & Inventory Optimization")

st.markdown("""
This dashboard predicts future store demand using machine learning
and provides intelligent inventory planning recommendations.
""")


# ---------------------------------------------------
# SIDEBAR INPUTS
# ---------------------------------------------------
st.sidebar.header("Input Features")

store = st.sidebar.number_input("Store ID", 1, 1115, 1)

customers = st.sidebar.number_input(
    "Expected Customers",
    0,
    5000,
    500
)

promo = st.sidebar.selectbox(
    "Promotion Active",
    [0, 1]
)

school_holiday = st.sidebar.selectbox(
    "School Holiday",
    [0, 1]
)

day_of_week = st.sidebar.slider(
    "Day of Week",
    0,
    6,
    2
)

month = st.sidebar.slider(
    "Month",
    1,
    12,
    6
)

year = st.sidebar.number_input(
    "Year",
    2024,
    2030,
    2026
)

day = st.sidebar.slider(
    "Day",
    1,
    31,
    15
)

week_of_year = st.sidebar.slider(
    "Week of Year",
    1,
    52,
    24
)

lag_1 = st.sidebar.number_input(
    "Previous Day Sales",
    0,
    50000,
    5000
)

lag_7 = st.sidebar.number_input(
    "Sales 7 Days Ago",
    0,
    50000,
    4500
)


# ---------------------------------------------------
# INPUT DATAFRAME
# ---------------------------------------------------
input_data = pd.DataFrame([[
    store,
    customers,
    promo,
    school_holiday,
    day_of_week,
    month,
    year,
    day,
    week_of_year,
    lag_1,
    lag_7
]], columns=features)


# ---------------------------------------------------
# PREDICTION BUTTON
# ---------------------------------------------------
if st.button("Predict Demand"):

    prediction = model.predict(input_data)[0]

    safety_factor = 1.2
    recommended_stock = prediction * safety_factor
    safety_buffer = recommended_stock - prediction

    st.markdown("---")
    st.subheader("Forecast Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Expected Sales",
            f"{int(prediction):,} units"
        )

    with col2:
        st.metric(
            "Recommended Inventory",
            f"{int(recommended_stock):,} units"
        )

    with col3:
        st.metric(
            "Safety Buffer",
            f"{int(safety_buffer):,} units"
        )



    # ---------------------------------------------------
    # GRAPH 1: SALES TREND
    # ---------------------------------------------------
    st.markdown("### Sales Trend Visualization")

    trend_data = pd.DataFrame({
        "Period": [
            "7 Days Ago",
            "Previous Day",
            "Predicted"
        ],
        "Sales": [
            lag_7,
            lag_1,
            prediction
        ]
    })

    fig1, ax1 = plt.subplots(figsize=(10, 5))

    ax1.plot(
        trend_data["Period"],
        trend_data["Sales"],
        marker="o"
    )

    ax1.set_title("Sales Trend Forecast")
    ax1.set_ylabel("Units")

    st.pyplot(fig1)



    # ---------------------------------------------------
    # GRAPH 2: INVENTORY COMPARISON
    # ---------------------------------------------------
    st.markdown("### Inventory Planning")

    inventory_chart = pd.DataFrame({
        "Category": [
            "Predicted Demand",
            "Safety Buffer",
            "Recommended Inventory"
        ],
        "Units": [
            prediction,
            safety_buffer,
            recommended_stock
        ]
    })

    st.bar_chart(
        inventory_chart.set_index("Category")
    )



    # ---------------------------------------------------
    # GRAPH 3: FEATURE IMPACT
    # ---------------------------------------------------
    st.markdown("### Input Influence Analysis")

    feature_values = pd.DataFrame({
        "Feature": [
            "Customers",
            "Previous Day Sales",
            "7 Day Sales"
        ],
        "Value": [
            customers,
            lag_1,
            lag_7
        ]
    })

    st.bar_chart(
        feature_values.set_index("Feature")
    )



    # ---------------------------------------------------
    # DEMAND STATUS
    # ---------------------------------------------------
    st.markdown("### Demand Analysis")

    if prediction < 3000:
        st.error("Low customer demand expected.")

    elif prediction < 8000:
        st.warning("Moderate sales expected.")

    else:
        st.success("High customer demand expected.")



    # ---------------------------------------------------
    # PROMOTION IMPACT
    # ---------------------------------------------------
    st.markdown("### Promotion Impact")

    if promo == 1:
        st.success(
            "Promotion is active. Historical patterns suggest increased sales."
        )
    else:
        st.info(
            "No active promotion. Forecast based on organic demand."
        )



    # ---------------------------------------------------
    # DETAILED EXPLANATION
    # ---------------------------------------------------
    st.markdown("### Detailed Business Interpretation")

    st.info(f"""
**Forecast Summary**

The machine learning model evaluated:

- Historical store performance
- Customer traffic
- Promotional impact
- Seasonal sales patterns
- Recent demand trends

**Prediction**

Expected sales: **{int(prediction):,} units**

Recommended stock allocation:
**{int(recommended_stock):,} units**

Safety reserve:
**{int(safety_buffer):,} units**

This reserve helps prevent stock shortages.
""")


    # ---------------------------------------------------
    # OPERATIONAL RECOMMENDATIONS
    # ---------------------------------------------------
    st.markdown("### Operational Recommendations")

    recommendations = []

    if prediction > 8000:
        recommendations.append(
            "Increase warehouse stock immediately."
        )
        recommendations.append(
            "Prepare extra operational staff."
        )

    if promo == 1:
        recommendations.append(
            "Monitor fast-selling products closely."
        )

    if school_holiday == 1:
        recommendations.append(
            "Adjust stock based on altered customer behavior."
        )

    if prediction < 3000:
        recommendations.append(
            "Avoid overstocking."
        )

    if not recommendations:
        recommendations.append(
            "Maintain standard stock allocation."
        )

    for rec in recommendations:
        st.write(f"• {rec}")



    # ---------------------------------------------------
    # INPUT SUMMARY
    # ---------------------------------------------------
    st.markdown("### Input Summary")

    summary = pd.DataFrame({
        "Feature": features,
        "Value": input_data.iloc[0].values
    })

    st.dataframe(summary, use_container_width=True)