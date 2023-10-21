import streamlit as st
import utils

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

st.title("Session 25")
st.write("A smart time approach for optimizing your daily tasks and routines.")
st.caption("beta 0.1.0")

prompt1 = st.text_input('Enter Spreadsheet Link')
prompt2 = st.text_input('Enter Sheet Name')

if prompt1 and prompt2:
    data = utils.load_data(prompt1, prompt2)

    if st.toggle('View data'):
        st.write(data)
    
    st.divider()
    col1, col2, col3 = st.columns(3)
    col1.metric("Recorded Sessions", "87/234", "14")
    col2.metric("Time Tracked", "925 minutes", "-8%")
    col3.metric("Productivity Score", "66%", "4%")

    if st.button('More Insights'):
        st.info('Redirecting you to your analytics dashboard')

