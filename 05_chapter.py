import streamlit as st
import requests

st.header("Live Currency Converter")
st.write("This app converts currencies in real-time using the ExchangeRate-API")
amount = st.number_input("Enter the amount in PKR", min_value=1)
target_currency = st.selectbox("Convert to", ["USD", "EUR", "GBP", "JPY"])

if st.button("Convert"):
    api_url = f"https://api.exchangerate-api.com/v4/latest/PKR"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        exchange_rate = data["rates"][target_currency]
        converted_amount = amount * exchange_rate
        st.success(f"{amount} PKR is equal to {converted_amount: ,.2f} {target_currency}")
    else:
        st.error("Failed to fetch data")