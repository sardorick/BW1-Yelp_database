import streamlit as st
from streamlit_option_menu import option_menu

# Load data





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
