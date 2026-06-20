import joblib
import pandas as pd

model = joblib.load("ml_model/model.pkl")

def predict_risk(new_device, unusual_location, multiple_failed_attempts, recent_password_change):
    input_data = pd.DataFrame([{
        "new_device": 1 if new_device == "yes" else 0,
        "unusual_location": 1 if unusual_location == "yes" else 0,
        "multiple_failed_attempts": 1 if multiple_failed_attempts == "yes" else 0,
        "recent_password_change": 1 if recent_password_change == "yes" else 0
    }])

    prediction = model.predict(input_data)[0]
    return prediction