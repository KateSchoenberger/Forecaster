from sklearn.model_selection import GridSearchCV

class ModelTrainer:
    def __init__(self, model):
        self.model = model

    def train(self, X, y):
        self.model.fit(X, y)
        return self

    def hyperparameter_tune(self, param_grid, X, y, cv=5):
        grid = GridSearchCV(self.model, param_grid, cv=cv)
        grid.fit(X, y)
        self.model = grid.best_estimator_
        return self.model
