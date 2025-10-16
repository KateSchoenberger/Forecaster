import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

class Decomposition:
    def __init__(self):
        pass

    def decompose(self, series: pd.Series, period: int=12):
        """
        Returns trend, seasonal, residual components
        """
        result = seasonal_decompose(series, model='additive', period=period)
        return result.trend, result.seasonal, result.resid
