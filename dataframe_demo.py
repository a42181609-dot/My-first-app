import streamlit as st
import json
import pandas as pd
import dataframe_demo
st.title("love my father")
st.caption("Allah kher kray")
def load_data():
    # make the simple dataframe
    data = {
        'Name': ['Ali', 'Sara', 'Ahmed', 'Zara'],
        'Age': [25, 30, 22, 28],
        'City': ['Lahore', 'Karachi', 'Islamabad', 'Multan']
    }
    df = pd.DataFrame(data)

