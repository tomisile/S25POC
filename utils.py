'''Utility functions for loading, preprocessing and visualizing data'''

import streamlit as st
import pandas as pd
import re


@st.cache_data
def load_data(link, sheet_name):
    '''Fetch data from a google spreadsheet url'''
    
    # Extract the sheet id after '/d/'
    pattern = r"/d/([a-zA-Z0-9-]+)"
    match = re.search(pattern, link)

    # Check if a match was found
    if match:
        sheet_id = match.group(1)
    else:
        st.error("Your data could not be found. \n Please verify your spreadsheet link.")
    
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    
    # Fetch data
    try:
        data = pd.read_csv(url)
        st.success("Your data was fetched successfully")
    except:
        st.error("Your sheet name may be incorrect.")
    
    return data


def new_func():
    '''  '''
    return
