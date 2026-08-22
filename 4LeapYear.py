import streamlit as st

st.title("📅 Leap Year Checker" )

year = st.number_input("Enter Year :", min_value=1, step=1)
if st.button("Check"):
    if year % 400==0 or ( year % 4==0 and year % 100!=0 ):
        st.success(f"{year} is a Leap Year.")
    else:   
        st.error(f"{year} is not a Leap Year.")
