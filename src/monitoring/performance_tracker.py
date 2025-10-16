import pandas as pd

class PerformanceTracker:
    def __init__(self):
        self.history = pd.DataFrame()

    def log_metrics(self, metrics_dict):
        self.history = pd.concat([self.history, pd.DataFrame([metrics_dict])], ignore_index=True)
