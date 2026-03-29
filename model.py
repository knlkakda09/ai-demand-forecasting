import pandas as pd

def simple_forecast(df):
    # Very basic moving average forecast (placeholder)
    if 'sales' not in df.columns:
        return []

    forecast = df['sales'].rolling(window=3).mean().fillna(method='bfill')
    return forecast.tolist()
