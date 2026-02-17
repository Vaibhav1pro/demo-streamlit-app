import streamlit as st

# Dummy user database (for testing)
USER_DB = {
    "vaibhav": "1234",
    "admin": "admin123"
}

def login():
    st.subheader("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USER_DB and USER_DB[username] == password:
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.success("Login Successful 🎉")
        else:
            st.error("Invalid Username or Password")

def logout():
    st.session_state["authenticated"] = False
    st.session_state["username"] = ""
