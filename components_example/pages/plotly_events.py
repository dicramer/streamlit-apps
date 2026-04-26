import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Streamlit Plotly Events Example: Penguins")
df = pd.read_csv("penguins.csv")
df = df.dropna()

# Figure ganz normal erstellen
fig = px.scatter(df, x="bill_length_mm", y="bill_depth_mm", color="species")

# Nutze das eingebaute `on_select="rerun"` von Streamlit
event_dict = st.plotly_chart(fig, on_select="rerun")

# Zugreifen auf die Liste der ausgewählten Punkte im Dictionary
points = event_dict["selection"]["points"]

if len(points) == 0:
    st.stop()

# X- und Y-Wert des ersten ausgewählten Punktes abrufen
selected_x_value = points[0]["x"]
selected_y_value = points[0]["y"]

df_selected = df[
    (df["bill_length_mm"] == selected_x_value)
    & (df["bill_depth_mm"] == selected_y_value)
]

st.write("Data for selected point:")
st.write(df_selected)
