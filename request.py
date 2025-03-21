import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "Gender": 1,
    "Married": 1,
    "Dependents": 0,
    "Education": 0,
    "Self_Employed": 0,
    "ApplicantIncome": 5000,
    "CoapplicantIncome": 2000,
    "LoanAmount": 150,
    "Loan_Amount_Term": 360,
    "Credit_History": 1,
    "Property_Area": 2
}

response = requests.post(url, json=data)
print("Loan Status Prediction:", response.json())