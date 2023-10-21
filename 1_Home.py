import streamlit as st
import utils

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.title('Small Daily Actions, Big Change: Unleash the Power of Time and Money Tracking.')

        st.caption('Harnessing the power of Artificial Intelligence, we provide you with valuable '
                'insights into your spending habits and time allocation, empowering you to make '
                'informed decisions and prioritize your resources wisely.')
        st.link_button('Try now', url='www.googl.com')
    
    with col2:
        mini_col1, mini_col2, mini_col3 = st.columns(3)
        with mini_col1:
            st.write('')
        with mini_col2:
            st.image('https://www.svgrepo.com/show/418517/analytics-chart-growth.svg', width=300)
        with mini_col3:
            st.write('')
        