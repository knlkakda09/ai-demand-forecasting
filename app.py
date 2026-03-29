from fastapi import FastAPI
import pandas as pd
from model import simple_forecast

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Demand Forecasting API Running"}

@app.post("/forecast")
def forecast(data: dict):
    df = pd.DataFrame(data)
    result = simple_forecast(df)
    return {"forecast": result}
