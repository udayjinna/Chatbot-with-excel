import pandas as pd
import re

def normalize_column_names(columns):
    return [re.sub(r'[^a-zA-Z0-9_]', '_', col.strip().lower()) for col in columns]

def load_and_clean_excel(uploaded_file):
    df = pd.read_excel(uploaded_file, engine="openpyxl")
    df.columns = normalize_column_names(df.columns)
    return df