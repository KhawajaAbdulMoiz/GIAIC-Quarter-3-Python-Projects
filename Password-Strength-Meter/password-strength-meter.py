import streamlit as st
import re

# Main Page Styling
st.markdown(
    """
    <style>
        body {
            background-color: #8EC5FC; 
            color: #ffff;
        }
        .stApp {
          background-color: #9a577f;
          background-image: linear-gradient(225deg, #9a577f 0%, #784BA0 50%, #2B86C5 100%);
        }
         .stButton button {
            font-size: 28px;
            font-weight: bold;
            color: white;
            background-color: #443158; 
        }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("🔐 Password Strength Meter")
st.write("Enter your password below to check its strength.")
# Function to check the strength of the password
def strength_check(password):
    score = 0
    suggestions = []
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("🔴 Password should be at least **8 characters long**.")
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("🔴 Password should contain **both uppercase and lowercase letters**.")
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("🔴 Password should contain **at least one number**.")
    if re.search(r"[\W_]", password): 
        score += 1
    else:
        suggestions.append("🔴 Password should contain **special characters (e.g., !@#$%^&*)**.")
    if score >= 4:
        st.success("✅ Your password is **strong**! 💪")
    elif score == 3:
        st.info("⚠️ Improvement Needed: Try adding **special characters, numbers, and a mix of alphabets**.")
    else:
        st.error("❌ Weak Password: Consider making it more secure.")
    if suggestions:
        with st.expander("🔎 How to Improve Your Password"):
            for suggestion in suggestions:
                st.write(suggestion)

password = st.text_input("Enter Your Password", type="password", help="Ensure your password is strong.")
if st.button("Check Strength"):
    if password:
        strength_check(password)
    else:
        st.warning("⚠️ Please enter your password first.")
