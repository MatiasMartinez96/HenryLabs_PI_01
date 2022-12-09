# Importamos del archivo ETL el Dataframe necesario para realizar las consultas y la libreria pandas

import pandas as pd
from ETL import df_plataformas

# Restablecemos los indices del Dataframe para optimizar las consultas

df_plataformas.reset_index(drop=True, inplace=True)


df_plataformas



# PRIMER CONSULTA

# - Máxima duración según tipo de film (película/serie), por plataforma y por año: El request debe ser: get_max_duration(año, plataforma, [min o season])

def get_max_duration(anio:int, plataforma:str, min_season:str):  

    if plataforma == 'amazon':
        plataforma = 'amz'
    elif plataforma == 'disney':
        plataforma = 'dis'
    elif plataforma == 'hulu':
        plataforma = 'hl'
    else:
        plataforma = 'ntf'

    df_temp = df_plataformas.query('show_id.str.contains(@plataforma)')
    
    df_temp = df_temp.query("release_year == @anio and min_season == @min_season")

    df_temp.reset_index(drop=True, inplace=True)

    df_temp = df_temp.iloc[df_temp['duration'].idxmax()]

    datos = {
        'titulo' : [df_temp['title']]
    }

    df_titulo = pd.DataFrame(datos)
    
    return df_titulo


get_max_duration(2018,'hulu','min')



# SEGUNDA CONSULTA
# - Cantidad de películas y series (separado) por plataforma El request debe ser: get_count_plataform(plataforma)

def get_count_platform(plataforma:str):

    aux = plataforma
    
    if plataforma == 'amazon':
        plataforma = 'amz'
    elif plataforma == 'disney':
        plataforma = 'dis'
    elif plataforma == 'hulu':
        plataforma = 'hl'
    else:
        plataforma = 'ntf'

    df_temp = df_plataformas.query('show_id.str.contains(@plataforma)')

    cant_movies = df_temp.apply(lambda df_temp: df_temp['type'] == 'Movie', axis=1).sum()
    cant_tvshows = df_temp.apply(lambda df_temp: df_temp['type'] == 'TV Show', axis=1).sum()

    datos = {
        'platform' : [aux],
        'movie': cant_movies,
        'tvshow': cant_tvshows
    }

    df_count = pd.DataFrame(datos)
    
    return df_count


get_count_platform('netflix')


# TERCER CONSULTA
# - Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo. El request debe ser:
#   get_listedin('genero'). Como ejemplo de género pueden usar 'comedy', el cuál deberia devolverles un count 
#   de 2099 para la plataforma de amazon.


def get_listedin(genero:str):
    
    cant_genero1 = df_plataformas.query('listed_in.str.contains(@genero) and show_id.str.contains("amz")').shape[0]

    cant_genero2 = df_plataformas.query('listed_in.str.contains(@genero) and show_id.str.contains("dis")').shape[0]

    cant_genero3 = df_plataformas.query('listed_in.str.contains(@genero) and show_id.str.contains("hl")').shape[0]

    cant_genero4 = df_plataformas.query('listed_in.str.contains(@genero) and show_id.str.contains("ntf")').shape[0]
    
    cantidades = sorted([cant_genero1, cant_genero2, cant_genero3, cant_genero4], reverse=True)
    
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
    
    
    df_cant = pd.DataFrame(datos)

    return df_cant


# CUARTA CONSULTA
# - Actor que más se repite según plataforma y año. El request debe ser: get_actor(plataforma, año)

def get_actor(plataforma:str, anio:int):
    
    aux = plataforma
    
    from statistics import mode
    
    if plataforma == 'amazon':
        plataforma = 'amz'
    elif plataforma == 'disney':
        plataforma = 'dis'
    elif plataforma == 'hulu':
        plataforma = 'hl'
    else:
        plataforma = 'ntf'

    df_temp = df_plataformas.query('show_id.str.contains(@plataforma) and release_year == @anio')

    total_actores = []

    lista_actores = df_temp['cast'].tolist()
    
    #En este ciclo obtengo cada actor individualmente
    for i in range(len(lista_actores)):
        lista_actores2 = lista_actores[i].split(",")
        for j in range (len(lista_actores2)):
            if lista_actores2[j] != 'Sin dato':
                total_actores.append(lista_actores2[j])
    
    
    datos = {
            'platform' : [aux],
            'cantidad': total_actores.count(mode(total_actores)),
            'actores' : mode(total_actores)
            }
    
    
    df_act = pd.DataFrame(datos)
    
    

    return df_act


get_actor('netflix',2018)
