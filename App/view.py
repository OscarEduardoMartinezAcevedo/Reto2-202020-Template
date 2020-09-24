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

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________
moviesdetails = "Data\AllMoviesDetailsCleaned.csv"
moviescasting = "Data\AllMoviesCastingRaw.csv"




# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________



# ___________________________________________________
#  Menu principal
# ___________________________________________________
def menuprint():
    print("Opciones:")
    print("1- Inicializar Catálogo")
    print("2- Cargar informacion a una lista")
    print("3- Cargar información en el catálogo")
    print("4-Peliculas de...(Productora)")
    print("5-Peliculas dirigidas por:")
    print("6-Peliculas donde ha hecho presencia")
    print("7-Peliculas de genero:")
    print("8-Peliculas de...(Pais)")
    print("0- Salir")

def main():
    bt=lt.newList()
    b=lt.newList()
    r=lt.newList()
    t=lt.newList()
    tr=lt.newList()
    menuprint()
    sionR=True
    while sionR:
        opcion=input("Elija rey: ")
        if int(opcion) in list(range(0,9)):
            if int(opcion)==1:
                controller.iniCatalog()
            elif int(opcion)==2:
                print("Loading files...")
                MD=controller.loadData(moviesdetails)
                MC=controller.loadData(moviescasting)
                print("Loaded files...")
                print("Loaded ",MD["size"]," elements of Details(list)")
                print("Loaded ",MC["size"]," elements of Castings(list)")
                #print("Prueba:")
                #x=0
                #y=it.newIterator(MD)
                #while x<5:
                #    x+=1
                #    print(it.next(y)['\ufeffid'])
                #    print(type(it.next(y)))

            elif int(opcion)==3:
                loadedC=controller.loadData(moviesdetails)
                print(loadedC)
                print("Loaded info:Completed!")    
            elif int(opcion)==4:
                #authorname = input("Nombre del autor a buscar: ")
                #authorinfo = controller.getBooksByAuthor(cont, authorname)
                #printAuthorData(authorinfo)
                MD=controller.loadData(moviesdetails)
                productora=input("La productora rey: \n")
                print(controller.la4(productora,MD))
            #elif int(opcion)==5:
                #print("naranjas")
            elif int(opcion)== 5:
                director = input("El director rey: \n")
                t1 = process_time()
                print(controller.mostrar_directores(catalogo, director))
                t2 = process_time()
                print("time running: ", t2-t1,' seconds')
            elif int(opcion)== 6:
                actor = input("El actor rey: \n")
                t1 = process_time()
                print(controller.mostrar_actor(catalogo, actor))
                t2 = process_time()
                print("time running: ", t2-t1,' seconds')
            elif int(opcion)== 7:
                genero = input("El genero rey: \n")
                t1 = process_time()
                print(controller.mostrar_generos(catalogo, genero))
                t2 = process_time()
                print("time running: ", t2-t1,' seconds')
            elif int(opcion)==0:
                sionR=False
                print("Vemos Rey")
        else:
            print("Escriba Bien")

main()

