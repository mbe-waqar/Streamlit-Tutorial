import streamlit as st
import pandas as pd

st.title("Chai Sales Dashboard")

file = st.file_uploader("Choose a CSV file", type="csv")

if file:
    data = pd.read_csv(file)
    st.subheader("Data Overview")
    st.dataframe(data)

if file:
    st.subheader("Data Statistics")
    st.write(data.describe())

if file:
    cities = data["City"].unique()
    selected_city = st.selectbox("Select a city", cities)
    filtered_data = data[data["City"] == selected_city]
    st.dataframe(filtered_data)