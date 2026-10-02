import pandas as pd

def add_forecast(history, days=14):
    history = history.copy()
    history = history.sort_values("date")

    history["series"] = "Actual"

    if history.empty:
        return history

    average = history.tail(7)["units_sold"].mean()

    future_dates = pd.date_range(
        start=history["date"].max() + pd.Timedelta(days=1),
        periods=days,
        freq="D"
    )

    future = pd.DataFrame({
        "date": future_dates,
        "units_sold": [round(average, 2)] * days,
        "series": "Forecast"
    })

    return pd.concat(
        [history, future],
        ignore_index=True
    )