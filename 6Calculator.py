import streamlit as st

st.title("🧮 Simple Calculator")


n1 = st.number_input("First Number:", step=1, key="n1")
n2 = st.number_input("Second Number:", step=1, key="n2")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Add"):
        st.success(f"Result: {n1 + n2}")

with col2:
    if st.button("Subtract"):
        st.success(f"Result: {n1 - n2}")

with col3:
    if st.button("Multiply"):
        st.success(f"Result: {n1 * n2}")

with col4:
    if st.button("Divide"):
        if n2 != 0:
            st.success(f"Result: {n1 / n2}")
        else:
            st.error("Cannot divide by zero")
