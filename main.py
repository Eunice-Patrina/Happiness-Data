import streamlit as st
import pandas as pd
import plotly.express as px

st.header("In Search for Happiness")

x = st.selectbox(options=["GDP", "Happiness", "Generosity"],
                 label="Select the data for X-axis")
y = st.selectbox(options=["GDP", "Happiness", "Generosity"],
                 label="Select the data for Y-axis")

st.subheader(f"{x} and {y}")

df = pd.read_csv("happy.csv")
xa = list(df[x.lower()].squeeze())
ya = list(df[y.lower()].squeeze())


fig = px.scatter(x=xa, y=ya, labels={"x": x, "y": y})
st.plotly_chart(fig)
