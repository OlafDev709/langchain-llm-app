import langchain_helper as lch
import streamlit as st

st.title("Pet Name Generator")
user_animal_type = st.sidebar.selectbox("Select Animal Type", ["dog", "cat", "cow", "bird"])

if user_animal_type == "dog":
    st.sidebar.image("https://example.com/dog_image.jpg", caption="Dog Image")
    pet_color = st.sidebar.text_area(label="Enter Dog Color", value="brown")

if user_animal_type == "cat":
    st.sidebar.image("https://example.com/cat_image.jpg", caption="Cat Image")
    pet_color = st.sidebar.text_area(label="Enter Cat Color", value="white")

if user_animal_type == "cow":
    st.sidebar.image("https://example.com/cow_image.jpg", caption="Cow Image")
    pet_color = st.sidebar.text_area(label="Enter Cow Color", value="black")

if pet_color:
    response = lch.generate_pet_name(user_animal_type, pet_color)
    st.text(response['pet_name'])
