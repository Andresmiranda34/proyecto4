import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv(
    "C:\\Users\\petox\\workspace\\vs-edit\\proyecto4\\vehicles_us.csv"
)

st.header("Datos de anuncios de venta de coches")  # Encabezado

hist_button = st.button("Construir histograma")  # boton hist


if hist_button:  # funcionalidad del boton hist
    st.write(
        "Creación de un histograma para el conjunto de datos de anuncios de venta de coches"
    )

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)


scatter_button = st.button("Construir grafico de dispersión")  # boton scatter


if scatter_button:  # funcionalidad del boton scatter
    st.write(
        "Creacion de un grafico de dispersión para el conjunto de datos de anuncios de venta de coches"
    )

    fig2 = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(fig2, use_container_width=True)
