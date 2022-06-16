import pandas as pd
import unicodedata


def full_to_half(df: pd.DataFrame, columns_name="rooms"):
    df[columns_name] = df[columns_name].map(lambda x: unicodedata.normalize("NFKC", x))
    return df
