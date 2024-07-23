import streamlit as st
st.set_page_config(page_title="My Webpage", page_icon="👨‍💻", layout="wide")
st.subheader("Hi, I am Kgaogelo")
st.title("Data Analyst and a software Developer")
st.write("I am passionate about finding ways to use python and VBA to be more efficient")
button1 = st.button("Email")
button2 = st.button("Message")
button3 = st.button("Submit")
if button1:
    # Text area for user feedback
    user_feedback = st.text_area("Provide your feedback", "Type your feedback here...")

    # Display the feedback if provided
    if user_feedback:
        st.write(f"Your feedback: {user_feedback}")
    else:
        st.write("Please enter your feedback above.")

    # You can add more components to your app below!

