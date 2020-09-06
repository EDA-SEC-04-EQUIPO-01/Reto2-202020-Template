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
from DISClib.DataStructures import listiterator as it
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros

def newCatalogMovies():
  
    catalog = {"details":None,
                "casting":None}
    catalog["details"]=lt.newList("ARRAY_LIST")
    catalog["casting"]=lt.newList("ARRAY_LIST")
    return catalog

def addDetails(catalog, details):
    lt.addLast(catalog["details"],details)

def addCasting(catalog,casting):
    lt.addLast(catalog["casting"],casting)


# -----------------------------------------------------

# ==============================
# Funciones de consulta
# ==============================

def moviesSize(catalog):
    return lt.size(catalog["details"])

def getMovieNameByPos(catalog, pos):
    peli = lt.getElement(catalog["details"],pos)
    name = peli["original_title"]
    return name

def getMovieDateByPos(catalog, pos):
    peli = lt.getElement(catalog["details"],pos) 
    r_date = peli["release_date"]
    return r_date

def getMovieVoteCountByPos(catalog,pos):
    peli = lt.getElement(catalog["details"],pos) 
    v_count = peli["vote_count"]
    return v_count

def getMovieVoteAverageByPos(catalog,pos):
    peli = lt.getElement(catalog["details"],pos) 
    v_average = peli["vote_average"]
    return v_average

def getMovieLanguageByPos(catalog,pos):
    peli = lt.getElement(catalog["details"],pos) 
    language = peli["original_language"]
    return language

# ==============================
# Funciones de Comparacion
def compare():
    pass
# ==============================


