# Importamos del archivo EDA el Dataframe necesario para realizar las consultas y la libreria pandas. También importamos la libreria Pandas.

import pandas as pd
from EDA import df_plataformas

# Restablecemos los indices del Dataframe para optimizar las consultas

df_plataformas.reset_index(drop=True, inplace=True)

# Test del Dataframe importado
df_plataformas



# PRIMER CONSULTA

# - Máxima duración según tipo de film (película/serie), por plataforma y por año: El request debe ser: 
#   get_max_duration(año, plataforma, [min o season])

def get_max_duration(anio:int, plataforma:str, min_season:str):  

    # Verifico cual de las 4 plataformas ingresó el usuario y modifico la variable plataforma para usarla luego en los filtros
    if plataforma == 'amazon':
        plataforma = 'amz'
    elif plataforma == 'disney':
        plataforma = 'dis'
    elif plataforma == 'hulu':
        plataforma = 'hl'
    else:
        plataforma = 'ntf'

    # Creo un Dataframe temporal filtrando sus datos de acuerdo a:

        # Filtro 1 = plataforma elegida anteriormente
    df_temp = df_plataformas.query('show_id.str.contains(@plataforma)')
        # Filtro 2 = año y tipo de duracion (minutos o seasons)
    df_temp = df_temp.query("release_year == @anio and min_season == @min_season")
        # Restablecemos los indices del Dataframe para optimizar las consultas
    df_temp.reset_index(drop=True, inplace=True)
    
    # Obtengo el indice con mayor duracion del Dataframe con idxmax(). Luego utilizo este valor como parámetro para 
    # obtener la fila cuya duracion es la mayor.
    df_temp = df_temp.iloc[df_temp['duration'].idxmax()]

    # Creamos un diccionario con la informacion de df_temp
    datos = {
        'titulo' : [df_temp['title']]
    }
    # Creamos un nuevo Dataframe a partir del diccionario anterior para retornar el resultado.
    df_titulo = pd.DataFrame(datos)
    
    return df_titulo

# Test de la funcion
get_max_duration(2018,'hulu','min')



# SEGUNDA CONSULTA
# - Cantidad de películas y series (separado) por plataforma El request debe ser: get_count_plataform(plataforma)

def get_count_platform(plataforma:str):

    # Guardo en una variable auxiliar la plataforma elegida por el usuario
    aux = plataforma
    
    # Verifico cual de las 4 plataformas ingresó el usuario y modifico la variable plataforma para usarla luego en los filtros
    if plataforma == 'amazon':
        plataforma = 'amz'
    elif plataforma == 'disney':
        plataforma = 'dis'
    elif plataforma == 'hulu':
        plataforma = 'hl'
    else:
        plataforma = 'ntf'

    # Creo un Dataframe temporal filtrando sus datos de acuerdo a la plataforma elegida anteriormente
    df_temp = df_plataformas.query('show_id.str.contains(@plataforma)')

    # Calculo la cantidad de veces que aparecen las palabras Movie y TV Show en el Dataframe df_temp y luego guardo sus resultados en 2 variables
    cant_movies = df_temp.apply(lambda df_temp: df_temp['type'] == 'Movie', axis=1).sum()
    cant_tvshows = df_temp.apply(lambda df_temp: df_temp['type'] == 'TV Show', axis=1).sum()

    # Creamos un diccionario con la variables aux (plataforma elegida por el usuario), cant_movies y cant_tvshows 
    datos = {
        'platform' : [aux],
        'movie': cant_movies,
        'tvshow': cant_tvshows
    }

    # Creamos un nuevo Dataframe a partir del diccionario anterior para retornar el resultado.
    df_count = pd.DataFrame(datos)
    
    return df_count


# Test de la funcion
get_count_platform('netflix')



# TERCER CONSULTA
# - Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo. El request debe ser:
#   get_listedin('genero'). Como ejemplo de género pueden usar 'comedy', el cuál deberia devolverles un count 
#   de 2099 para la plataforma de amazon.


def get_listedin(genero:str):
    
    # Obtengo los resultados de filtrar el Dataframe de acuerdo a la plataforma y el género elegido por el usuario.
    # Luego con la funcion shape[0] obtengo la cantidad de filas que cumplen con los filtros. 
    cant_genero1 = df_plataformas.query('listed_in.str.contains(@genero) and show_id.str.contains("amz")').shape[0]

    cant_genero2 = df_plataformas.query('listed_in.str.contains(@genero) and show_id.str.contains("dis")').shape[0]

    cant_genero3 = df_plataformas.query('listed_in.str.contains(@genero) and show_id.str.contains("hl")').shape[0]

    cant_genero4 = df_plataformas.query('listed_in.str.contains(@genero) and show_id.str.contains("ntf")').shape[0]
    
    # Creamos una lista con las 4 variables anteriores y la ordenamos descendentemente para poder obtener la mayor
    # de ellas (la que se encuentre en la primera posicion de la lista)
    cantidades = sorted([cant_genero1, cant_genero2, cant_genero3, cant_genero4], reverse=True)
    
    # Determino, de acuerdo a cual variable de la lista sea la mayor, la plataforma a la que pertenece dicha cantidad y guardo
    # ambos datos en un diccionario 
    if cantidades[0] == cant_genero1:
        datos = {
        'platform' : ['amazon'],
        'cantidad': cant_genero1,
        }
        df_cant = pd.DataFrame(datos)
    elif cantidades[0] == cant_genero2:
        datos = {
        'platform' : ['disney'],
        'cantidad': cant_genero2,
        }
        df_cant = pd.DataFrame(datos)

    elif cantidades[0] == cant_genero3:
        datos = {
        'platform' : ['hulu'],
        'cantidad': cant_genero3,
        }
        df_cant = pd.DataFrame(datos)
    else:
        datos = {
        'platform' : ['netflix'],
        'cantidad': cant_genero4,
        }
    
    
    # Creamos un nuevo Dataframe a partir del diccionario anterior para retornar el resultado.
    df_cant = pd.DataFrame(datos)

    return df_cant


# Test de la funcion
get_listedin('Comedy')



# CUARTA CONSULTA
# - Actor que más se repite según plataforma y año. El request debe ser: get_actor(plataforma, año)

def get_actor(plataforma:str, anio:int):
    
    # Guardo en una variable auxiliar la plataforma elegida por el usuario
    aux = plataforma
    
    # Importamos la funcion mode de la libreria statistics
    from statistics import mode
    
    # Verifico cual de las 4 plataformas ingresó el usuario y modifico la variable plataforma para usarla luego en los filtros
    if plataforma == 'amazon':
        plataforma = 'amz'
    elif plataforma == 'disney':
        plataforma = 'dis'
    elif plataforma == 'hulu':
        plataforma = 'hl'
    else:
        plataforma = 'ntf'

    # Creo un Dataframe temporal filtrando sus datos de acuerdo a la plataforma y el año elegidos anteriormente 
    df_temp = df_plataformas.query('show_id.str.contains(@plataforma) and release_year == @anio')

    # Creo una lista vacia
    total_actores = []

    # Creo una lista con los valores de la columna cast del Dataframe
    lista_actores = df_temp['cast'].tolist()
    
    #En este ciclo obtengo cada actor individualmente y los agrego a la lista total_actores
    for i in range(len(lista_actores)):
        lista_actores2 = lista_actores[i].split(",")
        for j in range (len(lista_actores2)):
            if lista_actores2[j] != 'Sin dato':
                total_actores.append(lista_actores2[j])
    
    # Creamos un diccionario con la variables:
    # aux = plataforma elegida por el usuario 
    # cantidad = cantidad de veces que aparece el actor mas elegido en la lista total_actores
    # actores = con la funcion mode verifico cual es el item (actor) que mas se repite en la lista total_actores
    datos = {
            'platform' : [aux],
            'cantidad': total_actores.count(mode(total_actores)),
            'actores' : mode(total_actores)
            }
    
    # Creamos un nuevo Dataframe a partir del diccionario anterior para retornar el resultado.
    df_act = pd.DataFrame(datos)
    
    

    return df_act

# Test de la funcion
get_actor('netflix',2018)
