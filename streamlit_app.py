from calendar import c
from sys import maxsize
import streamlit as st
from streamlit_option_menu import option_menu

import pandas as pd

import plotly.express as px




# menu
with st.sidebar:
    menu = option_menu(None, ['Home', 'Restaurant', 'Hotels', 'Pubs', 
    'Business comparison', 'Recommendation'], icons =['house', 'shop', 'building', 'cup-straw', 'graph-up-arrow', 'info-circle '] )

# house, people, building, cup-straw, graph-up-arrow, geo-alt, info-circle

if menu == 'Home':
    st.title('Which Business to run in Barcelona?')
    st.markdown(""" Home content here!!!  
    Photo of Barcelona in the background.
    Some text about the project and key facts about Barcelona  

    
    """)

elif menu == 'Restaurant':
    st.sidebar.radio('Plots', ['plot1', 'plot2'])


elif menu == 'Hotels':
    graph = st.sidebar.radio('Graph', ['Reviews/Rating distributions', 'Price range', 'Location'])

    # load data
    hotel = pd.read_csv('hotel_dataset.csv')

    if graph == 'Location':
        
        hotel = hotel[hotel.reviews.notnull()]

        px.set_mapbox_access_token(open(".mapbox_token").read())
        fig = px.scatter_mapbox(hotel, lat="Latitude", lon="Longitude",zoom=12, size = 'reviews', color='rating', 
        width=900, height=600, opacity=1, template="plotly_dark")
        st.plotly_chart(fig)
 
        # st.map(hotel[['lat', 'lon']])