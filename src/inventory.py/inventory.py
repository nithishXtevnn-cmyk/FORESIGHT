import pandas as pd

def inventory_summary(df):
    latest = (
        df.sort_values("date")
        .groupby("product", as_index=False)
        .tail(1)[["product", "stock"]]
    )

    demand = (
        df.groupby("product", as_index=False)["units_sold"]
        .mean()
        .rename(columns={"units_sold": "avg_daily_demand"})
    )

    result = latest.merge(
        demand,
        on="product",
        how="left"
    )

    result["estimated_days_left"] = result.apply(
        lambda row: round(
            row["stock"] / row["avg_daily_demand"], 1
        ) if row["avg_daily_demand"] > 0 else None,
        axis=1
    )

    result["status"] = result["estimated_days_left"].apply(
        lambda days: "Low stock"
        if pd.notna(days) and days < 7
        else ("Check demand" if pd.isna(days) else "OK")
    )

    return result