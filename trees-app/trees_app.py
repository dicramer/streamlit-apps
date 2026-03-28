import streamlit as st
import pandas as pd
import numpy as np

st.title("SF Trees")
st.write(
    """This app analyzes trees in San Francisco using
    a dataset kindly provided by SF DPW"""
)
trees_df = pd.read_csv("trees.csv")
df_dph_grouped = pd.DataFrame(trees_df.groupby(["dbh"]).count()["tree_id"])
df_dph_grouped.columns = ["tree_count"]
st.write(df_dph_grouped.head())
st.line_chart(df_dph_grouped)
st.bar_chart(df_dph_grouped)
st.area_chart(df_dph_grouped)
df_dph_grouped["new_col"] = np.random.randn(len(df_dph_grouped)) * 500
st.line_chart(df_dph_grouped)

# Index zurücksetzen und explizite Angabe der x/y Achse
df_dph_grouped_index = pd.DataFrame(trees_df.groupby(["dbh"]).count()["tree_id"]).reset_index()
df_dph_grouped_index.columns = ["dbh", "tree_count"]
st.write(df_dph_grouped_index.head())
st.line_chart(df_dph_grouped_index, x="dbh", y="tree_count")

# Map erzeugen
trees_df = trees_df.dropna(subset=["longitude", "latitude"])
trees_df = trees_df.sample(n=1000)
st.map(trees_df)
