import streamlit as st
import pandas as pd

# Title and headers
st.title("Welcome to WSCube")
st.header("Python Programming")
st.subheader("Java Programming")
st.markdown("### I Love Coding")

# Displaying a code snippet
st.code("for i in range(2, 9, 23):")

# Loading and displaying the dataset
try:
    dataset = pd.read_csv("data.csv")
    st.dataframe(dataset)
except FileNotFoundError:
    st.error(
        "The file 'data.csv' was not found. Please ensure it is in the correct location."
    )

# User inputs
name = st.text_input("Enter your name:")
father_name = st.text_input("Enter your father's name:")
address = st.text_area("Enter your address:")
class_data = st.selectbox("Select your class:", [1, 2, 3, 4, 5, 6, 7, 8])

# Display entered data (optional)
if st.button("Submit"):
    st.write(f"Name: {name}")
    st.write(f"Father's Name: {father_name}")
    st.write(f"Address: {address}")
    st.write(f"Class: {class_data}")
