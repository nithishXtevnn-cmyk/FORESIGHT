import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="FORESIGHT",
    page_icon="📦",
    layout="wide"
)

st.title("📦 FORESIGHT")
st.subheader("Demand Forecasting & Inventory Intelligence")

st.write(
    "Welcome to FORESIGHT, your demand forecasting "
    "and inventory management dashboard."
)


data = {
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone"],
    "Units Sold": [25, 40, 15, 30, 50],
    "Stock": [100, 120, 60, 90, 110]
}

df = pd.DataFrame(data)


col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", int(df["Units Sold"].sum()))
col2.metric("Products", df["Product"].nunique())
col3.metric("Total Stock", int(df["Stock"].sum()))


st.header("Sales Overview")

fig = px.bar(
    df,
    x="Product",
    y="Units Sold",
    color="Product",
    title="Product Sales"
)

st.plotly_chart(fig, use_container_width=True)


st.header("Inventory Overview")

st.dataframe(df, use_container_width=True)