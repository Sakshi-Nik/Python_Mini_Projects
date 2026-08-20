import streamlit as st

st.title("Even Odd Number Checker")
num =st.number_input("Enter a number:", step=1)

if st.button("Check"):
    if num %2==0:
        st.success(f"{num} is even")
    else:
        st.success(f"{num} is odd")
