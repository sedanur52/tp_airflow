import pandas as pd

def remove_negative_amounts(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["amount"] >= 0]

def normalize_dates(df: pd.DataFrame) -> pd.DataFrame:
    df["date"] = pd.to_datetime(df["date"])
    return df

def transform_sales(df: pd.DataFrame) -> pd.DataFrame:
    df = normalize_dates(df)
    df = remove_negative_amounts(df)
    return df
