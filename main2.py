import streamlit as st
import agent as agent
import textwrap

st.title("YouTube Video Query Assistant")

with st.sidebar:
    with st.form(key="video_form"):
        youtube_url = st.text_input(label="Enter YouTube Video URL", value="https://www.youtube.com/watch?v=lG7Uxts9SXs&ab_channel=freeCodeCamp.org", key="youtube_url_input")
        query = st.sidebar.text_area(label="Enter Your Query", value="What is the main topic of the video?", key="query_input")
        submit_button = st.form_submit_button("Load Video")

if query and youtube_url:
    db = agent.create_vector_db_from_youtube_url(youtube_url)
    response, docs = agent.get_response_from_query(db, query)
    st.subheader("Answer")
    st.text(textwrap.fill(response, width=80))