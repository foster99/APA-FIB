# Autores
* Edgar Pérez Blanco
* Bartomeu Perelló Comas

# Instrucciones 

Dado que la practica ha sido realizada en Notebooks a traves de la plataforma Google Colab, recomendamos su ejecucion en dicho entorno. Este es el enlace a la [practica](https://colab.research.google.com/drive/15yaxBhVm_daX6YuK8XP7a1TqhkNhV7d0?usp=sharing). Con tan solo ejecutar el notebook, automaticamente se descarga de internet el dataset y se realiza tanto el preprocesado de los datos como el entremaiento/evaluacion de los modelos.

De todas formas, adjuntamos el fichero ``requeriments.txt`` por si se quiere ejecutar de forma local, y descargar las librerias necesarias.

## El Notebook

El notebook esta formado por 3 partes: 
    1. Descarga de datos
    2. Preproceso de datos
    3. Entrenamiento

### 1. Descarga de datos
Esta parte encargara de descargar el dataset de internet y añadirle la cabacera, ademas de reemplazar un ciertos carateres '-' por '_' con el fin de evitar ambiguedades al cargar los datos.

### 2. Preproceso de datos

Esta parte se encarga de aplicarle el preprocesado correspondiente a los datos. Guardara el dataset procesado, asi como sus respectivas parciones para entrenamiento y test en formato pickle comprimido.

### 3. Entrenamiento
La ultima parte cargara los datos comprimidos en pickle generados previamente y ejecutara todos los modelos. Los parametros optimos han sido previamente procesados, pero si de todas formas se quieren re-explorar de nuevo, al inicio de esta parte, hay una serie de flags que permiten activar o desactivar la optimizacion de cada uno de los modelos:

```
# Valores por defecto a Falso, con el fin de no alargar el tiempo de ejecucion:
train_LinearRegression = False
train_Ridge            = False
train_KNN              = False
train_MLP              = False
train_RandomForest     = False
```

## Script de descarga de datos 

A pesar de que el notebook es capaz de descargar automaticamente el dataset, adjuntamos tambien un fichero ``data_download.py``, el cual es un script en python que descarga el dataset de internet en formato ``.csv``.

Se puede ejecutar el script con el siguiente comando:
```
$ python3 data_download.py
```