import pandas as pd

class DataLoader:
    def __init__(self):
        pass

    def load_csv(self, filepath: str) -> pd.DataFrame:
        """
        Load CSV file into DataFrame.
        """
        return pd.read_csv(filepath, parse_dates=True, index_col=0)

    def load_api(self, endpoint: str) -> pd.DataFrame:
        """
        Load data from an API endpoint.
        """
        # TODO: Implement API fetching
        pass

    def load_database(self, query: str):
        """
        Load data from database.
        """
        # TODO: Implement DB query
        pass
