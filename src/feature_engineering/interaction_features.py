import pandas as pd

class InteractionFeatures:
    def __init__(self):
        pass

    def create_interactions(self, df: pd.DataFrame, feature_pairs: list) -> pd.DataFrame:
        for f1, f2 in feature_pairs:
            df[f"{f1}_x_{f2}"] = df[f1] * df[f2]
        return df
