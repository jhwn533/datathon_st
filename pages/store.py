import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib.animation import FuncAnimation
import matplotlib.dates as mdates

st.title('Analyze by Store')
train = pd.read_parquet('data/train.parquet', engine = 'pyarrow')

store_nbr = st.selectbox("상점 번호를 선택하세요", options=sorted(train['store_nbr'].unique()))

if store_nbr:
    top5_sales = train[train['store_nbr'] == store_nbr].groupby('family')['sales'].sum().nlargest(5).reset_index()

    plt.figure(figsize=(10, 6))
    sns.barplot(x='family', y='sales', data=top5_sales, palette='viridis')
    plt.title(f'Store {store_nbr}: Top 5 selling product families')
    st.pyplot(plt)
    
# store_avg_sales(total)
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
