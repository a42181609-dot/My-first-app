import streamlit as st
st.title("✅ Synced Todo list")
st.write("Your list lives in an npoint document.save the sync code to pick it up again any where")
name=st.text_input("Sync Code")

    
import streamlit as st

with st.sidebar:
    st.header('server')
    st.text_input(label='Main app URL', value='http://localhost:3001')
    st.text_input(label='Main Api URL', value='http://api.localhost:3001')
tab_new, tab_existing = st.tabs(["start a new list", "open an existing list"])


    