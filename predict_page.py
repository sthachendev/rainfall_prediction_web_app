import streamlit as st
import pickle
import numpy as np
from streamlit_option_menu import option_menu
from explore_page import show_data_frame, show_heat_map, show_rainfall_chart, show_rainfall_chart_group
# from PIL import Image

def show_predict_page():

    # with st.sidebar:
    
    selected = option_menu(
            menu_title = '',
            options=['Home','Predict','Explore','Team'],
            icons=['house','book','meta','people'] ,
            menu_icon='cast',
            default_index=0,
            orientation='horizontal',          
        )
    
    if selected == 'Home':
        home()
    if selected == 'Predict':
        predict_page()
    if selected == 'Explore':
        explore()
    if selected == 'Team':
        team()

def home():
    st.title('Rainfall Prediction')
    st.write("##### Accuracy of rainfall forecasting has great importance for countries like Bhutan whose economy is largely dependent on hydro-power project and agriculture. ")
    st.write('Rainfall')
    show_rainfall_chart()
    show_rainfall_chart_group()

def predict_page():
    st.title('Enter the features to predict')

    model = pickle.load(open('Model/model.pkl', 'rb'))

    location_array = ['Paro','Simkotha','Haa','Kanglung','Mongar',
    'Chamkhar','Deothang','Punakha','Pemagatshel','Tashiyangtse']

    location_array_encoded = [5, 6, 7, 9, 0, 1, 2, 3, 4, 8]

    location_input = st.selectbox('Location', location_array)

    for i in location_array:
        if location_input == i:
            location_data = location_array_encoded[location_array.index(i)]
            #st.write(location_data)

    year_array = []
    year_start= 2000
    year_end = 2100

    for i in range(year_start, year_end):
        year_array.append(i)

    year = st.selectbox('Year',year_array)

    month_array = ['JAN','FEB','MAR','APR','MAY',
    'JUN','JUL','AUG','SEP','OCT','NOV','DEC']

    month_input = st.selectbox('Month', month_array)

    for i in month_array:
        if month_input == i:
            month_data = month_array.index(i)+1
            #st.write(month_data)

    maxT = st.number_input('Max Temperature (c)')
    minT = st.number_input('Min Temperature')
    rh = st.number_input('RH')
    ws = st.number_input('WS')

    predict = st.button('Predict')
    
    if predict:
        input_data = (location_data, year, month_data, maxT, minT, rh, ws)
        input_data_as_numpy_array = np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        result = model.predict(input_data_reshaped)

        if (result>0):
            st.write('Rainfall', result[0].round(2),'ml')
        else:
            st.write('No rainfall', result[0].round(2))

def explore():
    st.title('Data Exploration & Data Visualization')
    st.write('Dataset')
    show_data_frame()
    st.write('Heatmap')
    show_heat_map()

def team():
    st.title('Team Members')
    # image = Image.open('./image/user.jpg')
    
    # st.image(image)
    st.write('Sherab Tharchen Dorji')
    st.write('Ugyen Tenzin')
    st.write('Tshewang Dema')
    st.write('Sonam Tobden')

