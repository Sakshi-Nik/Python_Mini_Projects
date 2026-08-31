import streamlit as st

st.title("🔢 Multiplication Table Generator")

num = st.number_input("Enter a number:", min_value=1, step=1)

if st.button("Generate Table"):
    if num:
        st.write(f"Multiplication Table for {num}:")
        for i in range(1, 11):
            st.write(f"{num} x {i} = {num * i}")