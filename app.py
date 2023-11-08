import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv(
    'C:/Users/jemeo/TripleTen/Projects/sprint4-project/sprint4-project/vehicles.csv')  # lendo os dados

st.header('Data Viewer')

hist_button = st.button('Criar histograma')  # criar um botão

if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
