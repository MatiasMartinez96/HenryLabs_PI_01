from fastapi import FastAPI
from Querys import get_max_duration, get_count_platform, get_listedin, get_actor

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World .---."}


@app.get("/get_max_duration/{anio}/{plataforma}/{tipo}")
async def max_dur(anio:int,plataforma:str,tipo:str):
    lista = get_max_duration(anio,plataforma,tipo).to_numpy().tolist()
    return f'La pelicula/serie de maxima duración de la plataforma {plataforma} es {lista[0][0]}'


@app.get("/get_count_platform/{plataforma}")
async def count(plataforma:str):
    lista = get_count_platform(plataforma).to_numpy().tolist()
    return f'La plataforma: {lista[0][0]} tiene {lista[0][1]} peliculas y {lista[0][2]} series'


@app.get("/get_listedin/{genero}")
async def listed(genero:str):
    lista = get_listedin(genero).to_numpy().tolist()
    return f'La plataforma en la que el género {genero} se repite más veces es {lista[0][0]} con un valor de {lista[0][1]}'


@app.get("/get_actor/{plataforma}/{anio}")
async def actor(plataforma:str,anio:int):
    lista = get_actor(plataforma,anio).to_numpy().tolist()
    return f'El actor que mas se repite en la plataforma {plataforma} en el año {anio} es{lista[0][2]}. Aparece en {lista[0][1]} peliculas/series'
