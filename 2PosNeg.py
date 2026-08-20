import streamlit as st

st.title(" Positive Negative Checker")
num = st.number_input("Enter Number :",step=1)

if st.button("Check"):
    if num>0:
        st.success(f"{num} is positive.")
        st.write("hdgfegf")
    else:
        st.success("zero")