import streamlit as st

st.title("Chai Maker App")

if st.button("Make Chai"):
    st.success("your chai is ready")

add_masala = st.checkbox("Add Masala")

if add_masala:
    st.write("Masala added to your chai")

tea_type = st.radio("Pick a tea type", ["Black", "Green", "Herbal"])
st.write(f"Selected tea type: {tea_type}")

flavor = st.selectbox("Pick a flavor", ["Vanilla", "Cinnamon", "Ginger"])
st.write(f"Selected flavor: {flavor}")

sugar = st.slider("Add sugar", 0, 5, 2)
st.write(f"Added sugar: {sugar} spoons")