import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

from datetime import datetime


APP_TITLE = 'Local Sales'

def total_sales(df, start_date, end_date):
    '''
    설정 날짜 내 매출 합산액
    '''
    # start_date = start_date.date()
    # end_date = end_date.date()
    
    df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
    total = df['sales'].sum()
    st.metric('Total sales', '$ {:,.0f}'.format(total))    
    
def total_transactions(df, start_date, end_date):
    '''
    설정 날짜 내 거래내역 수
    '''
    # start_date = start_date.date()
    # end_date = end_date.date()
    
    df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
    total = df['transactions'].sum()
    st.metric('Total transactions', '{:,.0f}'.format(total))    

def display_map(df, start_date, end_date):
    '''
    설정 기간 내 지역별 sales ratio
    '''
    df['state'] = df['state'].str.upper()
    
    df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
    df = df.groupby(['state'])[['sales', 'transactions']].sum().reset_index()
    df['sales_ratio'] = (df['sales']/df['transactions'])*100
    
    ec_geo = r'data/provs-ec.json'
    
    map = folium.Map(location=[-1.8312, -77.1834], zoom_start=7, scrollWheelZoom=False, tiles='cartodbpositron')
    
    Choropleth = folium.Choropleth(
        geo_data=ec_geo,
        data=df,
        columns=['state', 'sales_ratio'],
        key_on='feature.properties.nombre',
        fill_color='YlOrRd', 
        fill_opacity=0.7, 
        line_opacity=0.2,
        legend_name='Sales',
        highlight=True,
        reset=True,
    )

    Choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['nombre'], labels=False)
    )
    
    Choropleth.geojson.add_to(map)

    st_folium(map, width=900, height=600)
    
    
def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
    
    # date slider
    values = st.slider(
        '데이터 범위(날짜) 선택 🗓️',
        datetime(2013, 1, 1), datetime(2017, 8, 15),(datetime(2013, 1, 1),datetime(2017, 8, 15)), format="YYYY/MM/DD")
    
    start_date = values[0].date()
    end_date = values[1].date()


    # load data
    # df = pd.read_parquet('data/train.parquet')
    # df_store = pd.read_csv('data/stores.csv')
    # df_merge = pd.merge(df, df_store, on='store_nbr', how='left')
    # df_ts =pd.read_parquet('data/transactions.parquet')
    df = pd.read_parquet('data/merged_df.parquet')

    # Facts
    col1, col2 = st.columns(2)

    with col1:
        total_sales(df, start_date, end_date)

    with col2:
        total_transactions(df, start_date, end_date)

    st.write('sales_ratio')
    display_map(df, start_date, end_date)

    
if __name__ == "__main__":
    main()
    
