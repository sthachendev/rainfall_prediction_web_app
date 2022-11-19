import streamlit as st
from predict_page import show_predict_page

st.set_page_config(
    page_title='Rainfall Prediction', 
    page_icon='Image/cloud-rain.png',  
    initial_sidebar_state = 'auto')

show_predict_page()