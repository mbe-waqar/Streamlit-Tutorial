import streamlit as st

st.header("Chai Taste Poll")

col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    vote1 = st.button("Vote Masala Chai")

with col2:
    st.header("Ginger Chai")
    vote2 = st.button("Vote Ginger Chai")

if vote1:
    st.write("You voted for Masala Chai!")
elif vote2:
    st.write("You voted for Ginger Chai!")

name = st.sidebar.text_input("What's your name?")
tea_choice = st.sidebar.selectbox("Which tea would you like to vote for?", ["Masala Chai", "Ginger Chai", "Adrak Chai"])

st.write(f"Welcome, {name}! You chose {tea_choice} as your favorite tea.")