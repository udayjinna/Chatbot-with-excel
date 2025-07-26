def load_and_clean_excel(uploaded_file):
    try:
        # Try reading the first few rows to identify actual header
        df_raw = pd.read_excel(uploaded_file, header=None)
        st.write("Raw Preview:", df_raw.head(5))  # Debug step

        # Manually set header row (e.g., row 1 or 2 depending on your file)
        header_row_index = 1
        df = pd.read_excel(uploaded_file, header=header_row_index)
        df = df.dropna(how="all")  # Drop empty rows
        df.columns = df.columns.str.strip()  # Clean column names
        return df

    except Exception as e:
        st.error(f"Error loading Excel file: {e}")
        return None
