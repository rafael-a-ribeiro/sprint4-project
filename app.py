import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles.csv')  # lendo os dados

st.header('Data Viewer')
st.dataframe(car_data)

st.header('Vehicle Types by Manufacturer')
# Separando a informação de modelo e fabricante
car_data[['manufacturer', 'model']
         ] = car_data['model'].str.split(' ', 1, expand=True)
# Agrupando os dados por Fabricante
group_manufacturers = car_data.groupby(['manufacturer', 'type'])[
    'date_posted'].count()
group_manufacturers = group_manufacturers.reset_index()
# Trocando o nome da coluna para ficar de acordo com a informação guardada
group_manufacturers.rename(columns={'date_posted': 'count'}, inplace=True)
# Gerando o gráfico de barra
bar_chart = px.bar(group_manufacturers, x='manufacturer',
                   y='count', color='type', barmode='stack')
st.plotly_chart(bar_chart, use_container_width=True)
# fig.show()

hist_button = st.button('Criar histograma')  # criar um botão

if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
