📊 Customer Churn Prediction - Telecom Dataset

📝 Overview

This project focuses on predicting customer churn for a telecom company using supervised machine learning. The goal is to identify customers who are likely to discontinue their services, allowing the business to take preemptive actions. This prediction is critical for customer retention and cost-saving strategies.

🔍 Problem Statement

Customer churn poses a major challenge for telecom companies. A small portion of customers (about 25%) represent the churn cases, while the remaining majority do not churn, leading to a heavily imbalanced dataset. The main problem lies in achieving a high recall for the minority class (churn = 1) without sacrificing overall accuracy.

💡 Solution

This project addresses the imbalance and model performance through the following steps:

Exploratory Data Analysis (EDA)

Identified skewed distributions and missing values

Visualized churn trends across tenure, contract types, and payment methods

Data Preprocessing

Converted string columns to numeric using Label Encoding

Handled missing values in TotalCharges

Feature scaling (where necessary)

Balancing the Dataset

Used SMOTE (Synthetic Minority Over-sampling Technique) to balance class distribution

Applied Stratified Train-Test Split to ensure both classes are represented equally in training and testing

Model Building

Started with a Decision Tree (moderate performance, lower recall)

Switched to Random Forest Classifier with class_weight='balanced'

Hyperparameter tuning via GridSearchCV

Final model achieved:

Accuracy: ~77.5%

Recall for Churn (Class 1): ~56%

Model Deployment

Created a Streamlit Web App

User inputs customer attributes through UI

Model predicts churn probability in real time

🛠 Technologies Used

Python

Pandas, NumPy, Scikit-learn

Imbalanced-learn (SMOTE)

Streamlit (for deployment)

Joblib (for model saving/loading)

🚀 Key Learnings

Tackling data imbalance is critical in churn prediction.

Accuracy is misleading when the dataset is biased — recall is more important for minority class.

Real-world datasets require a lot of preprocessing and patience (e.g., encoding errors, missing values).

📁 How to Run

Clone the repository

Install dependencies: pip install -r requirements.txt

Run: streamlit run app.py

📈 Future Improvements

Use XGBoost or LightGBM for better performance

Add pipeline for automatic encoding and scaling

Integrate with live telecom dashboard or CRM

