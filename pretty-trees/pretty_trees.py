import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
st.title("SF Trees")
st.write(
    """
    This app analyses trees in San Francisco using
    a dataset kindly provided by SF DPW.
    """
)
trees_df = pd.read_csv("trees.csv")
df_dbh_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']
col1, col2, col3 = st.columns((1, 1, 1), gap='large')
with col1:
    st.line_chart(df_dbh_grouped)
with col2:
    st.bar_chart(df_dbh_grouped)
with col3:
    st.area_chart(df_dbh_grouped)

tab1, tab2, tab3 = st.tabs(["Line Chart", "Bar Chart", "Area Chart"])
with tab1:
    st.line_chart(df_dbh_grouped)
with tab2:
    st.bar_chart(df_dbh_grouped)
with tab3:
    st.area_chart(df_dbh_grouped)

owners = st.sidebar.multiselect("Tree Owner Filter", trees_df['caretaker'].unique())
if owners:
    trees_df = trees_df[trees_df['caretaker'].isin(owners)]
    df_dbh_grouped2 = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
    df_dbh_grouped2.columns = ["tree_count"]
    st.line_chart(df_dbh_grouped2)

trees_df = trees_df.dropna(subset=['longitude', 'latitude'])
trees_df = trees_df.sample(n = 1000, replace=True)
st.map(trees_df)
