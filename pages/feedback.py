import streamlit as st

class Feedback:
    def __init__(self) -> None:
        Name = st.text_input('Enter Your Name:')
        Phone_No = st.number_input('Enter Your Mobile No:')
        Email = st.text_input("Enter Your Email:")
        FeedBack = st.text_area("Give us your Feedback:")
        submit_btn = st.button("Submit Response")
        self.name = Name
        self.phone_no = Phone_No
        self.email = Email
        self.feedback = FeedBack
        self.submit_btn = submit_btn
        if self.name is None and self.phone_no is None and self.email is None and self.email is None and self.feedback is None:
            st.warning('Field is empty')
            if self.submit_btn:
                st.success("Reposnse Submitted")


object = Feedback()