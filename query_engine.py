import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

def ask_question(df, question):
    prompt = f"""
You are a data analyst. You are provided with a pandas DataFrame named 'df'.
This is the data:
{df.head(20).to_csv(index=False)}

A user asked the question: "{question}"

Your job is to:
1. Answer using **actual values** from the data.
2. If suitable, suggest a chart and provide valid Python pandas code to create a variable called `chart_data`.

Respond strictly in this format:

ANSWER: <short factual answer using actual values>
CHART_TYPE: <bar/line/hist/none>
CHART_CODE: <Python code to assign chart_data>
"""
    response = model.generate_content(prompt)
    content = response.text

    answer, chart_type, chart_code = "", "none", ""
    for line in content.splitlines():
        if line.startswith("ANSWER:"):
            answer = line.replace("ANSWER:", "").strip()
        elif line.startswith("CHART_TYPE:"):
            chart_type = line.replace("CHART_TYPE:", "").strip().lower()
        elif line.startswith("CHART_CODE:"):
            chart_code = line.replace("CHART_CODE:", "").strip()
    return answer, chart_type, chart_code
