import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

def ask_question(df, question):
    prompt = f"""
    You are a data analyst. Here are the columns in a DataFrame: {list(df.columns)}.
    A user asked: "{question}"
    Please provide:
    1. A short summary answer.
    2. If a chart is useful, suggest the chart type and provide pandas code to prepare chart_data.
    Respond in this format:
    ANSWER: ...
    CHART_TYPE: ...
    CHART_CODE: ...
    """
    
    response = model.generate_content(prompt)
    content = response.text

    # Extract answer parts
    answer = ""
    chart_type = "none"
    chart_code = ""
    
    for line in content.splitlines():
        if line.startswith("ANSWER:"):
            answer = line.replace("ANSWER:", "").strip()
        elif line.startswith("CHART_TYPE:"):
            chart_type = line.replace("CHART_TYPE:", "").strip()
        elif line.startswith("CHART_CODE:"):
            chart_code = line.replace("CHART_CODE:", "").strip()

    return answer, chart_type, chart_code
