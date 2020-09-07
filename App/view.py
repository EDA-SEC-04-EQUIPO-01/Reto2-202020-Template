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


booksfile = 'GoodReads/books-small.csv'
tagsfile = 'GoodReads/tags.csv'
booktagsfile = 'GoodReads/book_tags-small.csv'

movies_details = 'themoviesdb/SmallMoviesDetailsCleaned.csv'
movies_casting = 'themoviesdb/MoviesCastingRaw-small'

# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________


def printAuthorData(author):
    """
    Imprime los libros de un autor determinado
    """
    if author:
        print('Autor encontrado: ' + author['name'])
        print('Promedio: ' + str(author['average_rating']))
        print('Total de libros: ' + str(lt.size(author['books'])))
        iterator = it.newIterator(author['books'])
        while it.hasNext(iterator):
            book = it.next(iterator)
            print('Titulo: ' + book['title'] + '  ISBN: ' + book['isbn'])
    else:
        print('No se encontro el autor')


def printBooksbyTag(books):
    """
    Imprime los libros que han sido clasificados con
    una etiqueta
    """
    print('Se encontraron: ' + str(lt.size(books)) + ' Libros')
    iterator = it.newIterator(books)
    while it.hasNext(iterator):
        book = it.next(iterator)
        print(book['title'])


def printBooksbyYear(books):
    """
    Imprime los libros que han sido publicados en un
    año
    """
    print('Se encontraron: ' + str(lt.size(books)) + ' Libros')
    iterator = it.newIterator(books)
    while it.hasNext(iterator):
        book = it.next(iterator)
        print(book['title'])

# ----------------------------------- MENU ----------------------------------------

def printMenu():

    """Imprime el menu de opciones """

    print("Bienvenido")
    print("1- Cargar datos")
    print("0- Salir")


while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        catalogo = controller.initCatalog()
        print("Cargando información de los archivos ....")
        controller.loadData(catalogo, movies_details, movies_casting)

        # Puntos a,b,c,d,e,f a contestar:
        print(str("La cantidad de películas cargadas es: ") +str(controller.moviesSize))
        print(str("El titulo de estas peliculas son: ") +str(controller.getMovieNameByPos(catalogo,1)))
        print(str("Las fechas de estreno fueron: ") +str(controller.getMovieDateByPos(catalogo,1)))
        print(str("El promedio de votacion de estas peliculas fue de: ") +str(controller.getMovieVoteCountByPos(catalogo,1)))
        print(str("El numero de votos de estas peliculas fue de: ") +str(controller.getMovieVoteAverageByPos(catalogo,1)))
        print(str("Los idiomas de estas peliculas son: ") +str(controller.getMovieLanguageByPos(catalogo,1)))



    else:
        sys.exit(0)
sys.exit(0)