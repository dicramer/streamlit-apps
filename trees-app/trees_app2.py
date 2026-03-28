import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from bokeh.plotting import figure
from streamlit_bokeh import streamlit_bokeh 
import seaborn as sns
import altair as alt
import datetime as dt
import pydeck as pdk

st.title("SF Trees")
st.write(
    """This app analyzes trees in San Francisco using
    a dataset kindly provided by SF DPW"""
)
st.subheader("Plotly Chart")
trees_df = pd.read_csv("trees.csv")
fig = px.histogram(trees_df["dbh"])
st.plotly_chart(fig)

trees_df["age"] = (pd.to_datetime("today") - pd.to_datetime(trees_df["date"])).dt.days
st.subheader("Seaborn Chart")
fig_sb, ax_sb = plt.subplots()
ax_sb = sns.histplot(trees_df["age"])
plt.xlabel("Age Days")
st.pyplot(fig_sb)
st.subheader("Matplotlib Chart")
fig_mpl, ax_mpl = plt.subplots()
ax_mpl = plt.hist(trees_df["age"])
plt.xlabel("Age Days")
st.pyplot(fig_mpl)

st.subheader("Bokeh Chart")
scatterplot = figure(title = "Bokeh Scatterplot of SF Trees")
scatterplot.scatter(trees_df["dbh"], trees_df["site_order"])
scatterplot.yaxis.axis_label = "site_order"
scatterplot.xaxis.axis_label = "dbh"
streamlit_bokeh(scatterplot, use_container_width=True, key="plot1")

st.subheader("Altair Chart")
df_caretaker = trees_df.groupby(["caretaker"]).count()["tree_id"].reset_index()
df_caretaker.columns = ["caretaker", "tree_count"]
fig = alt.Chart(df_caretaker).mark_bar().encode(x="caretaker", y="tree_count")
st.altair_chart(fig)

st.subheader("PyDeck & Mapbox")
sf_initial_view = pdk.ViewState(
     latitude=37.77,
     longitude=-122.4,
     zoom=11
     )
sp_layer = pdk.Layer(
     'ScatterplotLayer',
     data = trees_df,
     get_position = ['longitude', 'latitude'],
     get_radius=30)
st.pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state=sf_initial_view,
     layers = [sp_layer]
     ))

st.subheader("PyDeck & Mapbox 3D Hexagons")
trees_df.dropna(how="any", inplace=True)
sf_initial_view = pdk.ViewState(
     latitude=37.77,
     longitude=-122.4,
     zoom=11,
     pitch=30
     )
hx_layer = pdk.Layer(
     'HexagonLayer',
     data = trees_df,
     get_position = ['longitude', 'latitude'],
     radius=100,
     extruded=True)
st.pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state=sf_initial_view,
     layers = [hx_layer]
     ))