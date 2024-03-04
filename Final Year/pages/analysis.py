import streamlit as st
import mysql.connector
import matplotlib.pyplot as plt
from collections import Counter
def fetch_data(col_name:str):
    try:
      
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Shelby@1256",
            database="Enrollment"
        )
        cursor = db_connection.cursor()

       
        cursor.execute(f"SELECT {col_name} FROM enrollments")
        data = cursor.fetchall()
        
        cursor.close()
        db_connection.close()

        return data
    except mysql.connector.Error as e:
        st.error(f"Error fetching data from the database: {e}")
        return None

def pie_chart(data):
    if data:
        if len(data) > 0:  
            departments = [row[0] for row in data]

           
            department_count = {}
            for department in departments:
                department_count[department] = department_count.get(department, 0) + 1

            if department_count:
              
                fig, ax = plt.subplots()
                ax.pie(department_count.values(), labels=department_count.keys(), autopct='%1.1f%%', startangle=90)
                ax.axis('equal')  

              
                st.pyplot(fig)
            else:
                st.write("No data available.")
        else:
            st.write("No departments found in the database.")
    else:
        st.write("Failed to fetch data from the database.")

def bar_chart(data):

    dep_counts = Counter([row[0] for row in data])
    dep = list(dep_counts.keys())
    dep_counts_val = list(dep_counts.values())
    if data:
        if len(data) > 0: 
         
            fig, ax = plt.subplots()
            ax.bar(dep, dep_counts_val)

            ax.set_xlabel('Department')
            ax.set_ylabel('Count')
            ax.set_title('Enrollments by Department')

            plt.xticks(rotation=45, ha='right')
            st.pyplot(fig)
        else:
            st.write("No data available.")
    else:
        st.write("Failed to fetch data from the database.")

def main():
    analyse = st.sidebar.selectbox('Courses',['Main','Specialization Course','Additional Course'])
    st.title("Most widely used Course")
    if analyse == "Main":
        data = fetch_data('department')
        pie_chart(data)
        bar_chart(data)

    elif analyse == "Specialization Course":
        data = fetch_data('department_spec')
        pie_chart(data)
        # bar_chart(data)
    elif analyse == 'Additional Course':
        data = fetch_data('department_aditi')
        pie_chart(data)
        # bar_chart(data)
    
    
main()