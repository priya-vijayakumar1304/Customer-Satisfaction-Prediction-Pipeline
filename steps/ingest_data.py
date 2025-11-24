import logging

import pandas as pd
from zenml import step

class IngestData:
    """
    Ingesting data from the data path
    """
    def __init__(self, data_path: str):
        """
        Args:
            data_path: Path to the data
        """
        self.data_path = data_path
    
    def get_data(self):
        """
        Ingesting the data from the data path
        """
        logging.info(f"Ingesting data from {self.data_path}")
        return pd.read_csv(self.data_path)
    
@step
def ingest_df(data_path:str) -> pd.DataFrame:
    """
    Ingesting the data from the data path

    Args:
        data_path: Path to the data
    Returns:
        pd.DataFrame: Ingested data as a pandas DataFrame

    """
    try:
        ingest_data = IngestData(data_path)
        return ingest_data.get_data()
    except Exception as e:
        logging.error(f"Error while ingesting data: {e}")
        raise e
