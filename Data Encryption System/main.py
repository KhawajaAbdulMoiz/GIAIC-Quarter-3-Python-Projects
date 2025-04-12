import streamlit as st
import hashlib
from cryptography.fernet import Fernet
st.set_page_config(
    page_title="Secure Data Vault",
    page_icon="🔒",  
    layout="centered"
)
# Custom CSS
st.markdown("""
<style>
    .footer {
        font-size: 0.8rem;
        text-align: center;
        margin-top: 2rem;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)

# 🔐 Generate encryption key
if "KEY" not in st.session_state:
    st.session_state.KEY = Fernet.generate_key()
    st.session_state.cipher = Fernet(st.session_state.KEY)

cipher = st.session_state.cipher

# Initialize session state
if "stored_data" not in st.session_state:
    st.session_state.stored_data = {}

if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

# 🔐 Function to hash passkey
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# 🔏 Encrypt function
def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

# 🔓 Decrypt function
def decrypt_data(encrypted_text, passkey):
    hashed_passkey = hash_passkey(passkey)
    for key, value in st.session_state.stored_data.items():
        if value["encrypted_text"] == encrypted_text and value["passkey"] == hashed_passkey:
            st.session_state.failed_attempts = 0
            return cipher.decrypt(encrypted_text.encode()).decode()
    st.session_state.failed_attempts += 1
    return None

# App UI
st.title("🔒 Secure Data Vault")
st.caption("By Khawja Abdul Moiz")

menu = ["Home", "Store Data", "Retrieve Data", "Admin"]
choice = st.sidebar.selectbox("Menu", menu, help="Navigate through the application")

# 🏠 Home
if choice == "Home":
    st.subheader("Welcome to Secure Data Vault")
    st.write("""
    This application allows you to securely store and retrieve sensitive data using military-grade encryption.
    
    ### Features:
    - 🔐 AES-256 encryption
    - 🔑 Passkey protection
    - 💾 Secure data storage
    - 🔍 Safe data retrieval
    
    Get started by selecting an option from the sidebar.
    """)

# 💾 Store Data
elif choice == "Store Data":
    st.subheader("Store Encrypted Data")
    with st.form("store_form"):
        user_data = st.text_area("Data to encrypt:", height=150)
        passkey = st.text_input("Create a passkey:", type="password", help="Remember this passkey - you'll need it to decrypt")
        submitted = st.form_submit_button("Encrypt & Store")
        
        if submitted:
            if user_data and passkey:
                hashed_passkey = hash_passkey(passkey)
                encrypted_text = encrypt_data(user_data)
                st.session_state.stored_data[encrypted_text] = {
                    "encrypted_text": encrypted_text,
                    "passkey": hashed_passkey
                }
                st.success("Data encrypted and stored successfully!")
                st.subheader("Your Encrypted Data")
                st.code(encrypted_text, language="text")
                st.warning("⚠️ Copy and save this encrypted data along with your passkey")
            else:
                st.error("Please enter both data and passkey")

# 🔍 Retrieve Data
elif choice == "Retrieve Data":
    st.subheader("Retrieve Your Data")
    with st.form("retrieve_form"):
        encrypted_text = st.text_area("Paste encrypted data:", height=150)
        passkey = st.text_input("Enter your passkey:", type="password")
        submitted = st.form_submit_button("Decrypt")
        
        if submitted:
            if encrypted_text and passkey:
                result = decrypt_data(encrypted_text, passkey)
                if result:
                    st.success("Decryption successful!")
                    st.subheader("Your Decrypted Data")
                    st.code(result, language="text")
                else:
                    remaining = 3 - st.session_state.failed_attempts
                    st.error(f"Incorrect passkey! {remaining} attempts remaining")
                    if st.session_state.failed_attempts >= 3:
                        st.warning("Account locked. Please contact admin.")
            else:
                st.error("Please enter both encrypted data and passkey")

# 🔐 Admin
elif choice == "Admin":
    st.subheader("Admin Portal")
    login_pass = st.text_input("Enter admin password:", type="password")
    
    if st.button("Authenticate"):
        if login_pass == "admin123":
            st.session_state.failed_attempts = 0
            st.success("Admin access granted")
            st.write("Stored data entries:", len(st.session_state.stored_data))
        else:
            st.error("Invalid admin credentials")

# Footer
st.markdown("---")
st.markdown('<div class="footer">Developed by Khawja Abdul Moiz | Secure Data Vault v1.0</div>', unsafe_allow_html=True)