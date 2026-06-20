import streamlit as st

st.set_page_config(page_title="RecoveryShield AI")

st.title("🛡️ RecoveryShield AI")
st.subheader("Suspicious Account Recovery Detection")

new_device = st.selectbox("New Device?", ["no", "yes"])
unusual_location = st.selectbox("Unusual Location?", ["no", "yes"])
failed_attempts = st.selectbox("Multiple Failed Attempts?", ["no", "yes"])
password_change = st.selectbox("Recent Password Change?", ["no", "yes"])

score = 0

if new_device == "yes":
    score += 25

if unusual_location == "yes":
    score += 25

if failed_attempts == "yes":
    score += 30

if password_change == "yes":
    score += 20

st.metric("Risk Score", score)

if score >= 60:
    st.error("High Risk")
elif score >= 30:
    st.warning("Medium Risk")
else:
    st.success("Low Risk")