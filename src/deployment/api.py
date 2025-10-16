from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/forecast")
def get_forecast():
    # TODO: Load model and return forecast
    return {"message": "Forecast endpoint not implemented yet"}
