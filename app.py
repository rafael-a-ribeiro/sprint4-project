import streamlit as st
import pandas as pd
import plotly_express as px
import plotly.graph_objects as go
import numpy as np

car_data = pd.read_csv('vehicles.csv')  # lendo os dados

# Separando a informação de modelo e fabricante
car_data[['manufacturer', 'model']
         ] = car_data['model'].str.split(' ', 1, expand=True)

st.header('Data Viewer')
min_price = car_data['price'].min()
max_price = car_data['price'].max()
min_price, max_price = st.slider(
    "Select the range of price you want to be showed", float(min_price), float(max_price), (float(min_price), float(max_price)))
filtered = car_data[(car_data['price'] >=
                    min_price) & (car_data['price'] <= max_price)]
st.dataframe(filtered)

st.header('Vehicle Types by Manufacturer')

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

st.header('Price X Days listed colored by manufacturer')
# Criando gráfico de dispersão
scatter = px.scatter(car_data, x="days_listed",
                     y="price", color='manufacturer')
st.plotly_chart(scatter, use_container_width=True)

st.header("Compare price distribuition between types of car")

# Tipos de carros que serão usados na comparação
car_types = car_data['type'].unique()
type = st.selectbox("Select the fisrt type of car", car_types)
type2 = st.selectbox("Select the second type of car", car_types, index=1)

# Checkbox para normalizar o gráfico
normalized = st.checkbox("Normalize histogram", value=True)
if normalized:
    histnorm = 'probability'
    yaxis_title_text = 'Percent'
else:
    histnorm = ''
    yaxis_title_text = 'Count'

# Filtrando Dataframe com os tipos selecionados
car_data_filtered = car_data[car_data['type'] == type]
car_data_filtered2 = car_data[car_data['type'] == type2]

# Construindo Histograma Preço X Tipo
hist_type = go.Figure()
hist_type.add_trace(go.Histogram(
    x=car_data_filtered['price'], name=type, histnorm=histnorm))
hist_type.add_trace(go.Histogram(
    x=car_data_filtered2['price'], name=type2, histnorm=histnorm))
hist_type.update_layout(
    barmode='overlay', xaxis_title_text='Price', yaxis_title_text=yaxis_title_text)
hist_type.update_traces(opacity=0.6)
st.plotly_chart(hist_type, use_container_width=True)
