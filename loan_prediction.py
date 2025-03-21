import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load Dataset (Using Your Uploaded CSV File)
df = pd.read_csv(r"C:\Users\User\Desktop\Projects\train.csv")

# Drop 'Loan_ID' as it is not useful for prediction
if 'Loan_ID' in df.columns:
    df.drop(columns=['Loan_ID'], inplace=True)

# Check for missing values
df.dropna(inplace=True)

# Encoding categorical variables
le = LabelEncoder()
categorical_columns = ['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area', 'Loan_Status']

for col in categorical_columns:
    if col in df.columns:
        df[col] = le.fit_transform(df[col].astype(str))

# Convert 'Dependents' column to numeric (handling special cases)
if 'Dependents' in df.columns:
    df['Dependents'] = df['Dependents'].replace({'3+': 3})
    df['Dependents'] = pd.to_numeric(df['Dependents'], errors='coerce')

# Fill missing numerical values with the median **(Fixed the error here!)**
df.fillna(df.select_dtypes(include=[np.number]).median(), inplace=True)

# Feature Selection
X = df.drop(columns=['Loan_Status'], errors='ignore')
y = df['Loan_Status']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Model Evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")
print(classification_report(y_test, y_pred))

# Save the Model
import joblib
joblib.dump(model, r"C:\Users\User\Desktop\Projects\loan_approval_model.pkl")

print("Model trained and saved successfully!")