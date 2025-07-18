from openai import OpenAI
import os

# ✅ Create OpenAI client using the new v1+ syntax
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_question(df, question):
    prompt = f"""
    You are a data analyst. Convert the following question into pandas code to run on a DataFrame named df:
    DataFrame info: {list(df.columns)}
    Question: {question}
    Return the result and also if a chart is needed, mention the chart type and code.
    Format your response as:
    ANSWER: <short text summary of result>
    CHART_TYPE: <bar/hist/line/none>
    CHART_CODE: <pandas code to generate data for chart>
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    content = response.choices[0].message.content
    lines = content.split("\n")
    answer = lines[0].replace("ANSWER: ", "")
    chart_type = lines[1].replace("CHART_TYPE: ", "")
    chart_code = "\n".join(lines[2:]).replace("CHART_CODE: ", "")
    return answer, chart_type, chart_code
