import streamlit as st
import pandas as pd
import requests

st.title("AI Demand Forecasting Tool")

file = st.file_uploader("Upload CSV with 'sales' column")

if file:
    df = pd.read_csv(file)
    st.write(df.head())

    if st.button("Generate Forecast"):
        response = requests.post("http://localhost:8000/forecast", json=df.to_dict())
        st.write(response.json())
