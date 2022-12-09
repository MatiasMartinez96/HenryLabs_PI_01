# INGESTA DE DATOS - EXTRACCIÓN

# Importamos las librerias necesarias

import pandas as pd
import numpy as np
import requests as rq
import io

# Realizamos la extraccion de los datos utilizando la libreria request

req_amazon = rq.get('https://raw.githubusercontent.com/HX-FAshur/PI01_DATA05/main/Datasets/amazon_prime_titles.csv').content

req_disney = rq.get('https://raw.githubusercontent.com/HX-FAshur/PI01_DATA05/main/Datasets/disney_plus_titles.csv').content

req_hulu = rq.get('https://raw.githubusercontent.com/HX-FAshur/PI01_DATA05/main/Datasets/hulu_titles.csv').content

req_netflix = rq.get('https://raw.githubusercontent.com/HX-FAshur/PI01_DATA05/main/Datasets/netflix_titles.json').content


# Convertimos las request obtenidas en "Dataframes" de Pandas

df_amazon = pd.read_csv(io.StringIO(req_amazon.decode('utf-8')))

df_disney = pd.read_csv(io.StringIO(req_disney.decode('utf-8')))

df_hulu = pd.read_csv(io.StringIO(req_hulu.decode('utf-8')))

df_netflix = pd.read_json(io.StringIO(req_netflix.decode('utf-8')))


# Verficamos la informacion de cada dataframe

df_amazon.head(2)
df_disney.head(2)
df_hulu.head(2)
df_netflix.head(19)



# NORMALIZACIÓN DE DATOS

# Modificamos ID's para poder diferenciarlos por plataforma

df_amazon.show_id = df_amazon.show_id + '_amz'
df_disney.show_id = df_disney.show_id + '_dis'
df_hulu.show_id = df_hulu.show_id + '_hl'
df_netflix.show_id = df_netflix.show_id + '_ntf'

# Concatenamos (unimos) los 4 dataframes en un único dataframe para poder realizar las consultas

df_plataformas = pd.concat([df_amazon, df_disney, df_hulu, df_netflix], axis=0)

df_plataformas.head(2)


# Dividimos los datos de la columna "duration" en 2 columnas: "duration" (con el valor numérico de la duración) y "min/season" (con el tipo de valor ya sea minutos o season)

temp = df_plataformas["duration"].str.split(" ", n = 1, expand = True) 
  
df_plataformas.drop(columns =["duration"], inplace = True)

df_plataformas["duration"]= temp[0]

df_plataformas["min_season"]= temp[1]
  
df_plataformas


# Convertimos el tipo de datos de la columna "duration" a Float

df_plataformas['duration'] = df_plataformas['duration'].astype(float)


# Elimino las columnas que considero innecesarias para las consultas del proyecto 
# (solo las elimino del Dataframe df_plataformas). Si se presenta la situacion de que la 
# compañia/empresa necesite algunos de estos datos en el futuro puedo obtenerlos de los 4 dataframes 
# creados al inicio del script.

df_plataformas.drop(['date_added','rating', 'description'], axis = 'columns', inplace=True)


# Verificamos la existencia de valores nulos por columna

print(df_plataformas['show_id'].isna().sum())
print(df_plataformas['type'].isna().sum())
print(df_plataformas['title'].isna().sum())
print(df_plataformas['director'].isna().sum())
print(df_plataformas['cast'].isna().sum())
print(df_plataformas['country'].isna().sum())
print(df_plataformas['release_year'].isna().sum())
print(df_plataformas['listed_in'].isna().sum())
print(df_plataformas['duration'].isna().sum())
print(df_plataformas['min_season'].isna().sum())


# Modificamos los valores nulos de acuerdo a la siguiente condicion:
#   - Si la columna es tipo string (object en Pandas), los NaN se reemplazan por 'Sin dato'.
#   - Si la columna es de tipo float, los NaN reemplazan por la Mediana de la columna. La elección de
#     la mediana (85) se debe a que la mayoria de las peliculas duran más de 1 hora y el valor de la media 
#     es 67 (aproximadamente 1 hora).

df_plataformas.fillna({'director': 'Sin dato', 'cast': 'Sin dato', 'country': 'Sin dato', 'duration': df_plataformas['duration'].median() , 'min_season': 'Sin dato'}, inplace=True)

df_plataformas['min_season'].replace({"Season":'season',"Seasons":'season'}, inplace=True)


df_plataformas
