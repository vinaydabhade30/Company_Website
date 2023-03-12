import streamlit as st
import pandas as pd
st.set_page_config(layout='wide')


st.header("The Best Company")
content = """ We have a team of writers & designers, who are highly experienced and talented to work in diverse professionals.

All the team members are extremely trained and experienced with past exposure in the corporate world as distinguished professionals.
We have a set criterion that determines those who joins our team. It is upon fulfilling the stringent and rigorous tests and interview that one can become part of Our Team as Writer.
Our teams have confidence with handling any background irrespective of the complexity linked to such a task. We have a balanced team of professionals simplifying all projects that we handle.
Our Team is divided into each group, which leads by a highly qualified and seasoned Senior Content leader to ensure ample research, drafting, editing and proof-reading all the content before submission to our clients.
Our team maintains a subtle accessibility and working relationship which guarantee our clients full-time attention whenever they need our help
"""
st.write(content)
st.title("Our Team")
col1,empty_col1, col2,empty_col2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])
df = pd.read_csv("data.csv", sep=',')
with col1:
    for index, row in df[:4].iterrows():
        name = row['first name']+row['last name']
        st.subheader(name)
        st.write(row['role'])
        st.image('images/'+row['image'])
        st.write('                      ')
with col2:
    for index, row in df[4:8].iterrows():
        name = row['first name']+row['last name']
        st.subheader(name)
        st.write(row['role'])
        st.image('images/'+row['image'])
        st.write('                      ')
with col3:
    for index, row in df[8:].iterrows():
        name = row['first name']+row['last name']
        st.subheader(name)
        st.write(row['role'])
        st.image('images/'+row['image'])
        st.write('                      ')
