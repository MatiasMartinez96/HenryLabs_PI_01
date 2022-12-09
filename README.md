<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1 - Matias Martinez** </h1>

# <h1 align=center>**`Data Engineering`**</h1>

<p align="center">
<img src="[[https://www.google.com/url?sa=i&url=https%3A%2F%2Fmorioh.com%2Fp%2Fe8d81910885d&psig=AOvVaw21_uEiqd-XHm75Iqr5wVlT&ust=1670647152569000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCMiwmeLb6_sCFQAAAAAdAAAAABAJ](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.dataversity.net%2Fwant-data-engineer%2F&psig=AOvVaw0b5MTclr5HuKSfnvJ0gwR2&ust=1670647438406000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCMDm1urc6_sCFQAAAAAdAAAAABAE)](https://onlinedegrees.sandiego.edu/wp-content/uploads/2022/01/how-to-become-a-data-engineer.jpg)"  height=300>
</p>

¡Bienvenidos a mi primer proyecto individual de la etapa de LABS de SoyHenry ! En este repositorio podrán observar el desarrollo de un proceso EDA, la creación de una API y un container de Docker y su consecuente deploy en Mogenius. La finalidad del proyecto es simular el rol de un ***Data Engineer***.


Herramientas utilizadas:

+ Python, Docker, FastAPI, Jupyter Notebooks.

+ Librerias de Python: Requests, Pandas, Numpy, Statistics.
<hr> 

## **Introducción**

La idea de este proyecto es lograr internalizar los conocimientos requeridos para la elaboración y ejecución de una API.

`Application Programming Interface` es una interfaz que permite que dos aplicaciones se comuniquen entre sí, independientemente de la infraestructura subyacente. Son herramientas muy versátiles y fundamentales para la creación de, por ejemplo, pipelines, ya que permiten mover y brindar acceso simple a los datos que se quieran disponibilizar a través de los diferentes endpoints, o puntos de salida de la API.

Hoy en día contamos con **FastAPI**, un web framework moderno y de alto rendimiento para construir APIs con Python.
<p align=center>
<img src = 'https://i.ibb.co/9t3dD7D/blog-zenvia-imagens-3.png' height=250><p>

## **Propuesta de trabajo**

El proyecto consiste en realizar una ingesta de datos desde diversas fuentes, posteriormente aplicar las transformaciones que considere pertinentes, y luego disponibilizar los datos limpios para su consulta a través de una API. Esta API será construida en un entorno virtual dockerizado.

Los datos serán obtenidos en archivos de diferentes extensiones, como *csv* o *json*. Se realizará un EDA para cada dataset. Posteriormente, se relacionarán los datasets así pueden acceder a su información por medio de consultas a la API.

Las consultas a realizar son:

+ Máxima duración según tipo de film (película/serie), por plataforma y por año:
    El request debe ser: get_max_duration(año, plataforma, [min o season])

+ Cantidad de películas y series (separado) por plataforma
    El request debe ser: get_count_plataform(plataforma)  
  
+ Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.
    El request debe ser: get_listedin('genero')  
    Como ejemplo de género pueden usar 'comedy', el cuál deberia devolverles un cunt de 2099 para la plataforma de amazon.

+ Actor que más se repite según plataforma y año.
  El request debe ser: get_actor(plataforma, año)

## **Pasos del proyecto**

1. Ingesta y normalización de datos

2. Relacionar el conjunto de datos y crear la tabla necesaria para realizar consultas

3. Desarrollar funciones para realizar las consultas con sus respectivos parámetros

4. Crear la API (utilizando Uvicorn, FastAPI) en un entorno Docker

5. Testear las consultas solicitadas

6. Realizar un video demostrativo

7. Realizar un deployment en Mogenius

<p align=center>
<img src = 'https://i.postimg.cc/2SwvnTcw/Sin-t-tulo.png' height = 400></p>

## **Video demostrativo**

Link: 

+ https://hub.docker.com/r/tiangolo/uvicorn-gunicorn-fastapi/

## **Deployment en Mogenius**

Link: 

## **Aclaraciones**

+ La carpeta "notebooks" contiene los archivos ETL y Querys pero con la extension .ipynb utilizados al comienzo del desarrollo del proyecto debido a la comodidad del uso de Jupyter Notebooks.

+ El archivo EDA.py contiene todo el proceso de ingesta de datos y transformacion de los mismos.

+ El archivo Querys.py contiene las funciones necesarias para realizar las solicitudes requeridas.

+ El archivo main.py contiene las instrucciones necesarias para crear la API

+ El archivo Dockerfile contiene el código necesario para crear el entorno Docker

