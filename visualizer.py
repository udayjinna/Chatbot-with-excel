import matplotlib.pyplot as plt

def generate_chart(df, chart_code, chart_type):
    try:
        exec_globals = {"df": df.copy()}
        exec(chart_code, exec_globals)

        data = exec_globals.get("chart_data")
        fig, ax = plt.subplots()

        if chart_type == "bar":
            data.plot(kind="bar", ax=ax)
        elif chart_type == "line":
            data.plot(kind="line", ax=ax)
        elif chart_type == "hist":
            data.plot(kind="hist", ax=ax)
        else:
            return None

        ax.set_title("Generated Chart")
        ax.set_xlabel(data.columns[0])
        ax.set_ylabel("Value")
        return fig

    except Exception as e:
        print(f"Chart generation failed: {e}")
        return None