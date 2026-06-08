import pandas as pd

def extract_sales(path: str) -> pd.DataFrame:
    return pd.read_excel(path)
