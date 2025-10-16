import pandas as pd

class LagFeatures:
    def __init__(self):
        pass

    def create_lags(self, df: pd.DataFrame, columns: list, lag: int=12) -> pd.DataFrame:
        for col in columns:
            for i in range(1, lag+1):
                df[f"{col}_lag_{i}"] = df[col].shift(i)
        return df
