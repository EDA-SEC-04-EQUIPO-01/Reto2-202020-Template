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

movies_details = 'themoviesdb/AllMoviesDetailsCleaned.csv'
movies_casting = 'themoviesdb/AllMoviesCastingRaw.csv'

# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________



# ----------------------------------- MENU ----------------------------------------

def printMenu():

    """Imprime el menu de opciones """

    print("Bienvenido")
    print("1- Cargar datos")
    print("2- Descubrir una compañía de producción")
    print("3- Conocer un director")
    print("4- Conocer un actor")
    print("5- Conocer un genero")
    print("6- Descubrir un país")
    print("0- Salir")


while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        catalogo = controller.initCatalog()
        print("Cargando información de los archivos ....")
        controller.loadData(catalogo, movies_details, movies_casting)
        print("Se cargo la información de",lt.size(catalogo["id"]),"películas")
    elif int(inputs[0]) == 2:
        company = input("Inserte el nombre de la compañía que desea conocer: ")
        producer = controller.discoverProducerCompany(catalogo,company)
        if producer != None:
            print(producer[0],"\nLa lista que se imprimió contiene las",producer[1],"películas de la compañía",company.title(),"que tienen un promedio acumulado de",producer[2],"\n")
        else:
            print("Esta compañía no existe en el registro")
    elif int(inputs[0]) == 3:
        director_name = input("Inserte el nobre del director ue desea conocer: ")
        director = controller.discoverDirector(catalogo, director_name)
        if director != None:
            print(director[0],"\nLa lista que se imprimió contiene las",director[1],"películas del director",director_name.title(),"que tienen un promedio acumulado de",director[2],"\n")
        else:
            print("Este director no existe en el registro")
    elif int(inputs[0]) == 6:
        country = input("Inserte el nombre del país que desea conocer: ")
        countries = controller.discoverMoviesByCountry(catalogo,country)
        if countries != None:

            print(countries[0],"\nSe imprimió la lista de las",countries[1],"peliculas del país",country.title())
        else:
            print("Este país no existe en el registro")

    else:
        sys.exit(0)
sys.exit(0)


