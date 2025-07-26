import streamlit as st
import pandas as pd
from file_handler import load_and_clean_excel
from query_engine import ask_question
from visualizer import generate_chart

# Page setup
st.set_page_config(page_title="Conversational Excel Assistant", layout="wide")
st.markdown("## 🤖 Chatbot with Excel")
st.markdown("Upload an Excel file and ask natural language questions about the data.")

# File uploader
uploaded_file = st.file_uploader("📂 Upload your Excel file (.xlsx)", type=["xlsx"])

df = None

if uploaded_file:
    # Load and display file
    df = load_and_clean_excel(uploaded_file)
    
    st.markdown("### 🧾 Preview of Uploaded Data")
    with st.expander("🔍 Click to view data preview"):
        st.dataframe(df.head(20), use_container_width=True)

    st.markdown("---")

    # Question input
    st.markdown("### ❓ Ask a Question About Your Data")
    user_query = st.text_input(
        "Type your question here (e.g., What is the average score?)", 
        placeholder="Try asking: Which product has the highest revenue?"
    )

    # Process query
    if user_query and df is not None:
        with st.spinner("🧠 Analyzing your data..."):
            answer, chart_type, chart_code = ask_question(df, user_query)

        st.markdown("### ✅ Answer:")
        st.write(answer if answer else "Sorry, I couldn't find an exact answer.")

        # If chart is returned
        if chart_code and chart_type != "none":
            st.markdown("### 📊 Generated Chart:")
            fig = generate_chart(df, chart_code, chart_type)
            if fig:
                st.pyplot(fig)
            else:
                st.warning("⚠️ Could not generate chart from the query.")
