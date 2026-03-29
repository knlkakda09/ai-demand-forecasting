import streamlit as st
import pandas as pd
import requests

st.title("AI Demand Forecasting Tool")

file = st.file_uploader("Upload CSV with 'sales' column")

if file:
    df = pd.read_csv(file)
    st.write(df.head())

    if st.button("Generate Forecast"):
        response = {"forecast": df['sales'].rolling(3).mean().fillna(method='bfill').tolist()}
        st.write(response.json())
