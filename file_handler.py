import pandas as pd
import re

def normalize_column_names(columns):
    # Replace special characters and extra spaces with underscores
    return [re.sub(r'[^a-zA-Z0-9_]', '_', col.strip().lower()) for col in columns]

def load_excel(uploaded_file):
    # Read the Excel file using openpyxl engine
    df = pd.read_excel(uploaded_file, engine="openpyxl")
    
    # Normalize column names to avoid issues with special characters
    df.columns = normalize_column_names(df.columns)
    
    return df
