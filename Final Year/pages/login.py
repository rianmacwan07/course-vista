import streamlit as st
import mysql.connector
import hashlib
import secrets


def authenticate_user(email, password):
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shelby@1256",
        database="sign_up"
    )
    cursor = db_connection.cursor()

    query = f"SELECT email, password FROM sign_up WHERE email = '{email}'"
    cursor.execute(query)
    result = cursor.fetchone()
    
    if result:
        db_email, db_password = result
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if hashed_password == db_password:
            return db_email
    return None


def reset_password(email):
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shelby@1256",
        database="sign_up"
    )
    cursor = db_connection.cursor()

   
    token = secrets.token_hex(16)
    

    query = f"UPDATE sign_up SET reset_token = '{token}' WHERE email = '{email}'"
    cursor.execute(query)
    db_connection.commit()
    
   

    st.success("Password reset email sent. Check your inbox.")

st.title("Login Page")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    user = authenticate_user(email, password)
    if user:
        st.success("Logged in as: " + user)
    else:
        st.error("Invalid email or password")

if st.button("Forgot Password"):
    reset_email = st.text_input("Enter your email to reset password:")
    if st.button("Reset Password"):
        reset_password(reset_email)
