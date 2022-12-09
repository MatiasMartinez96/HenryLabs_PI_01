# Importamos:
#   - La libreria necesaria para poder crear nuestra API
#   - Las funciones necesarias del archivo Querys.py 
from fastapi import FastAPI
from Querys import get_max_duration, get_count_platform, get_listedin, get_actor

# Instanciamos la clase FastAPI importada anteriormente
app = FastAPI()

# Utilizamos el metodo get (del protocolo http) para realizar una peticion de acuerdo al nombre de la ruta ("/")
@app.get("/") # Decorador
def read_root():
    return {"HENRY LAB 01 - Matias Martinez - DTS-05"}


@app.get("/get_max_duration/{anio}/{plataforma}/{tipo}") # Decorador
# Funcion asíncrona que utiliza una de las funciones importadas al inicio del script
async def max_dur(anio:int,plataforma:str,tipo:str):
    # Convertimos en lista el resultado de la funcion importada para facilitar el retorno de su informacion en la API
    lista = get_max_duration(anio,plataforma,tipo).to_numpy().tolist()
    return f'La pelicula/serie de maxima duración de la plataforma {plataforma} es {lista[0][0]}'


@app.get("/get_count_platform/{plataforma}") # Decorador
# Funcion asíncrona que utiliza una de las funciones importadas al inicio del script
async def count(plataforma:str):
    # Convertimos en lista el resultado de la funcion importada para facilitar el retorno de su informacion en la API
    lista = get_count_platform(plataforma).to_numpy().tolist()
    return f'La plataforma: {lista[0][0]} tiene {lista[0][1]} peliculas y {lista[0][2]} series'


@app.get("/get_listedin/{genero}") # Decorador
# Funcion asíncrona que utiliza una de las funciones importadas al inicio del script
async def listed(genero:str):
    # Convertimos en lista el resultado de la funcion importada para facilitar el retorno de su informacion en la API
    lista = get_listedin(genero).to_numpy().tolist()
    return f'La plataforma en la que el género {genero} se repite más veces es {lista[0][0]} con un valor de {lista[0][1]}'


@app.get("/get_actor/{plataforma}/{anio}") # Decorador
# Funcion asíncrona que utiliza una de las funciones importadas al inicio del script
async def actor(plataforma:str,anio:int):
    # Convertimos en lista el resultado de la funcion importada para facilitar el retorno de su informacion en la API
    lista = get_actor(plataforma,anio).to_numpy().tolist()
    return f'El actor que mas se repite en la plataforma {plataforma} en el año {anio} es{lista[0][2]}. Aparece en {lista[0][1]} peliculas/series'