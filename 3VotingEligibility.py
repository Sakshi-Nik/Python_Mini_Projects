import streamlit as st

st.header("🗳️ Voting Eligibility Checker")
age = st.number_input("Enter age :",step=1)
if st.button("Check"):
    if age >= 18:
        st.success("Eligible for voting.")
    else:
        st.error("Not eligible for voting.")