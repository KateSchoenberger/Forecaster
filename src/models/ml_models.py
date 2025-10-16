from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR

class MLModels:
    def __init__(self):
        self.models = {
            "RandomForest": RandomForestRegressor(),
            "GradientBoosting": GradientBoostingRegressor(),
            "SVR": SVR()
        }

    def get_model(self, name: str):
        return self.models.get(name, None)
