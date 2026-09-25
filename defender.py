import streamlit as st
with st.sidebar:
    st.text_input(label='Main app URL', value='http://localhost:30001')
    st.text_input(label='Main api URL', value='http://api.localhost:30001')
    about = st.text_input(
        "love with father",
        placeholder="Your Work!"
    )



st.title("📝 Shared note board")
st.caption("Anyone with room code can read and post notes here. Share the code with classmate")
st.button("🔃Refresh")
st.button("Leave board")
# Correctly formatted HTML with inline CSS
color_code = "#74e7a4bb"
st.success("Room Code:31f910bbecea75c54e8b")  

tab_new, tab_existing = st.tabs(["New Work", "But Work Is Work"])

st.write(f"Your name is ALI NAWAZ and your hoby is love with animal and your favroit color is green")
st.markdown(
    f"""
    <div style="background-color: {color_code}; padding: 20px;">
     <h3 style="color:#333;">And here's a Green one to round it out!</h3>
        <p>-Devos.</p>
    </div>
    """,
    
    unsafe_allow_html=True
)
color_code = "#b0faff"
st.markdown(
    f"""
    <div style="background-color: {color_code}; padding: 20px;">
     <h3 style="color:#333;">Pair up and try the blue color option!</h3>
        <p>-Priyo.</p>
    </div>
    """,
    
    unsafe_allow_html=True
)
color_code = "#f8b0ff"
st.markdown(
    f"""
    <div style="background-color: {color_code}; padding: 20px;">
     <h3 style="color:#333;">This one's a pink note to test the colors!</h3>
        <p>-Sam.</p>
    </div>
    """,
    
    unsafe_allow_html=True
)
color_code = "#fff3b0"
st.markdown(
    f"""
    <div style="background-color: {color_code}; padding: 20px;">
     <h3 style="color:#333;">Room code is on the board_dont's lose it!</h3>
        <p>-Jordan.</p>
    </div>
    """,
    
    unsafe_allow_html=True
)
color_code = "#ffb0d1"
st.markdown(
    f"""
    <div style="background-color: {color_code}; padding: 20px;">
     <h3 style="color:#333;">Welcome to the week 07 npoint project!</h3>
        <p>-Mafia.</p>
    </div>
    """,
    
    unsafe_allow_html=True
)
