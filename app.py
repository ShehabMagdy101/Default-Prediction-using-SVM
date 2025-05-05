import streamlit as st
import numpy as np
import requests
import pandas as pd

st.header("Credit :blue[Default] Risk Prediction", divider=True)

def predict(features):
    endpoint = 'http://127.0.0.1:5000/predict'
    features = features.tolist()
    data = {"features": features}
    try:
        response = requests.post(endpoint, json=data)
        return response.json()["prediction"]
    except Exception as e:
        st.error(f"Error predicting the model: {str(e)}")
        return None

with st.expander("Predict Credit Default Risk", expanded=True):
    st.subheader("Enter customer information")

    LIMIT_BAL = st.number_input("Limit Balance (USD)", min_value=0.0, value=20000.0, format="%.5f")
    SEX = st.selectbox("Sex", ("Male", "Female"))
    EDUCATION = st.selectbox("Education Level", ("Graduate School", "University", "High School", "Others"))
    MARRIAGE = st.selectbox("Marital Status", ("Single", "Married", "Others"))
    AGE = st.number_input("Age", min_value=18.0, value=30.0, format="%.5f")

    PAY_1 = st.slider("Repayment status in September", -2, 8, 0)
    PAY_2 = st.slider("Repayment status in August", -2, 8, 0)
    PAY_3 = st.slider("Repayment status in July", -2, 8, 0)
    PAY_4 = st.slider("Repayment status in June", -2, 8, 0)
    PAY_5 = st.slider("Repayment status in May", -2, 8, 0)
    PAY_6 = st.slider("Repayment status in April", -2, 8, 0)

    BILL_AMT1 = st.number_input("Bill Amount in September", min_value=0.0, value=5000.0, format="%.5f")
    PAY_AMT1 = st.number_input("Payment Amount in September", min_value=0.0, value=1000.0, format="%.5f")
    PAY_AMT2 = st.number_input("Payment Amount in August", min_value=0.0, value=1000.0, format="%.5f")
    PAY_AMT3 = st.number_input("Payment Amount in July", min_value=0.0, value=1000.0, format="%.5f")
    PAY_AMT4 = st.number_input("Payment Amount in June", min_value=0.0, value=1000.0, format="%.5f")
    PAY_AMT5 = st.number_input("Payment Amount in May", min_value=0.0, value=1000.0, format="%.5f")
    PAY_AMT6 = st.number_input("Payment Amount in April", min_value=0.0, value=1000.0, format="%.5f")

    # Encode categorical values
    SEX = 1 if SEX == "Male" else 2
    EDUCATION = {"Graduate School": 1, "University": 2, "High School": 3, "Others": 4}[EDUCATION]
    MARRIAGE = {"Single": 1, "Married": 2, "Others": 3}[MARRIAGE]

    features = np.array([
        LIMIT_BAL, SEX, EDUCATION, MARRIAGE, AGE,
        PAY_1, PAY_2, PAY_3, PAY_4, PAY_5, PAY_6,
        BILL_AMT1,
        PAY_AMT1, PAY_AMT2, PAY_AMT3, PAY_AMT4, PAY_AMT5, PAY_AMT6
    ])

    if st.button("Predict"):
        with st.spinner("Calculating..."):
            prediction = predict(features)
            if prediction:
                st.success(prediction)

"_by Shehab_"
