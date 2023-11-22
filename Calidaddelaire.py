# %% [markdown]
# # Analisis calidad del aire (Jesus Morillo)

# %%
import pandas as pd

data = pd.read_csv(r"D:\Documentos\Visual Code\Análisis de la calidad del aire\air-quality-data.csv")

data

# %%

data['DateTime'] = pd.to_datetime(data['DateTime'], format="%d/%m/%Y %H:%M")

# Muestra el DataFrame 'data'
data

# %%
data.info()

# %% [markdown]
# # muestra la contaminación promedio anual con un gráfico de líneas

# %%
data.head()

data['Year'] = data.DateTime.dt.year

data

# %%
year_avg = data.groupby("Year") ['PM2.5'].mean()

year_avg

year_avg.plot(kind = 'line', figsize =(15,5));



# %%
year_avg.plot(kind = 'line', figsize =(15,5), style = '*');

# %% [markdown]
# # Dibuje el gráfico de área que muestre la contaminación promedio mensual

# %%
data['Month'] = data.DateTime.dt.month


month_avg = data.groupby('Month')['PM2.5'].mean()

month_avg.plot(kind = 'area', figsize=(12,5), color = 'orange');


# %% [markdown]
# # Dibuje un gráfico de barras para mostrar la contaminación promedio por hora

# %%
data['Hour'] = data.DateTime.dt.hour

hour_avg = data.groupby('Hour')['PM2.5'].mean()

hour_avg.plot(kind='bar', figsize=(18, 5), color = 'purple')

# %% [markdown]
# # Generalmente, ¿en qué mes se registró el aire como "Muy insalubre"?

# %%
x = data [(data['PM2.5'] >= 150.5) & (data['PM2.5'] <= 250.4)]

x.value_counts('Month')

# %% [markdown]
# # Normalmente, ¿en qué mes/es el aire estaba fresco (bueno)?

# %%
y = data [data['PM2.5'] <= 12.0]

y.value_counts('Month')

# %% [markdown]
# # En el año 2018 cuantas veces el ICA se registró "MODERADO"

# %%
z = data[(data['Year'] == 2018) & (data['PM2.5'] >= 12.1) & (data['PM2.5']<= 35.4)]

z.Year.unique()

z['PM2.5']

# %% [markdown]
# # ¿Cómo estuvo el tiempo en el mes de junio y julio?

# %%
data.head()

data [data['Month'] == 1]['PM2.5'].mean()

# %%
data [data['Month'] == 7]['PM2.5'].mean()


