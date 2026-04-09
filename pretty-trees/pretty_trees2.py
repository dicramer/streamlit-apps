import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')
st.title("SF Trees")
st.write(
    """
    This app analyses trees in San Francisco using
    a dataset kindly provided by SF DPW.
    """
)
trees_df = pd.read_csv("trees.csv")
today = pd.to_datetime('today')
trees_df['date'] = pd.to_datetime(trees_df['date'])
trees_df['age'] = (today - trees_df['date']).dt.days
unique_caretakers = trees_df['caretaker'].unique()
owners = st.sidebar.multiselect("Tree Owner Filter", unique_caretakers)
graph_color = st.sidebar.color_picker("Graph Colors")
if owners:
    trees_df = trees_df[trees_df['caretaker'].isin(owners)]
    df_dbh_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
    df_dbh_grouped.columns = ['tree_count']

col1, col2 = st.columns(2)
with col1:
    fig = px.histogram(
        trees_df,
        x=trees_df['dbh'],
        title="Tree Width",
        color_discrete_sequence=[graph_color]
    )
    st.plotly_chart(fig)
with col2:
    fig = px.histogram(
        trees_df,
        x=trees_df['age'],
        title="Tree Age",
        color_discrete_sequence=[graph_color]
    )
    st.plotly_chart(fig)

