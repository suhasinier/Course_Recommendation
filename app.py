import pickle
import streamlit as st
import numpy as np


st.header("Book Recommender System Using Machine Learning")
model = pickle.load(open('artifacts\model.pkl','rb'))
course_name = pickle.load(open('artifacts\course_name.pkl','rb'))
final_rating = pickle.load(open('artifacts/final_rating.pkl','rb'))
courses_pivot = pickle.load(open('artifacts/courses_pivot.pkl','rb'))

selected_courses = st.selectbox(
    "Type or select a course from the dropdown",
    course_name
)