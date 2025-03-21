import joblib  # Import joblib to load the model
import pandas as pd
from flask import Flask, request, jsonify

# ✅ Load the trained model at the beginning of the script
model = joblib.load("loan_approval_model.pkl")

# Initialize Flask app
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Loan Prediction API is running!"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Convert JSON data to DataFrame
        input_data = pd.DataFrame([data])

        # Make prediction
        prediction = model.predict(input_data)

        # Interpret the result
        result = "Approved" if prediction[0] == 1 else "Rejected"
        
        return jsonify({"loan_status": result})

    except Exception as e:
        return jsonify({"error": str(e)})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)