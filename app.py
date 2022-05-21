# -*- coding: utf-8 -*-
"""
Created on Mon May 16 21:21:08 2022

@author: PC-KARIM
"""
import plotly.express as px
# import openpyxl
import pandas as pd

import streamlit as st # pip intsall streamlit

# emojis: https//www.webfx.com/tools/emoji-cheat-sheet/

st.set_page_config(page_title='Sales Dashbord',
                   page_icon=':bare_chart:',
                   layout="wide")
st.header('store data 2022')
st.subheader('tutorial')

@st.cache
def get_data_from_excel():
  df=pd.read_excel('store.xls')
  #print(df.head())

# ADD THE year col
  df['Year']=pd.to_datetime(df['Order_Date'],format="%D%M%Y").dt.year

  return df

df=get_data_from_excel()


# ------SIDERBAR --------
st.sidebar.header('Please Filter Here:')

Province=st.sidebar.multiselect(
    " Select the Province:",
    options=df['Province'].unique(),
    default=df['Province'].unique()

)

st.sidebar.header('Please Filter Here:')

Customer_Segment=st.sidebar.multiselect(
    " Select the Customer Segment:",
    options=df['Customer_Segment'].unique(),
    default=df['Customer_Segment'].unique()

)

st.sidebar.header('Please Filter Here:')

Product_Category=st.sidebar.multiselect(
    " Select the Product Category:",
    options=df['Product_Category'].unique(),
    default=df['Product_Category'].unique()

)
df_selection = df.query(

    "Province==@Province & Customer_Segment==@Customer_Segment & Product_Category==@Product_Category "
)

st.dataframe(df_selection)

# ------- MainPage-------
st.title(":bar_chart:Sales Dashboard")
st.markdown("##")

# ---------- TOP KPI'S-------------
Total_Sales=int(df['Sales'].sum())
avreage_Profit=round(df['Profit'].mean(),1)
# star_rating=":star:" * int(round(avreage_Profit,0))
average_sale_by_transaction=round(df_selection['Sales'].mean(),2)
left_column,middle_column,right_column=st.columns(3)

with left_column:
    st.subheader('Total Sales')
    st.subheader(f"US ${Total_Sales}")

with middle_column:
    st.subheader("Avreage Rating")
    st.subheader(f"{avreage_Profit}")

with right_column:
    st.subheader('Avreage Sale Per Transaction:')
    st.subheader(f"US ${average_sale_by_transaction}")

st.markdown('---')


# --------SALES BY PRODUCT CATEGORY----
sales_by_product_category=(
df_selection.groupby(by=['Product_Category']).sum()[['Sales']].sort_values(by='Sales')

)
fig_product_sales=px.bar(
    sales_by_product_category,
    x='Sales',
    y=sales_by_product_category.index,
    orientation='h',
    title='<b>Sales by Product Category</b>',
    color_discrete_sequence=['#0083B8'] * len(sales_by_product_category),
    template="plotly_white",
)
fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))

)


#st.plotly_chart(fig_product_sales)

# -------  SALES by YEAR----------
sales_by_year=df_selection.groupby(by=['Year'])[["Sales"]].sum()

fig_yearly_sales=px.bar(
    sales_by_year,
    x='Sales',
    y=sales_by_year.index,
    orientation='h',
    title='<b>Sales by Year</b>',
    color_discrete_sequence=['#0083B8'] * len(sales_by_year),
    template="plotly_white",
)
fig_yearly_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(tickmode='linear')),
    yaxis=(dict(showgrid=False))

)
#st.plotly_chart(fig_yearly_sales)

left_column,right_column=st.columns(2)
left_column.plotly_chart(fig_yearly_sales,use_container_width=True)
right_column.plotly_chart(fig_product_sales,use_container_width=True)


# -----WIDE stremlit style----
hide_st_style="""
<style>
# MainMenu{visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>

st.markdown(hide_st_style,unsafe_allow_html=True)


"""

print(pil)

