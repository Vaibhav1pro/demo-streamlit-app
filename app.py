import streamlit as st
from login import login, logout

st.set_page_config(page_title="AI SaaS App", page_icon="🚀")

# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# If not logged in → show login page
if not st.session_state["authenticated"]:
    login()

else:
    st.title("🚀 Welcome to Your AI SaaS App")
    st.write(f"Hello, {st.session_state['username']} 👋")

    st.success("You are logged in successfully!")

    if st.button("Logout"):
        logout()
        st.rerun()
