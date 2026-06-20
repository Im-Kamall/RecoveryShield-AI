import streamlit as st
import sys
import os

sys.path.append(os.path.abspath("."))

from ml_model.predict import predict_risk
st.set_page_config(page_title="RecoveryShield AI", page_icon="🛡️")

st.title("🛡️ RecoveryShield AI")
st.subheader("AI-Powered Suspicious Account Recovery Detection")

st.write("This dashboard uses a trained machine learning model to predict account recovery risk.")

user_id = st.text_input("User ID", "user123")

new_device = st.selectbox("New Device?", ["no", "yes"])
unusual_location = st.selectbox("Unusual Location?", ["no", "yes"])
failed_attempts = st.selectbox("Multiple Failed Attempts?", ["no", "yes"])
password_change = st.selectbox("Recent Password Change?", ["no", "yes"])

if st.button("Predict Risk"):
    risk = predict_risk(
        new_device,
        unusual_location,
        failed_attempts,
        password_change
    )

    st.metric("Predicted Risk Level", risk)

    if risk == "High":
        st.error("High Risk: Manual review or biometric verification required.")
    elif risk == "Medium":
        st.warning("Medium Risk: OTP or additional verification required.")
    else:
        st.success("Low Risk: Recovery can be approved.")