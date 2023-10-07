import pandas as pd
import streamlit as st

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('sivigila_vih.csv', delimiter=';')  # Asegúrate de especificar el delimitador adecuado

# Convertir la columna 'fecha' a formato de fecha para poder ordenarla
df['fecha'] = pd.to_datetime(df['fecha'])

# Ordenar por 'fecha' de mayor a menor
df = df.sort_values(by='fecha', ascending=False)

# Ordenar por 'codigo_barrio' de menor a mayor
df = df.sort_values(by='codigo_barrio')

# Ordenar por 'nombre_barrio' de la A a la Z
df = df.sort_values(by='nombre_barrio')

# Ordenar por 'codigo_comuna'
df = df.sort_values(by='codigo_comuna')

# Mostrar el DataFrame filtrado y ordenado en una tabla de Streamlit
st.dataframe(df)