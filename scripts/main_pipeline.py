# scripts/main_pipeline.py

import pandas as pd
from src.data_layer.data_loader import DataLoader
from src.data_layer.data_cleaner import DataCleaner
from src.data_layer.feature_store import FeatureStore
from src.feature_engineering.lag_features import LagFeatures
from src.feature_engineering.interaction_features import InteractionFeatures
from src.feature_engineering.decomposition import Decomposition
from src.models.ml_models import MLModels
from src.models.model_trainer import ModelTrainer
from src.evaluation.metrics import Metrics
from src.monitoring.logger import Logger
import joblib

# -----------------------------
# 1. Load Data
# -----------------------------
Logger.log("Loading data...")
loader = DataLoader()
df = loader.load_csv("data/raw/option_prices.csv")

# -----------------------------
# 2. Clean Data
# -----------------------------
Logger.log("Cleaning data...")
cleaner = DataCleaner()
df = cleaner.handle_missing(df)
if not cleaner.validate_data(df):
    Logger.log("Data validation failed!")
    exit()

# -----------------------------
# 3. Feature Engineering
# -----------------------------
Logger.log("Generating features...")
lagger = LagFeatures()
df = lagger.create_lags(df, columns=["Price"], lag=12)

interactor = InteractionFeatures()
df = interactor.create_interactions(df, feature_pairs=[("Price", "Inflation"), ("Price", "InterestRate")])

decomposer = Decomposition()
trend, seasonal, resid = decomposer.decompose(df["Price"])
df["Trend"] = trend
df["Seasonal"] = seasonal

# Save processed features
store = FeatureStore()
store.save_features(df, "processed_features")

# -----------------------------
# 4. Prepare Data for Modeling
# -----------------------------
df.dropna(inplace=True)
X = df.drop(columns=["Price"])
y = df["Price"]

# -----------------------------
# 5. Train Models
# -----------------------------
Logger.log("Training ML models...")
ml_models = MLModels()
results = {}
for name, model in ml_models.models.items():
    trainer = ModelTrainer(model)
    trainer.train(X, y)
    results[name] = model

# Save one model as example
joblib.dump(results["RandomForest"], "models/random_forest.pkl")

# -----------------------------
# 6. Evaluate Models
# -----------------------------
Logger.log("Evaluating models...")
for name, model in results.items():
    y_pred = model.predict(X)
    rmse = Metrics.rmse(y, y_pred)
    mae = Metrics.mae(y, y_pred)
    mape = Metrics.mape(y, y_pred)
    Logger.log(f"{name} - RMSE: {rmse:.2f}, MAE: {mae:.2f}, MAPE: {mape:.2f}%")

