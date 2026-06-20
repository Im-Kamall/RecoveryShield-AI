import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("data/risk_dataset.csv")

X = df.drop(["user_id", "risk_level"], axis=1)

X = X.replace({"yes": 1, "no": 0})

y = df["risk_level"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "ml_model/model.pkl")

print("Model trained successfully!")