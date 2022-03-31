from matplotlib.pyplot import xlabel
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd
import numpy as np
import plotly.express as px
# Load data

resto_df = pd.read_csv(r"C:\Users\Lenovo\OneDrive\Documents\Strive repos\BW1-Yelp_database\Resto_df_cleaned.csv")
pub_df = pd.read_csv(r"C:\Users\Lenovo\OneDrive\Documents\Strive repos\BW1-Yelp_database\pub_df_cleaned3.csv")


# menu
with st.sidebar:
    menu = option_menu(None, ['Home', 'Restaurant', 'Hotels', 'Pubs', 
    'Business comparison', 'Recommendation'], icons =['house', 'shop', 'building', 'cup-straw', 'graph-up-arrow', 'info-circle '] )

# house, people, building, cup-straw, graph-up-arrow, geo-alt, info-circle

if menu == 'Home':
    st.title('Market Analysis for Barcelona hospitality industry using Yelp database')

    image_1 = Image.open("daniel-corneschi-N6HTCyN50p0-unsplash.jpg")
    image_2 = Image.open("dimitry-anikin-ECkAbFv_Nnc-unsplash.jpg")
    image_3 = Image.open("florian-wehde-WBGjg0DsO_g-unsplash.jpg")
    st.image(image_1)
    st.markdown(" Barcelona is located in an autonomous region of Spain - Catalonia, and it is one of the biggest cities of Spain and Europe.")
    st.markdown("""Catalonia and Barcelona has become one of the first tourist destination of Spain, it has everything to please the majority of visitors: with a history among the oldest in Europe, a capital, Barcelona, which never sleeps and an inland full of charm not to forget beautiful beaches in La Costa Brava.
    """)
    st.markdown("The city has been the center of entertainment for many years and is crowded with tourists from all around the globe all year round. ")
    st.image(image_2)
    st.markdown("As the city is one of the most important cities in Spain, it plays vital role in the tourism industry of the country.")
    st.markdown("""Tourism is one of the cornerstones of the Spanish economy and an outstanding driver of economic and social development. 
    In 2017 it accounted for 11.8% of GDP and in 2018 sustained 13.5% of employment (or 2.6 million direct jobs). 
    Tourism continues to contribute substantially to offsetting the country's trade deficit with tourism receipts amounting to EUR 62.5 billion, in 2018 – a growth of 3.6% compared with 2017. 
    In 2018, tourist arrivals reached 82.8 million (+1.1% compared to 2017), generating EUR 89.8 billion in international receipts (+3.3% compared to 2017). 
    Travel exports represented  52.3% of total service exports in 2018.""")
    st.markdown("""According to [Statista](https://www.statista.com/statistics/406660/popular-tourist-attractions-spain/), the most visited tourist attraction in Spain is La Sagrada Familia which is located in Barcelona.""")
    st.image(image_3)
    st.markdown("For this project, our team has conducted a market analysis for entertainment industry of Barcelona to help our investors choose the best business type to start in the city.")
    st.markdown("The analysis was conducted using Yelp database and includes data for hotels, restaurants and pubs in Barcelona. We have compared these three business and their success rate. ")
    st.markdown("We will present the data and will make a recommendation of the business type that we believe will succeed in Barcelona and support it with our findings. ")
    st.markdown("Team members: _Theophile Ishimwe, Sardorbek Zokirov_")

elif menu == 'Restaurant':
    sidebar_select = st.sidebar.radio('Plots', ['Neighborhood', 'Price range', 'Category'])
    if sidebar_select == 'Neighborhood':
        fig=px.bar(resto_df['Neighbourhood'].value_counts(ascending=True), orientation='h', template='ggplot2', height=600, width=800, labels={
            "value": "Number of restaurants per neighbourhood",
            "index": "Neighbourhoods"
        }, 
        title='In which neighbourhood most restaurants are located?')
        st.write(fig)

    elif sidebar_select == 'Price range':
        fig = px.bar(resto_df['Price range'].value_counts(ascending=True), orientation='h', template='ggplot2', height=600, width=800, labels={
            "value": "Number of Restaurants with respective price range",
            "index": "Price range (in euros)"
        },
        title='Price range of restaurants in Barcelona')
        st.write(fig)
    
    elif sidebar_select == 'Category':
        fig = px.bar(resto_df['Category'].value_counts(ascending=True).nlargest(20), orientation='h', template='ggplot2', height=600, width=800, labels={
            "value": "Number of Restaurants per category",
            "index": "Categories"
        },
        title='Most popular categories of restaurants')
        st.write(fig)

# Pubs sidemenu and plots
 
elif menu == 'Pubs':
    sidebar_select = st.sidebar.radio('Plots', ['Neighborhood', 'Price range', 'Category'])
    if sidebar_select == 'Neighborhood':
        fig=px.bar(pub_df['neighbourhood'].value_counts(ascending=True), orientation='h', template='ggplot2', height=600, width=800, labels={
            "value": "Number of pubs per neighbourhood",
            "index": "Neighbourhoods"
        }, 
        title='In which neighbourhood most pubs are located?')
        st.write(fig)

    elif sidebar_select == 'Price range':
        fig = px.bar(pub_df['price_range'].value_counts(ascending=True), orientation='h', template='ggplot2', height=600, width=800, labels={
            "value": "Number of pubs with respective price range",
            "index": "Price range (in euros)"
        },
        title='Price range of pubs in Barcelona')
        st.write(fig)
    
    elif sidebar_select == 'Category':
        fig = px.bar(pub_df['category'].value_counts(ascending=True).nlargest(20), orientation='h', template='ggplot2', height=600, width=800, labels={
            "value": "Number of pubs per category",
            "index": "Categories"
        },
        title='Most popular categories of pubs')
        st.write(fig)