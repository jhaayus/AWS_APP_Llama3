# pip install requests
# pip install langchain
# pip install streamlit


import streamlit as st

# Set the title of the webpage
st.title("Simple Webpage with Input and Output")

# Input field for user to enter something
user_input = st.text_input("Enter something:")

# Display the output when the user enters something
if user_input:
    st.write(f"You entered: {user_input}")
