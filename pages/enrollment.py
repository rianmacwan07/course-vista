import streamlit as st
import mysql.connector


def insert_enrollment_data(first_name, last_name, father_name, mobile, father_mobile, email_address, department,department_spec,department_aditi, month, course_duration, age, gender, education_level, comment):
    try:
     
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Shelby@1256",
            database="Enrollment"
        )
        cursor = db_connection.cursor()

        insert_query = """
        INSERT INTO enrollments (first_name, last_name, father_name, mobile, father_mobile, email_address, department,department_spec,department_aditi, month, course_duration, age, gender, education_level, comment)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s ,%s, %s, %s, %s, %s, %s)
        """
        data = (first_name, last_name, father_name, mobile, father_mobile, email_address, department,department_spec,department_aditi,month, course_duration, age, gender, education_level, comment)
        cursor.execute(insert_query, data)
        
        db_connection.commit()
        cursor.close()
        db_connection.close()
        
        return True
    except mysql.connector.Error as e:
        st.error(f"Error inserting data into the database: {e}")
        return False


def enrollment_form(course:str):
    st.header("Enrollment Form")
    
    First_name = st.text_input("ENTER YOUR FIRST NAME")
    Last_name = st.text_input("ENTER YOUR LAST NAME")
    Father_name = st.text_input("ENTER YOUR PARENTS/GUARDIAN NAME")
    Mobile = st.text_input("ENTER MOBILE NUMBER")
    Father_mobile = st.text_input("ENTER YOUR PARENTS/GUARDIAN MOBILE NUMBER")
    email_address = st.text_input("ENTER YOUR EMAIL ADDRESS")
    department = st.selectbox("SELECT DEPARTMENT:",[
        "Mechanical Engineering", 
        "Electrical Engineering", 
        "Computer Science", 
        "Civil Engineering", 
        "Chemical Engineering"
        ])
    department_spec = st.selectbox("SELECT DEPARTMENT - SPECIALIZATION:",[
        "None",
        "Thermal Engineering",
        "Mechatronics and Robotics",
        "Automotive Engineering",
        "Aerospace Engineering",
        "Manufacturing Engineering",
        "Materials Engineering",
        "Mechanical Design Engineering",
        "Energy Engineering",
        "Biomechanical Engineering",
        "Nuclear Engineering",
        "Marine Engineering",
        "Environmental Engineering",
        "Renewable Energy Engineering"
        ])
    
    department_aditi = st.selectbox("SELECT DEPARTMENT - ADDITIONAL:",[
        'None',
        "Artificial Intelligence",
        "Automotive Engineering",
        "Engineering Ethics",
        "Engineering Economics",
        "Technical Writing",
        "Engineering Management",
        "Project Management",
        "Entrepreneurship",
        "Environmental Sustainability",
        "Renewable Energy Systems",
        "Cybersecurity for Engineers",
        "Data Science and Analytics",
        "Advanced Materials",
        "Robotics",
        "Nanotechnology",
        ])
    month = st.selectbox("Which month are you willing to start your course", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    course_duration = st.slider("Select Course Duration (in weeks)", min_value=1, max_value=12, value=4)
    age = st.number_input("Enter Your Age", min_value=1, max_value=100, value=18)
    gender = st.radio("Select Your Gender", ["Male", "Female", "Other"])
    education_level = st.selectbox("Select Your Background", ["ST", "SC", "OBC", "GENERAL"])
    comment = st.text_input("Any request you want to add")
    
    submit_button = st.button("Enroll in Course")
    if submit_button:
        if insert_enrollment_data(First_name, Last_name, Father_name, Mobile, Father_mobile, email_address, department,department_spec,department_aditi, month, course_duration, age, gender, education_level, comment):
            st.success("Enrollment Successful!")
            st.write(f"First name: {First_name}")
            st.write(f"Last name: {Last_name}")
            st.write(f"Parents/Guardian name: {Father_name}")
            st.write(f"Mobile number: {Mobile}")
            st.write(f"Parents/Guardian: {Father_mobile}")
            st.write(f"E-Mail: {email_address}")
            st.write(f"Department: {department}")
            st.write(f"Month you are willing to start the course: {month}")
            st.write(f"Course Duration: {course_duration} weeks")
            st.write(f"Age: {age} years")
            st.write(f"Gender: {gender}")
            st.write(f"Background: {education_level}")
            st.write(f"Comment: {comment}")
        else:
            st.error("Failed to enroll. Please try again.")
enrollment_form('Mechanical Engineering')

