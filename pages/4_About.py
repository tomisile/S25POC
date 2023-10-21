import streamlit as st

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

st.markdown("<h1 style='text-align: center;'>Your Smart Accountability Companion</h1>", unsafe_allow_html=True)
st.divider()
st.header('')

st.markdown("<p style='text-align: center;'>Discover how small daily actions can lead to profound changes \
            in your financial health and the way you use your most precious resource – time.</p>",
            unsafe_allow_html=True)

st.header('')
with st.container():
    abcol1, abcol2 = st.columns(2, gap="large")
    with abcol1:
        st.markdown("<h4 style='text-align: center;'>What You'll Do</h4>", unsafe_allow_html=True)
        st.divider()
        st.markdown("<p style='text-align: center;'>- Commit to daily logging of your expenses and how you use your time</p>", unsafe_allow_html=True)
    
    with abcol2:
        st.markdown("<h4 style='text-align: center;'>What We'll Provide</h4>", unsafe_allow_html=True)
        st.divider()
        st.markdown("<p style='text-align: center;'>- Dynamic dashboard showing activities or expenses over a specified period of time</p>", unsafe_allow_html=True)
