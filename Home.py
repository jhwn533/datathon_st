import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

import urllib.request
from datetime import datetime


APP_TITLE = 'N-Sub'

def main():
    st.set_page_config(APP_TITLE + ' 🐠🐟🐡')
    st.title(APP_TITLE)

    col1, col2 = st.columns(2)

    with col1:
        st.image("https://www.corporacionfavorita.com/wp-content/uploads/2022/07/logo-cf-70.png")

    with col2:
        st.header("ecuador market slaes analysis")
        st.write("likelion Datathon")
        
if __name__ == "__main__":
    main()
    
