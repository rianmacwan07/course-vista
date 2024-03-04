import streamlit as st
import mysql.connector
import hashlib
import webbrowser


def create_user(first_name, last_name, email, mobile_number, password, confirm_password):
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shelby@1256",
        database="sign_up"
    )

    cursor = db_connection.cursor()


    if password != confirm_password:
        st.warning("Passwords do not match. Please try again.")
        return

    
    query = f"SELECT COUNT(*) FROM sign_up WHERE email = '{email}'"
    cursor.execute(query)
    result = cursor.fetchone()[0]
    if result > 0:
        st.warning("Email already exists. Please use a different email.")
        return

    
    query = f"INSERT INTO sign_up (first_name, last_name, email, mobile_number, password, confirm_password) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (first_name, last_name, email, mobile_number, hashed_password, hashed_password)
    try:
        cursor.execute(query, values)
        db_connection.commit()
        st.success("Account created successfully!")
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
    finally:
        cursor.close()
        db_connection.close()

def main():
    st.title("Sign Up")

    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    email = st.text_input("Email (Gmail)")
    mobile_number = st.text_input("Mobile Number")
    password = st.text_input("Password", type="password", key=2)
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):
        create_user(first_name, last_name, email, mobile_number, password, password)
        webbrowser.open('http://localhost:8501/')

if __name__ == "__main__":
    main()
