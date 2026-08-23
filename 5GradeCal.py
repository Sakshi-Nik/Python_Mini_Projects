import streamlit as st

st.title("📅 Grade Calculator")
student_name = st.text_input("Enter Student Name:")
math_score = st.number_input("Enter Math Score:", min_value=0, max_value=100,step=1)
science_score = st.number_input("Enter Science Score:", min_value=0, max_value=100,step=1)
english_score = st.number_input("Enter English Score:", min_value=0, max_value=100,step=1)
history_score = st.number_input("Enter History Score:", min_value=0, max_value=100,step=1)

if st.button("Calculate Grade"):
    total_score = math_score + science_score + english_score + history_score
    average_score = total_score / 4

    if average_score >= 90:
        grade = "A"
    elif average_score >= 80:
        grade = "B"
    elif average_score >= 70:
        grade = "C"
    elif average_score >= 60:
        grade = "D"
    else:
        grade = "F"

    st.success(f"{student_name}'s Average Score: {average_score:.2f}, Grade: {grade}")