import streamlit as st

st.title("ATM Withdrawal Checker")


amount = st.number_input("Enter the amount you want to withdraw:", min_value=1, step=1)

if st.button("Check Withdrawal"):
    if amount % 10 == 0:
        st.success(f"Transaction Approved! You can withdraw ${amount}.")
    else:
        st.error("Transaction Denied. Please enter an amount that is a multiple of $10.")
