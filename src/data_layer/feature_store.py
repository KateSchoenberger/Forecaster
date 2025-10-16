import pandas as pd
import os

class FeatureStore:
    def __init__(self, path="data/processed/"):
        self.path = path
        os.makedirs(self.path, exist_ok=True)

    def save_features(self, df: pd.DataFrame, name: str):
        df.to_csv(f"{self.path}/{name}.csv")

    def load_features(self, name: str) -> pd.DataFrame:
        return pd.read_csv(f"{self.path}/{name}.csv", index_col=0, parse_dates=True)
