import pandas as pd
import re

def normalize_column_names(columns):
    # Only normalize column names, not values
    return [re.sub(r'[^a-zA-Z0-9_]', '_', str(col).strip().lower()) for col in columns]

def load_and_clean_excel(uploaded_file):
    try:
        df = pd.read_excel(uploaded_file, engine="openpyxl", header=0)
    except Exception:
        df = pd.read_excel(uploaded_file, engine="openpyxl", header=None)
        df.columns = df.iloc[0]
        df = df[1:]

    df.columns = normalize_column_names(df.columns)
    return df
