import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters 

    if use_digits:
        characters += string.digits  

    if use_special:
        characters += string.punctuation 


    return "".join(random.choice(characters) for _ in range(length))


st.title("🔐 Simple Password Generator")  


st.write(
    "Welcome to the Simple Password Generator! Use the options below to create a secure password."
)

length = st.slider(
    "Select password length:",
    min_value=6,
    max_value=32,
    value=12,
    help="Choose the length of your password.",
)


use_digits = st.checkbox("Include numbers", value=True, help="Include digits in the password.")
use_special = st.checkbox(
    "Include special characters", value=True, help="Include special characters in the password."
)

if st.button("Generate Password", help="Click to generate your password."):
    password = generate_password(length, use_digits, use_special)
    st.success("Password generated successfully!")  # Show a success message
    st.code(password, language="plaintext") 

st.markdown(
    """
    ---
    **Made with ❤️ by Khawaja Abdul Moiz**
    """,
    unsafe_allow_html=True,
)