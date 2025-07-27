import matplotlib.pyplot as plt

def generate_chart(df, chart_code, chart_type):
    try:
        local_context = {"df": df.copy()}
        exec(chart_code, {}, local_context)

        chart_data = local_context.get("chart_data")
        if chart_data is None or chart_data.empty:
            print("⚠️ chart_data not found or empty")
            return None

        fig, ax = plt.subplots()
        chart_data.plot(kind=chart_type, ax=ax)

        ax.set_title("Generated Chart")
        ax.set_xlabel(chart_data.columns[0])
        ax.set_ylabel("Value")

        plt.tight_layout()  # ✅ Makes sure chart isn't cut off
        return fig

    except Exception as e:
        print("Chart generation error:", e)
        return None
