import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(model_name="models/gemini-2.5-pro")


def ask_question(df, question):
    # Use only a limited number of rows if it's too big
    csv_preview = df.head(200).to_csv(index=False)

    prompt = f"""
You are a helpful data assistant working with a pandas DataFrame. Based on the following CSV data:

{csv_preview}

Answer this question clearly: "{question}"

Respond strictly in this format:
ANSWER: <actual answer to user's question>
CHART_TYPE: <bar/line/hist/none>
CHART_CODE: <pandas code to assign chart_data>

Only provide actual answer from the data, not explanation or steps. If chart is not needed, set CHART_TYPE to none.
"""

    response = model.generate_content(prompt)
    content = response.text

    # Extract response parts
    answer, chart_type, chart_code = "", "none", ""
    for line in content.splitlines():
        if line.startswith("ANSWER:"):
            answer = line.replace("ANSWER:", "").strip()
        elif line.startswith("CHART_TYPE:"):
            chart_type = line.replace("CHART_TYPE:", "").strip()
        elif line.startswith("CHART_CODE:"):
            chart_code = line.replace("CHART_CODE:", "").strip()

    return answer, chart_type, chart_code


