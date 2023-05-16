import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib.animation import FuncAnimation
import matplotlib.dates as mdates
import mplfinance as mpf
st.title('승민님도 store 분석이면 여기에 같이 붙일까요..?')
train = pd.read_parquet('data/train.parquet', engine = 'pyarrow')

store_nbr = st.selectbox("상점 번호를 선택하세요", options=sorted(train['store_nbr'].unique()))

if store_nbr:
    top5_sales = train[train['store_nbr'] == store_nbr].groupby('family')['sales'].sum().nlargest(5).reset_index()

    plt.figure(figsize=(10, 6))
    sns.barplot(x='family', y='sales', data=top5_sales, palette='viridis')
    plt.title(f'Store {store_nbr}: Top 5 selling product families')
    st.pyplot(plt)