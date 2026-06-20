from fastapi import FastAPI
from pydantic import BaseModel
from backend.risk_engine import calculate_risk_score

app = FastAPI(title="RecoveryShield AI")

class RecoveryRequest(BaseModel):
    user_id: str
    new_device: str
    unusual_location: str
    multiple_failed_attempts: str
    recent_password_change: str

@app.get("/")
def home():
    return {"message": "RecoveryShield AI API is running"}

@app.post("/check-risk")
def check_risk(request: RecoveryRequest):
    data = request.dict()
    score, risk_level = calculate_risk_score(data)

    return {
        "user_id": request.user_id,
        "risk_score": score,
        "risk_level": risk_level,
        "recommendation": "Allow recovery" if risk_level == "Low Risk" else "Require extra verification"
    }