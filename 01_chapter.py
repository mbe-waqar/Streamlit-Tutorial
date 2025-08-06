import streamlit as st

st.title("hello world")
st.subheader("my first app")
st.text("welcome to my app")
st.write("chose a number")

num = st.selectbox("your fav number", [1, 2, 3, 4, 5])

st.write(f"you choose a {num} ")

st.success(f"Your fav number is {num}")