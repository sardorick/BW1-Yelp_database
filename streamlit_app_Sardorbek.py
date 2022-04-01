from matplotlib.pyplot import xlabel
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd
import numpy as np
import plotly.express as px
# Load data

# resto_df = pd.read_csv(r"C:\Users\Lenovo\OneDrive\Documents\Strive repos\BW1-Yelp_database\Resto_df_cleaned.csv")
# pub_df = pd.read_csv(r"C:\Users\Lenovo\OneDrive\Documents\Strive repos\BW1-Yelp_database\pub_df_cleaned3.csv")
# hotel_df = pd.read_csv(r"C:\Users\Lenovo\OneDrive\Documents\Strive repos\BW1-Yelp_database\hotel_df_cleaned.csv")

resto_df = pd.read_csv("Resto_df_cleaned.csv")
pub_df = pd.read_csv("pub_df_cleaned3.csv")
hotel_df = pd.read_csv("hotel_df_cleaned2.csv")



# Menu
with st.sidebar:
    menu = option_menu(None, ['Home','Hotels', 'Restaurant', 'Pubs', 'Recommendation'], 
    icons =['house', 'building','shop', 'cup-straw', 'graph-up-arrow', 'info-circle '] )


# Home page
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




# Restaurant
elif menu == 'Restaurant':
    resto = pd.read_csv('theo/resto_dataset.csv')


    sidebar_select = st.sidebar.radio('GRAPH', ['Distribution reviews rating', 'Neighborhood', 'Price range', 'Category', 'Location'])



    if sidebar_select == 'Neighborhood':
        fig=px.bar(x = resto_df['Neighbourhood'].value_counts(ascending=True).values, y = resto_df['Neighbourhood'].value_counts(ascending=True).index, orientation='h', template='ggplot2', height=600, width=800, labels={
            "x": "Number of restaurants per neighbourhood",
            "y": "Neighbourhoods"
        }, 
        title='In which neighbourhood most restaurants are located?',)
        st.write(fig)

    elif sidebar_select == 'Price range':
        fig = px.bar(x = resto_df['Price range'].value_counts(ascending=True).values, y = resto_df['Price range'].value_counts(ascending=True).index, orientation='h', template='ggplot2', height=600, width=800, labels={
            "x": "Number of Restaurants with respective price range",
            "y": "Price range (in euros)"
        },
        title='Price range of restaurants in Barcelona')
        st.write(fig)
    
    elif sidebar_select == 'Category':
        fig = px.bar(x = resto_df['Category'].value_counts(ascending=True).nlargest(20).values, y = resto_df['Category'].value_counts(ascending=True).nlargest(20).index, orientation='h', template='ggplot2', height=600, width=800, labels={
            "x": "Number of Restaurants per category",
            "y": "Categories"
        },
        title='Most popular categories of restaurants')
        st.write(fig)
    elif sidebar_select == 'Distribution reviews rating':
        fig = px.box(data_frame=resto_df, x = 'Rating', y = 'Review count', template='ggplot2', height=600, width=800, title='Distribution of the number of reviews and rating')

        st.plotly_chart(fig)


    elif sidebar_select == 'Location':
        resto = resto[resto.reviews.notnull()]
        px.set_mapbox_access_token(open("theo/.mapbox_token").read())
        fig = px.scatter_mapbox(resto, lat="Latitude", lon="Longitude",zoom=12, size = 'reviews', color='rating', 
        width=900, height=600, opacity=0.5, template="plotly_dark",
        hover_name='name',
        hover_data={'Latitude':False, 'Longitude': False, 'price_range': True},
        title= 'Location of restaurants with respect to rating and number of reviews')
        st.plotly_chart(fig)





# Pubs
 
elif menu == 'Pubs':
    pub = pd.read_csv('theo/pub_dataset.csv')


    sidebar_select = st.sidebar.radio('Graphs', ['Neighborhood', 'Price range', 'Category', 'Distribution reviews rating', 'Location'])


    if sidebar_select == 'Neighborhood':
        fig=px.bar(x = pub_df['neighbourhood'].value_counts(ascending=True).values, y = pub_df['neighbourhood'].value_counts(ascending=True).index, orientation='h', template='ggplot2', height=600, width=800, labels={
            "x": "Number of pubs per neighbourhood",
            "y": "Neighbourhoods"
        }, 
        title='In which neighbourhood most pubs are located?')
        st.write(fig)

    elif sidebar_select == 'Price range':
        fig = px.bar(x = pub_df['price_range'].value_counts(ascending=True).values, y = pub_df['price_range'].value_counts(ascending=True).index, orientation='h', template='ggplot2', height=600, width=800, labels={
            "x": "Number of pubs with respective price range",
            "y": "Price range (in euros)"
        },
        title='Price range of pubs in Barcelona')
        st.write(fig)
    
    elif sidebar_select == 'Category':
        fig = px.bar(x = pub_df['category'].value_counts(ascending=True).nlargest(20).values, y = pub_df['category'].value_counts(ascending=True).nlargest(20).index, orientation='h', template='ggplot2', height=600, width=800, labels={
            "x": "Number of pubs per category",
            "y": "Categories"
        },
        title='Most popular categories of pubs')
        st.write(fig)
    elif sidebar_select == 'Distribution reviews rating':
        fig = px.box(data_frame=pub_df, x = 'rating', y = 'reviews', template='ggplot2', height=600, width=800, title='Distribution of the number of reviews and rating')

        st.plotly_chart(fig)


    elif sidebar_select == 'Location':
        pub = pub[pub.reviews.notnull()]
        px.set_mapbox_access_token(open("theo/.mapbox_token").read())
        fig = px.scatter_mapbox(pub, lat="Latitude", lon="Longitude",zoom=12, size = 'reviews', color='rating', 
        width=900, height=600, opacity=0.5, template="plotly_dark",
        hover_name='name',
        hover_data={'Latitude':False, 'Longitude': False, 'price_range': True},
        title= 'Location of pubs with respect to rating and number of reviews')
        st.plotly_chart(fig)





# Hotels
elif menu == 'Hotels':
    hotel = pd.read_csv('theo/hotel_dataset.csv')

    sidebar_select = st.sidebar.radio('Graphs', ['Distribution reviews rating', 'Neighborhood', 'Price range','Median reviews relative to price', 'Location'])
    
    
    if sidebar_select == 'Neighborhood':
        fig=px.bar(y = hotel_df['neighbourhood'].value_counts(ascending=True).index, 
        x = hotel_df['neighbourhood'].value_counts(ascending=True).values, template='ggplot2', height=600, width=800, labels={
            "x": "Number of hotels per neighbourhood",
            "y": "Neighbourhoods"
        }, 
        title='In which neighbourhood most hotels are located?')
        st.write(fig)

    elif sidebar_select == 'Price range':
        fig = px.bar(y = hotel_df['price_range'].value_counts(ascending=True).index, 
        x = hotel_df['price_range'].value_counts(ascending=True).values, template='ggplot2', height=600, width=800, labels={
                "x": "Number of hotels with respective price range",
                "y": "Price range (in euros)"
        },
        title='Price range of hotels in Barcelona')
        st.write(fig)


    elif sidebar_select == 'Location':
        hotel = hotel[hotel.reviews.notnull()]
        px.set_mapbox_access_token(open("theo/.mapbox_token").read())
        fig = px.scatter_mapbox(hotel, lat="Latitude", lon="Longitude",zoom=12, size = 'reviews', color='rating', 
        width=900, height=600, opacity=0.5, template="plotly_dark",
        hover_name='name',
        hover_data={'Latitude':False, 'Longitude': False, 'price_range': True},
        title= 'Location of hotels with respect to rating and number of reviews')
        st.plotly_chart(fig)


    elif sidebar_select == 'Distribution reviews rating':
        fig = px.box(data_frame=hotel, x = 'rating', y = 'reviews', template='ggplot2', height=600, width=800, title='Distribution of the number of reviews and rating')

        st.plotly_chart(fig)

    elif sidebar_select == 'Median reviews relative to price':
        fig = px.bar(x = hotel.groupby('price_range')['reviews'].agg('median').sort_values().values, 
        y = hotel.groupby('price_range')['reviews'].agg('median').sort_values().index,
        template='ggplot2', height=600, width=800, 
        labels={
                "x": "Average (median) number of reviews",
                "y": "Price range (in euros)"
        },
        title='Average rating with respect to price range per person')
        

        st.plotly_chart(fig)
