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
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert config
import time
import csv
from DISClib.DataStructures import listiterator as it


"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""
def loadCSVFile (file, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None  
    """
    lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    #lst = lt.newList("LINKED_LIST") #Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start =time.process_time() #ti
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = time.process_time() #tf
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------
def catalogo():
    catalogo = {"archivo_peliculas": None,
                "peliculasxcompañia": None,
                "peliculasxdirector": None,
                "peliculasxgenero":None,
                "peliculasxactor":None}

    catalogo["peliculasxcompañia"] = mp.newMap( numelements=1000,
                                                    prime=109345121,   
                                                    maptype='CHAINING', 
                                                    loadfactor=1.0, 
                                                    comparefunction=comparer)
    catalogo["peliculasxdirector"] = mp.newMap( numelements=1000,
                                                    prime=109345121,   
                                                    maptype='CHAINING', 
                                                    loadfactor=1.0, 
                                                    comparefunction=comparer)
                                                 
    catalogo["archivo_peliculas"] = mp.newMap(numelements=1000,
                                                    prime=109345121,   
                                                    maptype='CHAINING', 
                                                    loadfactor=1.0, 
                                                    comparefunction=comparer)
    catalogo["peliculasxgenero"] = mp.newMap(numelements=41,
                                                    prime=90537484771,   
                                                    maptype='PROBING', 
                                                    loadfactor=0.5, 
                                                    comparefunction=comparer)
    catalogo["peliculasxactor"] = mp.newMap(numelements=2000,
                                                    prime=109345121,   
                                                    maptype='CHAINING', 
                                                    loadfactor=1.0, 
                                                    comparefunction=comparer)
    return catalogo

def addMovies(catalog, movie):
    """
    Añade el nombre de una pelicula con su informacion
    """
    lt.addLast(catalog['Peliculas'], movie)
    mp.put(catalog['original_title'], movie['original_title'], movie)


# Funciones para agregar informacion al catalogo

def addcompany(catalogo, movie, compañia):
    """
    Añade el nombre de una compañia a la tabla de Hash para compañias en el catalogo
    """
    if mp.contains(catalogo["peliculasxcompañia"], compañia) == True:
        n = mp.get(catalogo["peliculasxcompañia"], compañia)
        lt.addLast(me.getValue(n), {"titulo":movie["original_title"], "calificacion":float(movie["vote_average"])})
    else:
        N = lt.newList("ARRAY_LIST")
        lt.addLast(N, {"titulo":movie["original_title"], "calificacion":float(movie["vote_average"])})
        mp.put(catalogo["peliculasxcompañia"], compañia, N)



def adddirector(catalogo, movie, director):
    C = catalogo["peliculasxdirector"]
    if "id" in movie:
        L = movie["id"]
    elif '\ufeffid' in movie:
        L = movie['\ufeffid']
    if mp.contains(C, director) == False:
        mp.put(catalogo["peliculasxdirector"], director, [])
    addpelistodirector(catalogo, L, director)


def addgenero(catalogo, movie, generos):
    for a in generos:
        if mp.contains(catalogo["peliculasxgenero"], a) and "id" in movie:
            addpelistogenre(catalogo, movie['id'] ,a)
        elif mp.contains(catalogo["peliculasxgenero"], a) and '\ufeffid' in movie:
            addpelistogenre(catalogo, movie['\ufeffid'] ,a)
        else:
            D = lt.newList("ARRAY_LIST")
            lt.addLast(D, {"titulo":movie["original_title"], "calificacion":float(movie["vote_average"])})
            mp.put(catalogo["peliculasxgenero"], a, D)
            

def addactor(catalogo, movie):
    C = {}
    Ana = catalogo["peliculasxactor"]
    for a in range(1, 6):
        fila = "actor"+str(a)+"_name"
        actor = movie[fila]
        if mp.contains(Ana, movie[fila]) and "id" in movie:
            addpelistoactor(catalogo, movie['id'], actor, movie)
        elif mp.contains(Ana, movie[fila]) and "\ufeffid" in movie:
            addpelistoactor(catalogo, movie['\ufeffid'], actor, movie)
        else:
            mp.put(catalogo["peliculasxactor"], actor, [])

def addcountry(catalogo, movie, pais):
    if mp.contains(catalogo["peliculasxpais"], pais) == True:
        n = mp.get(catalogo["peliculasxcompañia"], pais)
        addpelistocountry(catalogo, movie['\ufeffid'], pais, movie)
        if "id" in movie:
            addpelistocountry(catalogo, movie["id"], pais, movie)
        elif '\ufeffid' in movie:
            addpelistocountry(catalogo, movie['\ufeffid'], pais, movie)
    else:
        G = lt.newList("ARRAY_LIST")
        lt.addLast(G, {"titulo":movie["original_title"], "año de lanzamiento":movie["release_date"]})
        mp.put(catalogo["peliculasxpais"], pais, G)    

def calificacion(lista):
    N = 0
    B = 0
    A = it.newIterator(lista)
    while it.hasNext(A):
        C = it.next(A)
        N += float(C["calificacion"])
        B += 1
    N = round(N/B, 1)
    return {"Total de peilculas":B,
            "Calificacion promedio":N}



def calificacion2(lista):
    N = 0
    B = 0
    for A in lista:
        K = float(A["calificacion"])
        N += K
        B += 1
    N = round(N/B, 1)
    return {"Total de peilculas":B,
            "Calificacion promedio":N}


def calificacionActor(lista):
    Dire = {}
    N = 0
    B = 0
    mayor = 0
    nombre = None
    for A in lista:
        K = float(A["calificacion"])
        N += K
        B += 1
        if A["Nombre director"] not in Dire:
            Dire[A["Nombre director"]] = 1
        else:
            Dire[A["Nombre director"]] += 1
    for M in Dire:
        if (Dire[M] > mayor):
            mayor = Dire[M]
            nombre = M
        

    N = round(N/B, 1)
    return {"Total de peilculas":B,
            "Calificacion promedio":N,
            "Director con mayor colaboracion":nombre}


def addpelistodirector(catalogo, idp, director):
    cat = catalogo["archivo_peliculas"]
    B = mp.get(cat, idp)
    A = me.getValue(B)
    n = mp.get(catalogo["peliculasxdirector"], director)
    M = me.getValue(n)
    M.append(A)

def addpelistogenre(catalogo, idp, genero):
    cat = catalogo["archivo_peliculas"]
    B = mp.get(cat, idp)
    A = me.getValue(B)
    n = mp.get(catalogo["peliculasxgenero"], genero)
    M = me.getValue(n)
    lt.addLast(M, A)

def addpelistoactor(catalogo, idp, actor, movie):
    cat = catalogo["archivo_peliculas"]
    B = mp.get(cat, idp)
    A = me.getValue(B)
    n = mp.get(catalogo["peliculasxactor"], actor)
    M = me.getValue(n)
    A["Nombre director"] = movie["director_name"]
    M.append(A)

def addpelistocountry(catalogo, idp, pais, movie):
    cat = catalogo["archivo_peliculas"]
    B = mp.get(cat, idp)
    A = me.getValue(B)
    A["Fecha de lanzamiento"] = movie["release_date"]
    n = mp.get(catalogo["peliculasxpais"], pais)
    M = me.getValue(n)
    del A["calificacion"]
    lt.addLast(M, A)

# ==============================
# Funciones de consulta
# ==============================
def getBooksByAuthor(catalog, authorname):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    author = mp.get(catalog['authors'], authorname)
    if author:
        return me.getValue(author)
    return None

def pelisdeproductora(productora,MD):
    ite=it.newIterator(MD)
    pegaron=lt.newList("ARRAY_LIST")
    while it.hasNext(ite)==True:
        sera=it.next(ite)
        if sera['production_companies']==productora:
            lt.addLast(pegaron,sera)
    return pegaron

def totalpelis(pegaron):
    return lt.size(pegaron)

def showdirector(catalogo, direc):
    if mp.contains(catalogo["peliculasxdirector"], direc):
        A = mp.get(catalogo["peliculasxdirector"], direc)
        A = me.getValue(A)
    else:
        A = "No files.author found"
    return A

def showcompanies(catalogo, compan):
    if mp.contains(catalogo["peliculasxcompañia"], compan):
        A = mp.get(catalogo["peliculasxcompañia"], compan)
        A = me.getValue(A)
    else:
        A ="No files.company found"


def showgenres(catalogo, genr):
    if mp.cxns(catalogo["peliculasxgenero"], genr):
        A = mp.get(catalogo["peliculasxgenero"], genr)
        A = me.getValue(A)
    else:
        A ="No files.genre found"
    return A

def showactors(catalogo, acto):
    if mp.contains(catalogo["peliculasxactor"], acto):
        A = mp.get(catalogo["peliculasxactor"], acto)
        A = me.getValue(A)
    else:
        A ="No files.actor found"
    return A

def showcountry(catalogo, pais):
    if mp.contains(catalogo["peliculasxpais"], pais):
        A = mp.get(catalogo["peliculasxpais"], pais)
        A = me.getValue(A)
    else:
        A ="No files.country found"
    return A
# ==============================
# Funciones de Comparacion
# ==============================
def promediopelis(pegaron):
    ite=it.newIterator(pegaron)
    a=0
    b=0
    while it.hasNext(ite)==True:
        es=it.next(ite)
        a+=float(es['vote_average'])
        b+=1
    return float(a/b)



def compareMoviesIds(id1, id2):
    """
    Compara dos ids de libros
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


def compareIds(id, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1

def compareLanguages(keyname, lenguaje):
    entry = me.getKey(lenguaje)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1

def compareMoviesTittles(keyname, titulo):
    
    entry = me.getKey(titulo)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1


def compareTagNames(name, tag):
    tagentry = me.getKey(tag)
    if (name == tagentry):
        return 0
    elif (name > tagentry):
        return 1
    else:
        return -1

def compareAvergae(id, tag):
    tagentry = me.getKey(tag)
    if (int(id) == int(tagentry)):
        return 0
    elif (int(id) > int(tagentry)):
        return 1
    else:
        return 0

def compareVoteCount(id, tag):
    tagentry = me.getKey(tag)
    if (int(id) == int(tagentry)):
        return 0
    elif (int(id) > int(tagentry)):
        return 1
    else:
        return 0

def compareTagIds(id, tag):
    tagentry = me.getKey(tag)
    if (int(id) == int(tagentry)):
        return 0
    elif (int(id) > int(tagentry)):
        return 1
    else:
        return 0


def compareMapYear(id, tag):
    tagentry = me.getKey(tag)
    if (id == tagentry):
        return 0
    elif (id > tagentry):
        return 1
    else:
        return 0


def compareYears(year1, year2):
    if (int(year1) == int(year2)):
        return 0
    elif (int(year1) > int(year2)):
        return 1
    else:
        return 0

