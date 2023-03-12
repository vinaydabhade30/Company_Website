import streamlit as st
import pandas as pd
from mail_sender import email_sender_app


st.title("Contact Us")
topic_list = pd.read_csv("topics.csv")
with st.form(key='sub_form'):
    user_name = st.text_input("your Name")
    user_email = st.text_input("Your Email address")
    # user_topic = st.selectbox(['a','b','c'])
    option = st.selectbox(
        'What topic do you want to discuss?',
        (topic_list['topic']))

    # st.write('You selected:', option)
    raw_massage = st.text_area("Massage")
    massage_info = f"""\
Subject: Hi mail from Best company on {option}\n
    From: {user_name} email address: {user_email}\n
    {raw_massage} 

"""
    button_sub = st.form_submit_button("Submit")
    if button_sub:
        email_sender_app(massage_info)
        st.info("Your email was sent successfully, Thank you we will contact you!")
