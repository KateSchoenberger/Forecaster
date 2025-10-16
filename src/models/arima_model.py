import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import joblib

class ARIMAForecaster:
    def __init__(self, order=(1,1,1)):
        self.order = order
        self.model_fit = None

    def train(self, series: pd.Series):
        model = ARIMA(series, order=self.order)
        self.model_fit = model.fit()
        return self

    def forecast(self, steps=12):
        if self.model_fit is None:
            raise ValueError("Model not trained yet.")
        return self.model_fit.forecast(steps=steps)

    def save_model(self, path="models/arima_model.pkl"):
        joblib.dump({"order": self.order, "model_fit": self.model_fit}, path)

    def load_model(self, path="models/arima_model.pkl"):
        data = joblib.load(path)
        self.order = data["order"]
        self.model_fit = data["model_fit"]
