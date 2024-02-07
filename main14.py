import pandas as pd
import plotly.express as px

# Wczytanie danych
df = pd.read_csv('dane.csv')

# Analiza danych
mean_values = df.groupby('category')['value'].mean().reset_index()

# Wizualizacja danych
fig = px.bar(mean_values, x='category', y='value', title='Średnia wartość dla każdej kategorii')
fig.show()
