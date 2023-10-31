import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv("vehicles_us.csv")
df = pd.DataFrame(car_data)  # creacion de un DataFrame con los datos de los autos


st.header("Datos de anuncios de venta de coches")  # Encabezado

st.dataframe(df)


hist_button = st.button("Construir histograma")  # boton hist

if hist_button:  # funcionalidad del boton hist
    st.write(
        "Creación de un histograma para el conjunto de datos de anuncios de venta de coches"
    )

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)


scatter_checkbox = st.checkbox("Construir grafico de dispersión")  # casilla scatter

if scatter_checkbox:  # funcionalidad de casilla scatter
    st.write(
        "Creacion de un grafico de dispersión para el conjunto de datos de anuncios de venta de coches"
    )

    fig2 = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(fig2, use_container_width=True)
