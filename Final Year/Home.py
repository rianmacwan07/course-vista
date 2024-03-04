import streamlit as st
from streamlit.connections import SQLConnection
import webbrowser 
from pages import sign_up

st.set_page_config(
        page_title= "multipage app",
        initial_sidebar_state="expanded",
        layout="wide",
        menu_items={
        'Get Help': 'https://www.rianmacwan04@gmail.com/help'
        }
    )

st.title("HOME")
st.markdown("-----")
st.subheader("VENTURE IS NOT AN OPTION WHEN YOU KNOW YOU ARE SELECTING THE RIGHT PATH")
st.markdown("---")
st.subheader("Over **30+** courses available at university")
st.write("Get Started now")
st.button("GET STARTED")

title_alignment= """
<style>
#GET STARTED {
  text-align: right
}
</style>
"""
st.markdown(title_alignment, unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: black;'>Invest in your professional goals</h2>", unsafe_allow_html=True)

col1, col2, col3, col4= st.columns(4)
original = "images.png"
col1.image(original, use_column_width=True)
col1.subheader("Learn anything")
col1.write('''Explore any interest or trending topic, take prerequisites, and advance your skills''')

originals = "images(2).JPG"
col2.image(originals, use_column_width=True)
col2.subheader("Flexible learning")
col2.write("Learn at your own pace, move between multiple courses, or switch to a different course")

original_s = "1604739.png"
col3.image(original_s, use_column_width=True)
col3.subheader("Career Options")
col3.write("Many more paths will be opened to you according to your interest")

original_s1 = "downloa.png"
col4.image(original_s1, use_column_width=True)
col4.subheader("Time Consuming")
col4.write("You can select the period in which you want to learn, with multiple programs")
st.markdown("---")
st.subheader("Enroll now in any particular group of courses -")

col_1,col_2=st.columns(2)
with col_1:
    button1=st.button('SPECIALIZATION')
    if button1:
        webbrowser.open('http://localhost:8501/courses')

with col_2:
    button2=st.button('ADDITIONAL')
    if button2:
        webbrowser.open('http://localhost:8501/courses')

st.text("")
st.write("Look some of the famous courses available")
st.text("")
