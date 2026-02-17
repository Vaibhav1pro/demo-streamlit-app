import streamlit as st

# Page Title
st.title("🚀 My First Streamlit App")

# Text
st.write("Hello Vaibhav! Welcome to Streamlit.")

# User Input
name = st.text_input("Enter your name:")

if name:
    st.success(f"Hello {name}, keep building your AI SaaS 🔥")

# Slider
age = st.slider("Select your age:", 10, 50, 20)
st.write("Your age is:", age)

# Button
if st.button("Click Me"):
    st.balloons()
    st.write("You clicked the button!")

# Checkbox
if st.checkbox("Show Motivation"):
    st.info("You are going to crack highest placement 💪")

# Simple chart
import pandas as pd
import numpy as np

data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

st.line_chart(data)
