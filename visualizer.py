import matplotlib.pyplot as plt

def generate_chart(df, chart_code, chart_type):
    try:
        exec_globals = {"df": df.copy()}
        exec(chart_code, exec_globals)
        chart_data = exec_globals.get("chart_data")

        if chart_data is None or chart_data.empty:
            print("⚠️ chart_data is missing or empty.")
            return None

        fig, ax = plt.subplots()

        if chart_type == "bar":
            chart_data.plot(kind="bar", ax=ax)
        elif chart_type == "line":
            chart_data.plot(kind="line", ax=ax)
        elif chart_type == "hist":
            chart_data.plot(kind="hist", ax=ax)
        else:
            return None

        ax.set_title("Generated Chart")
        ax.set_xlabel(chart_data.columns[0])
        ax.set_ylabel("Value")
        return fig

    except Exception as e:
        print(f"Chart generation failed: {e}")
        return None
