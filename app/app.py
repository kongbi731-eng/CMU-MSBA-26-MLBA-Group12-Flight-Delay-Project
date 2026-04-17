import streamlit as st
import pandas as pd
import joblib

# ===== setup page =====
st.set_page_config(page_title="Flight Delay Prediction", page_icon="✈️")

st.title("✈️ Flight Delay Prediction")

st.caption("Predict the probability of flight delay using schedule and distance features.")

st.write("Enter flight information:")

# ===== load model =====
import os

@st.cache_resource
def load_model():
    base_dir = os.path.dirname(__file__)
    model_path = os.path.join(base_dir, "../model.pkl")
    cols_path = os.path.join(base_dir, "../columns.pkl")

    model = joblib.load(model_path)
    cols = joblib.load(cols_path)
    return model, cols

# ===== user input =====
month = st.number_input("Month", min_value=1, max_value=12, value=7)
day = st.number_input("Day of Month", min_value=1, max_value=31, value=15)
weekday = st.number_input("Day of Week (1=Mon, 7=Sun)", min_value=1, max_value=7, value=3)
dep_time = st.number_input("Departure Time (HHMM)", min_value=0, max_value=2359, value=1200)
arr_time = st.number_input("Arrival Time (HHMM)", min_value=0, max_value=2359, value=1500)
distance = st.number_input("Distance (miles)", min_value=0.0, value=800.0)

st.write("Click predict to estimate delay risk for this flight.")

# predict button
if st.button("Predict"):

    # input
    input_df = pd.DataFrame({
        "MONTH": [month],
        "DAY_OF_MONTH": [day],
        "DAY_OF_WEEK": [weekday],
        "CRS_DEP_TIME": [dep_time],
        "CRS_ARR_TIME": [arr_time],
        "DISTANCE": [distance]
    })

    
    input_df = pd.get_dummies(input_df)
    input_df = input_df.reindex(columns=cols, fill_value=0)

    # predict
    prob = model.predict_proba(input_df)[0][1]

    
    if prob > 0.7:
        st.error(f"🔴 High Risk of Delay ({prob:.2f})")
    elif prob > 0.4:
        st.warning(f"🟡 Moderate Risk ({prob:.2f})")
    else:
        st.success(f"🟢 Low Risk ({prob:.2f})")

    
    st.caption("Probability represents likelihood of delay ≥ 15 minutes.")
