def calculate_risk_score(data):
    score = 0

    if data.get("new_device") == "yes":
        score += 25

    if data.get("unusual_location") == "yes":
        score += 25

    if data.get("multiple_failed_attempts") == "yes":
        score += 30

    if data.get("recent_password_change") == "yes":
        score += 20

    if score >= 60:
        return score, "High Risk"
    elif score >= 30:
        return score, "Medium Risk"
    else:
        return score, "Low Risk"