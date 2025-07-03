import langchain_helper as lch
import streamlit as st

st.title("Pet Name Generator")
animal_type = st.sidebar.selectbox("Select Animal Type", ["dog", "cat", "cow", "bird"])

if animal_type == "dog":
    st.sidebar.image("https://example.com/dog_image.jpg", caption="Dog Image")
    pet_color = st.sidebar.text_area(label="Enter Dog Color", value="brown")

if animal_type == "cat":
    st.sidebar.image("https://example.com/cat_image.jpg", caption="Cat Image")
    pet_color = st.sidebar.text_area(label="Enter Cat Color", value="white")

if animal_type == "cow":
    st.sidebar.image("https://example.com/cow_image.jpg", caption="Cow Image")
    pet_color = st.sidebar.text_area(label="Enter Cow Color", value="black")