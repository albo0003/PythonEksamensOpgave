import streamlit as st
import requests

@st.dialog("Login")
def login_popup():
    username = st.text_input("Username", key="login_user")
    password = st.text_input("Password", type="password", key="login_pass")

    if st.button("Login"):
        response = requests.get(
            "http://backend:8000/login",
            params={
                "username": username,
                "password": password
            })
        if(response.status_code == 401):
            st.error("wrong username or password")
        else:
            
            st.session_state["user"] = username
            st.success("Logged in!")
            st.rerun()

@st.dialog("Signup")
def signup_popup():
    username = st.text_input("Username", key="signup_user")
    password = st.text_input("Password", type="password", key="signup_pass")
    passwordAgain = st.text_input("Password again", type="password", key="signup_pass_again")

    if st.button("Signup"):
        if password == passwordAgain:

            response = requests.get(
            "http://backend:8000/signup",
            params={
                "username": username,
                "password": password
            })
            if(response.status_code == 401):
                st.error("user with that username already exists")
            else:
                st.session_state["user"] = username
                st.success("Logged in!")
                st.rerun()
        else:
            st.error("password and password again is not the same")


def require_login():
    if "user" not in st.session_state:
        st.session_state["user"] = None

    if st.session_state["user"] is None:
        st.warning("You must log in first")

        # IMPORTANT: direct call, not nested inside button logic
        if st.button("Login"):
            login_popup()
        if st.button("Signup"):
            signup_popup()

        st.stop()