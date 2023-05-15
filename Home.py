import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

import urllib.request
from datetime import datetime


APP_TITLE = '☢️ 핵잠수함 ☢️'

def main():
    st.set_page_config(APP_TITLE)
    st.image('WELCOME TO ECUADOR.png')
    st.header("ecuador market slaes analysis")
    
    col1, col2 = st.columns(2)

    with col1:
        st.image("https://www.corporacionfavorita.com/wp-content/uploads/2022/07/logo-cf-70.png")

    with col2:
        st.markdown("* 에콰도르 주식에 도전하려는 **개미투자자**\n* 현지를 잘 모르니 그나마 안정적인 대기업에 투자해보려고 찾아본 기업이 '_**Corporación Favorita**_'\n* 최근 기업실적을 살펴보고 투자 결정 예정\n(※분석시기는 2017년 말로 가정함)")
        
if __name__ == "__main__":
    main()
    
