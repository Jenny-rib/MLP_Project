import streamlit as st
import pandas as pd
import numpy as np
import time
np.random.seed(int(time.time()))

# Page title and layout
st.set_page_config(page_title="CTR Prediction Demo", layout="wide")
st.title("🎯 Click-Through Rate (CTR) Prediction Demo")
st.markdown(
    """
    Welcome to the **CTR Prediction Demo**! 🚀  
    Explore the dataset, analyze features, and simulate predictions for click-through rates.  
    Use the sidebar to enter feature values and get a simulated prediction.  
    """
)

# Function to generate sample data
def generate_sample_data():
    num_samples = 10000
    data = {
        "id": np.arange(1, num_samples + 1),
        "click": np.random.choice([0, 1], num_samples, p=[0.8, 0.2]),
        "hour": np.random.randint(0, 24, num_samples),
        "banner_pos": np.random.choice([0, 1, 2, 3, 4], num_samples),
        "site_id": np.random.choice(["site_" + str(i) for i in range(1, 11)], num_samples),
        "site_domain": np.random.choice(["domain_" + str(i) for i in range(1, 11)], num_samples),
        "site_category": np.random.choice(["category_" + str(i) for i in range(1, 6)], num_samples),
        "device_type": np.random.choice([0, 1, 2, 3], num_samples),
        "device_conn_type": np.random.choice([0, 1, 2, 3], num_samples),
        "C1": np.random.randint(1, 10, num_samples),
        "C14": np.random.randint(1000, 5000, num_samples),
        "C15": np.random.randint(200, 600, num_samples),
        "C16": np.random.randint(200, 600, num_samples),
        "C17": np.random.randint(1000, 5000, num_samples),
        "C18": np.random.randint(0, 5, num_samples),
        "C19": np.random.randint(0, 50, num_samples),
        "C20": np.random.randint(-1, 100, num_samples),
        "C21": np.random.randint(0, 100, num_samples),
    }
    return pd.DataFrame(data)

# Generate data
data = generate_sample_data()

# Dataset Overview Section
st.subheader("📊 Dataset Overview")
st.write("Here is a preview of the dataset:")
st.dataframe(data.head())

# Dataset Statistics Section
st.subheader("📈 Dataset Statistics")
st.write(data.describe())

# Target Variable Distribution
st.subheader("🎯 Target Variable Distribution")
st.bar_chart(data["click"].value_counts())

# Feature Analysis Section
st.subheader("🔍 Feature Analysis")
feature = st.selectbox("Select a feature to analyze", options=data.columns)
if feature:
    st.write(f"Distribution of `{feature}`:")
    if data[feature].nunique() < 20:
        st.bar_chart(data[feature].value_counts())
    else:
        st.line_chart(data[feature].value_counts())

# Prediction Simulation Section
st.subheader("🤖 Simulate Prediction")
st.write("Enter values for the following features to simulate a CTR prediction:")

with st.sidebar:
    st.header("🔧 Input Features")
    user_input = {
        "hour": st.number_input("Hour of the day (0-23):", min_value=0, max_value=23, value=12),
        "banner_pos": st.selectbox("Banner position:", options=[0, 1, 2, 3, 4]),
        "device_type": st.selectbox("Device type:", options=[0, 1, 2, 3]),
        "device_conn_type": st.selectbox("Device connection type:", options=[0, 1, 2, 3]),
        "C1": st.number_input("C1 value:", min_value=1, max_value=10, value=5),
        "C14": st.number_input("C14 value:", min_value=1000, max_value=5000, value=2500),
        "C15": st.number_input("C15 value:", min_value=200, max_value=600, value=320),
        "C16": st.number_input("C16 value:", min_value=200, max_value=600, value=320),
        "C17": st.number_input("C17 value:", min_value=1000, max_value=5000, value=3000),
        "C18": st.selectbox("C18 value:", options=[0, 1, 2, 3, 4]),
        "C19": st.number_input("C19 value:", min_value=0, max_value=50, value=25),
        "C20": st.number_input("C20 value:", min_value=-1, max_value=100, value=10),
        "C21": st.number_input("C21 value:", min_value=0, max_value=100, value=50),
    }

# Display User Input
st.write("Your input values are:")
st.json(user_input)

# Display Prediction Result
st.subheader("💡 Prediction Result")
predicted_probability = round(np.random.uniform(0, 1), 2)
st.success(f"Based on your inputs, there is a **{predicted_probability * 100}%** chance of a click.")
