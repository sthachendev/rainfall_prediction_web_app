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
        st.write("Train set accuracy: ", 0.9413)
        st.write("Test set accuracy : ", 0.6941)
        st.write('MSE', 0.2874)
        st.write('RMSE', 0.5361)
    
    with col2:

        st.write("###### Decision Tree Accuracy")
        st.write("Train set accuracy: ", 0.7235)
        st.write("Test set accuracy : ", 0.6497)
        st.write('MSE', 0.3291)
        st.write('RMSE', 0.5736)

    st.write('')

    col1, col2 = st.columns(2)

    with col1:

        st.write("###### KNN Accuracy")
        st.write("Train set accuracy: ", 0.7290)
        st.write("Test set accuracy : ", 0.7134)
        st.write('MSE', 0.2691)
        st.write('RMSE', 0.5189)

    with col2:

        st.write("###### SVM Accuracy")
        st.write("Train set accuracy: ", 0.9099)
        st.write("Test set accuracy : ", 0.4120)
        st.write('MSE', 0.5452)
        st.write('RMSE', 0.7383)


    

    


