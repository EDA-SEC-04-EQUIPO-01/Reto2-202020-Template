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


"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

def initCatalog():
    catalog = model.newCatalogMovies()
    return catalog



# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
def loadData(catalog, file_details, file_casting):
    loadDetails(catalog, file_details)
    loadCasting(catalog,file_casting)

def loadDetails(catalog, file_details):
    dialect = csv.excel()
    dialect.delimiter=";"
    with open(  cf.data_dir + file_details, encoding="utf-8") as csvfile:
        row = csv.DictReader(csvfile, dialect=dialect)
        for details in row: 
            model.addId(catalog, details)
            model.addgenre(catalog,details)
            model.addtitle(catalog,details)
            model.addCompanies(catalog,details)
            model.addCountries(catalog,details)
            model.addReleaseDate(catalog,details)
            model.addVoteCount(catalog,details)
            model.addVoteAverage(catalog,details)


def loadCasting(catalog, file_casting):
    dialect = csv.excel()
    dialect.delimiter=";"
    with open(  cf.data_dir + file_casting, encoding="utf-8") as csvfile:
        row = csv.DictReader(csvfile, dialect=dialect)
        for casting in row: 
            model.addActors(catalog, casting)
            model.addDirector(catalog,casting)
            model.addDirectorId(catalog,casting)

def discoverProducerCompany(catalog,company):
    return model.discoverProducerCompany(catalog,company)

def discoverDirector(catalog,director_name):
    return model.discoverDirector(catalog,director_name)

def discoverMoviesByCountry(catalog,country):
    return model.discoverMoviesByCountry(catalog,country)

# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________

def moviesSize(catalog):
    return model.moviesSize(catalog)

def getMovieNameByPos(catalog, pos):
    return model.getMovieNameByPos(catalog, pos)

def getMovieDateByPos(catalog, pos):
    return model.getMovieDateByPos(catalog, pos)

def getMovieVoteCountByPos(catalog,pos):
    return model.getMovieVoteCountByPos(catalog,pos)

def getMovieVoteAverageByPos(catalog,pos):
    return model.getMovieVoteAverageByPos(catalog,pos)

def getMovieLanguageByPos(catalog,pos):
    return model.getMovieLanguageByPos(catalog,pos)
