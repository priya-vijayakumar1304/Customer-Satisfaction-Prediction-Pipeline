import logging
import pandas as pd
from zenml import step

@step
def train_model(df:pd.DataFrame) -> None:
    """
    Training the model on the cleaned data

    Args:
        df: Cleaned data as a pandas DataFrame

    """
    pass
