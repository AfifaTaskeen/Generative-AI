from google import genai
import streamlit as st

api_key = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=api_key)

st.title("AI Leave Letter Generator")

with st.form("leave_form"):

    name = st.text_input("Enter your name")
    student_id = st.text_input("Enter student ID")
    course = st.text_input("Enter course")
    email = st.text_input("Enter email")
    teacher = st.text_input("Enter teacher name")
    start_date = st.text_input("Leave start date")
    end_date = st.text_input("Leave end date")
    reason = st.text_area("Reason for leave")

    submit = st.form_submit_button("Generate Leave Letter")


if submit:

    prompt = f"""
Write a detailed formal leave letter using the information below.

Student Name: {name}
Student ID: {student_id}
Course: {course}
Email: {email}
Teacher Name: {teacher}
Leave Start Date: {start_date}
Leave End Date: {end_date}
Reason: {reason}

Rules:
- Do NOT use square brackets
- Do NOT add placeholders
- Use only the provided information
- Write a proper formal letter
- Detailed letter 

Format:

Subject: Leave Application

Dear {teacher},

I hope you are doing well. I am writing to respectfully request leave from {start_date} to {end_date} due to {reason}. During this period I will not be able to attend my classes.

I will ensure that I review all missed lectures and complete any assignments once I return.

Thank you for your understanding.

Sincerely,

{name}

Student ID: {student_id}
Course: {course}
Email: {email}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    st.subheader("Generated Leave Letter")
    st.text(response.text)