import streamlit as st

st.header("In Search for Happiness")

x = st.selectbox(options=["GDP", "Happiness", "Generosity"],
                 label="Select the data for X-axis")
y = st.selectbox(options=["GDP", "Happiness", "Generosity"],
                 label="Select the data for Y-axis")

st.subheader(f"{x} and {y}")