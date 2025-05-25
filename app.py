import streamlit as st
import joblib
import numpy as np 
import pandas as pd

# Load trained model
model = joblib.load('churn_model.pkl')# Input form

st.title("Customer Churn Prediction App")

gender = st.selectbox("Gender", ['Male', 'Female'])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Has Partner?", ['Yes', 'No'])
dependents = st.selectbox("Has Dependents?", ['Yes', 'No'])
tenure = st.slider("Tenure (months)", 0, 72, 12)
phone_service = st.selectbox("Phone Service", ['Yes', 'No'])
multiple_lines = st.selectbox("Multiple Lines", ['Yes', 'No'])
internet_service = st.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'])
online_security = st.selectbox("Online Security", ['Yes', 'No' ])
online_backup = st.selectbox("Online Backup", ['Yes', 'No'])
device_protection = st.selectbox("Device Protection", ['Yes', 'No'])
tech_support = st.selectbox("Tech Support", ['Yes', 'No'])
streaming_tv = st.selectbox("Streaming TV", ['Yes', 'No'])
streaming_movies = st.selectbox("Streaming Movies", ['Yes', 'No'])
contract = st.selectbox("Contract", ['Month-to-month', 'One year', 'Two year'])
paperless_billing = st.selectbox("Paperless Billing", ['Yes', 'No'])
payment_method = st.selectbox("Payment Method", [
    'Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'
])

monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
total_charges = st.number_input("Total Charges", 0.0, 10000.0, 1000.0)



# Convert inputs into dataframe
input_df = pd.DataFrame({
    'gender': [gender],
    'SeniorCitizen': [senior],
    'Partner': [partner],
    'Dependents': [dependents],
    'tenure': [tenure],
    'PhoneService': [phone_service],
    'MultipleLines': [multiple_lines],
    'InternetService': [internet_service],
    'OnlineSecurity': [online_security],
    'OnlineBackup': [online_backup],
    'DeviceProtection': [device_protection],
    'TechSupport': [tech_support],
    'StreamingTV': [streaming_tv],
    'StreamingMovies': [streaming_movies],
    'Contract': [contract],
    'PaperlessBilling': [paperless_billing],
    'PaymentMethod': [payment_method],
    'MonthlyCharges': [monthly_charges],
    'TotalCharges': [total_charges]
})

# Encoding
input_df['gender'] = input_df['gender'].map({'Male': 1, 'Female': 0})
input_df['Partner'] = input_df['Partner'].map({'Yes': 1, 'No': 0})
input_df['Dependents'] = input_df['Dependents'].map({'Yes': 1, 'No': 0})
input_df['PhoneService'] = input_df['PhoneService'].map({'Yes': 1, 'No': 0})
input_df['MultipleLines'] = input_df['MultipleLines'].map({'Yes': 1, 'No': 0})
input_df['InternetService'] = input_df['InternetService'].map({'DSL': 0, 'Fiber optic': 1, 'No': 2})
input_df['OnlineSecurity'] = input_df['OnlineSecurity'].map({'Yes': 1, 'No': 0})
input_df['OnlineBackup'] = input_df['OnlineBackup'].map({'Yes': 1, 'No': 0})
input_df['DeviceProtection'] = input_df['DeviceProtection'].map({'Yes': 1, 'No': 0})
input_df['TechSupport'] = input_df['TechSupport'].map({'Yes': 1, 'No': 0})
input_df['StreamingTV'] = input_df['StreamingTV'].map({'Yes': 1, 'No': 0})
input_df['StreamingMovies'] = input_df['StreamingMovies'].map({'Yes': 1, 'No': 0})
input_df['Contract'] = input_df['Contract'].map({'Month-to-month': 0, 'One year': 1, 'Two year': 2})
input_df['PaperlessBilling'] = input_df['PaperlessBilling'].map({'Yes': 1, 'No': 0})
input_df['PaymentMethod'] = input_df['PaymentMethod'].map({
    'Electronic check': 3,
    'Mailed check': 4,
    'Bank transfer (automatic)': 1,
    'Credit card (automatic)': 2
})

# Preprocess same as training (label encoding or one-hot if applied before)
# If you used a preprocessor, load and use that too

if st.button("Predict Churn"):
    prediction = model.predict(input_df)[0]
    if prediction == 1:
        st.error("⚠️ The customer is likely to churn.")
    else:
        st.success("✅ The customer is not likely to churn.")