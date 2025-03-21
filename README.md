"Loan Prediction API"
A "Flask-based Loan Prediction API" that uses "Machine Learning" to determine whether a loan will be "Approved" or "Rejected" based on user details.

🔹 How It Works
1️⃣ The "user provides loan details" (Income, Credit Score, Property Type, etc.).  
2️⃣ The API uses a "trained RandomForestClassifier model" to predict "Approval or Rejection".  
3️⃣ The response is returned in "JSON format".  

---

🔹 Installation & Setup
 1. Clone the Repository
```bash
git clone https://github.com/chandanrangaraju/loan-prediction-api.git
cd loan-prediction-api
```

 2. Install Dependencies
```bash
pip install -r requirements.txt
```

 3. Run the Flask API
```bash
python app.py
```
📌 API will be available at: `http://127.0.0.1:5000/` 

---

🔹 Example API Request & Response
 ---POST Request (Using Python)
```python
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
print(response.json())
```

**Expected Response**
```json
{"loan_status": "Approved"}
```

---

🔹 Project Structure
 -- loan-prediction-api 
 `app.py` → Flask API  
 `loan_approval_model.pkl` → Machine Learning model  
 `request.py` → API testing script  
 `train.csv` → Dataset  
 `README.md` → Project documentation  

---

🔹 Future Improvements 
- Deploy API Online (Render/Heroku)  
- Build a Web UI for User Input 
- Improve Model Accuracy with Hyperparameter Tuning

---

🔹 Author
👤 Chandanrangaraju 
🔗 GitHub: [loan-prediction-api](https://github.com/chandanrangaraju/loan-prediction-api)  

🔥 If you like this project, don't forget to star ⭐ the repository!

---
