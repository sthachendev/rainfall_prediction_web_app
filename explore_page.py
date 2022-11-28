import streamlit as st
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

import plotly.figure_factory as ff

df = pd.read_csv('Data/rainfall.csv')

def show_data_frame():
    st.dataframe(df,use_container_width=True)

# def show_heat_map():
    # fig, ax = plt.subplots()
    # sns.heatmap(df.corr(), ax=ax)
    # st.write(fig)

def rfa():

    col1, col2 = st.columns(2)

    with col1:

        st.write("###### Random Forest Accuracy")
        st.write("Train set accuracy: ", 0.9172)
        st.write("Test set accuracy : ", 0.7108)
    
    with col2:

        st.write("###### Decision Tree Accuracy")
        st.write("Train set accuracy: ", 0.7406)
        st.write("Test set accuracy : ", 0.6153)

    st.write('')

    col1, col2 = st.columns(2)

    with col1:

        st.write("###### KNN Accuracy")
        st.write("Train set accuracy: ", 0.7174)
        st.write("Test set accuracy : ", 0.6734)

    with col2:

        st.write("###### SVM Accuracy")
        st.write("Train set accuracy: ", 0.6753)
        st.write("Test set accuracy : ", 0.7172)


    

    


