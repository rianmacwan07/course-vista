import mysql.connector

# Function to fetch all users from the database
def get_all():
    # Replace these with your MySQL database credentials
    db_connection = mysql.connector.connect(
        host="DESKTOP-JL8HNJK",
        user="root@localhost",
        password="Shelby@1256",
        database="sign_up"
    )

    cursor = db_connection.cursor()

    # Replace "users" with your table name
    query = "SELECT * FROM sign_up"
    cursor.execute(query)

    users = cursor.fetchall()

    cursor.close()
    db_connection.close()

    return users

# Display all users
def display_users(users):
    for user in users:
        print(f"first_name: {user[0]},last_name: {user[1]},email: {user[2]},mobile_number: {user[3]},password:{user[4]},confirm_password: {user[5]}, Password: {user[6]}")  # Adjust column indices based on your schema

# Fetch and display users
users = get_all()

if users:
    print("All Users:")
    display_users(users)
else:
    print("No users found.")