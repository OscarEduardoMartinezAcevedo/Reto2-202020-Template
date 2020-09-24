"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
from App import model
import csv
from DISClib.ADT import list as lt
import time

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""
#antes del miercoles a la midnight
# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

def iniCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    return model.catalogo()

def loadData(file):
    """
    Carga los datos de los archivos en el modelo
    """
    return model.loadCSVFile(file)


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def getBooksByAuthor(catalog, authorname):
    """
    Retorna los libros de un autor
    """
    authorinfo = model.getBooksByAuthor(catalog, authorname)
    return authorinfo

def la4(productora,MD):
    return {"Peliculas: ":model.pelisdeproductora(productora,MD),
            "Total ":model.totalpelis(model.pelisdeproductora(productora,MD)),
            "Promedio ":model.promediopelis(model.pelisdeproductora(productora,MD))}
def loadinfo(catalogo, archivo1, archivo2):
    loaddatas(catalogo, archivo1)
    loadcasting(catalogo, archivo2)
    
def loaddatas(catalogo, archivo):
    sep = ";"
    dialect = csv.excel()
    dialect.delimiter=sep
    archivo = cf.data_dir + archivo
    input_file = csv.DictReader(open(archivo, encoding="utf-8"), dialect=dialect)
    
    for movie in input_file:
        model.addmovie(catalogo, movie)
        compañia = movie["production_companies"] # Se obtienen las compañias
        generos = (movie["genres"]).split(sep="|")
        model.añadir_compañia(catalogo, movie, compañia)
        model.añadir_genero(catalogo, movie, generos)

def loadcasting(catalogo, archivo):
    sep = ";"
    dialect = csv.excel()
    dialect.delimiter=sep
    archivo = cf.data_dir + archivo
    input_file = csv.DictReader(open(archivo, encoding="utf-8"), dialect=dialect)

    for movie in input_file:
        director = movie["director_name"]
        model.añadir_director(catalogo, movie, director)
        model.añadir_actor(catalogo, movie)



def showcompanies(catalogo, compan):
    N = model.showcompanies(catalogo, compan)
    if N != "No files.company found":
        C = model.calificacion(N)
        return [C, N]
    else:
        return N

def showdirector(catalogo, direc):
    N = model.showdirector(catalogo, direc)
    if N != "No files.author found":
        C = model.calificacion2(N)
        return [C, N]
    else:
        return N

def showgenres(catalogo, genr):
    N = model.showgenres(catalogo, genr)
    if N != "No files.genre found":
        C = model.calificacion(N)
        return [C, N]
    else:
        return N

def showactors(catalogo, acto):
    N = model.showactors(catalogo, acto)
    if N != "No files.actor found":
        C = model.calificacionActor(N)
        return [C, N]
    else:
        return N


A = ("Ready? set...").strip()
print(A)