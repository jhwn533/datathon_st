import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

from datetime import datetime


APP_TITLE = 'Analyze by product'


def top_10_products(df):
    df["date"] = pd.to_datetime(df["date"])
    df['year'] = df['date'].dt.year
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    year_product_sales = df.groupby(["year", "family"])["sales"].sum().reset_index()
    year_product_sales = year_product_sales.sort_values(by=["year", "sales"], ascending=[True, False])
    
    for year in year_product_sales["year"].unique():
        top_products = year_product_sales[year_product_sales["year"] == year].head(10)
        ax.bar(top_products["family"], top_products["sales"], label=str(year))
    
    ax.set_xlabel("Family")
    ax.set_ylabel("Sales")
    ax.legend(title="Total Sales", loc="upper right", bbox_to_anchor=(1.2, 1))
    plt.xticks(rotation=45)
    
    st.pyplot(fig)    


def product_avg_sales(df):
    check = df.groupby('family').agg({"sales": "mean"}).reset_index()
    check.columns = ['family', 'sales']
    check = check.sort_values('sales')
    
    fig = px.bar(
        check,
        y='family',
        x="sales",
        color="sales",
        orientation='h',
        title='제품군별 평균매출액',
        height=800,
        width=800
    )
    
    # Display
    st.plotly_chart(fig)


def store_avg_sales(df):
    check=df.groupby('store_nbr').agg({"sales" : "mean"}).reset_index()

    check.columns = [
        'store_nbr', 
        'sales'
    ]
    check = check.sort_values('sales')

    fig = px.bar(
        check, 
        y='store_nbr', 
        x="sales", 
        color="sales",
        orientation='h', 
        title='상점별 평균매출액', 
        height=800, 
        width=800
    )
    st.plotly_chart(fig)


def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)


    # load data
    df = pd.read_parquet('data/merged_df.parquet')
    
    # top 10
    st.markdown('**매출 TOP 10 상품군**')
    top_10_products(df)

    # product average
    product_avg_sales(df)

    # store average
    store_avg_sales(df)

if __name__ == "__main__":
    main()
    
