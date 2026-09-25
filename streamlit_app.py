import streamlit as st

st.title("✅ Synced Todo list")
st.write("Your list lives in an npoint document. Save the sync code to pick it up again anywhere.")
me = st.text_input("Sync Code")

with st.sidebar:
    st.header('server')
    st.text_input(label='Main app URL', value='https://my-first-app-hebza4pl2unseyllaftutk.streamlit.app')
    st.text_input(label='Main Api URL', value='https://my-first-app-hebza4pl2unseyllaftutk.streamlit.app')

tab_new, tab_existing = st.tabs(["start a new list", "open an existing list"])
st.button("big boos haq nawaz")


    