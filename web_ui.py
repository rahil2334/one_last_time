import streamlit as st
from controller.ui_controller import UIController

controller = UIController()

st.title("Explainable AI Decision Support System")

user_input = st.text_area("Enter your project idea")

if st.button("Analyze"):
    if user_input.strip():
        response = controller.handle_input(user_input)

        st.subheader("Results")
        st.write("Confidence Score:", response["confidence_score"])
        st.write("Risk Level:", response["risk_level"])

        st.subheader("Explanation")
        st.write(response["explanation"])

        st.subheader("Suggestions")
        for s in response["suggestions"]:
            st.write("-", s)
    else:
        st.warning("Please enter an idea.")
