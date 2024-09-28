import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("Teste do Mapa - Folium")

# Criando o mapa
m = folium.Map(location=[-7.119012285515138, -34.82788601966975], zoom_start=15)
folium.Marker([-7.119012285515138, -34.82788601966975], tooltip="Hotel Village").add_to(m)

# Exibindo o mapa
st_folium(m, width=800, height=400)
