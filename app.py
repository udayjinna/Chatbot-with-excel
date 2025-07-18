import streamlit as st
import pandas as pd
from helpers.file_handler import load_and_clean_excel
from helpers.query_engine import ask_question
from helpers.visualizer import generate_chart

st.set_page_config(page_title="Conversational Excel Assistant", layout="wide")
st.title("📊 Conversational Excel Assistant")

uploaded_file = st.file_uploader("Upload your Excel file (.xlsx)", type=["xlsx"])
df = None

if uploaded_file:
    df = load_and_clean_excel(uploaded_file)
    st.subheader("Preview of Uploaded Data")
    st.dataframe(df.head())

    st.subheader("Ask a Question About Your Data")
    user_query = st.text_input("Type your question here (e.g., What is the average sales?)")

    if user_query:
        with st.spinner("Processing your query..."):
            answer, chart_type, chart_code = ask_question(df, user_query)
            st.write("\n**Answer:**")
            st.write(answer)

            if chart_code and chart_type:
                st.write("\n**Generated Chart:**")
                fig = generate_chart(df, chart_code, chart_type)
                if fig:
                    st.pyplot(fig)
                else:
                    st.warning("Could not generate chart from the query.")
