import streamlit as st
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

import plotly.figure_factory as ff
# import altair as alt
from sklearn import preprocessing 
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error

from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor

df = pd.read_csv('Data/rainfall.csv')

def show_data_frame():
    st.dataframe(df,use_container_width=True)
    # st.line_chart(df['Tmax'])

def show_heat_map():
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(), ax=ax)
    st.write(fig)

# def show_rainfall_chart():
#     st.line_chart(df['Rainfall'])

# def show_rainfall_chart_group():

#     x1 = df['Rainfall'].loc[[0,263]]
#     x2 = df['Rainfall'].loc[[263,527]]
#     x3 = df['Rainfall'].loc[[527,791]]
#     x4 = df['Rainfall'].loc[[791,1056]]
#     x5 = df['Rainfall'].loc[[1056,1319]]
#     x6 = df['Rainfall'].loc[[1319,1584]]
#     x7 = df['Rainfall'].loc[[1584,1847]]
#     x8 = df['Rainfall'].loc[[1847,2110]]
#     x9 = df['Rainfall'].loc[[2110,2373]]
#     x10 = df['Rainfall'].loc[[2110,2638]]

#     hist_data = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]

    
#     group_labels = ['Paro','Simkotha','Haa','Kanglung','Mongar',
#     'Chamkhar','Deothang','Punakha','Pemagatshel','Tashiyangtse']

#     fig = ff.create_distplot(
#         hist_data, group_labels, bin_size=[.1, .25, .5, .1, .25, .5, .1, .25, .5, .1])

#     st.plotly_chart(fig, use_container_width=True)

def rfa():

    st.write("###### Random Forest Accuracy")
    st.write("Train set accuracy: ", 0.9172)
    st.write("Test set accuracy : ", 0.7108)

    st.write("###### Decision Tree Accuracy")
    st.write("Train set accuracy: ", 0.7406)
    st.write("Test set accuracy : ", 0.6153)

    st.write("###### KNN Accuracy")
    st.write("Train set accuracy: ", 0.7174)
    st.write("Test set accuracy : ", 0.6734)

    st.write("###### SVM Accuracy")
    st.write("Train set accuracy: ", 0.6753)
    st.write("Test set accuracy : ", 0.7172)


    

    


