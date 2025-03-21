import joblib

# Load the trained model
model = joblib.load("loan_approval_model.pkl")

# Print the expected feature names
print("Expected Feature Names:", model.feature_names_in_)