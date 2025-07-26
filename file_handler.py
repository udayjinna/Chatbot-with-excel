import pandas as pd
import re

def normalize_column_names(columns):
    return [re.sub(r'[^a-zA-Z0-9_]', '_', str(col).strip().lower()) for col in columns]

def load_and_clean_excel(uploaded_file):
    try:
        # Try reading the first few rows without headers
        preview_df = pd.read_excel(uploaded_file, header=1, engine="openpyxl")
        
        # Automatically detect header row by checking where most non-null values appear
        header_row_index = preview_df.notna().sum(axis=1).idxmax()

        # Read again using that row as header
        df = pd.read_excel(uploaded_file, header=header_row_index, engine="openpyxl")
        
        # Normalize the column names
        df.columns = normalize_column_names(df.columns)

        # Drop completely empty rows
        df.dropna(how='all', inplace=True)

        return df
    except Exception as e:
        print("Error loading Excel file:", e)
        return pd.DataFrame()  # Return empty DataFrame if error
