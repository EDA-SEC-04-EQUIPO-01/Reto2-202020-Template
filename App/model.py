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
  
    catalog = {'id': None, #Va
               'genres': None, #Va
               'original_title': None, #Va
               'production_companies': None, #Va
               'production_countries': None, #Va
               'release_date': None, #Va
               'vote_average': None, #Va
               'vote_count': None, #vA
               'actor_name': None, #Va
               'director_name': None} #Va
    catalog['id']=lt.newList("ARRAY_LIST")
    catalog['genres'] = mp.newMap(50,
                                   maptype='CHAINING',
                                   loadfactor=0.8,
                                   comparefunction=compare)
    catalog['original_title'] = mp.newMap(400000,
                                 maptype='CHAINING',
                                 loadfactor=1,
                                 comparefunction=compare)
    catalog['production_companies'] = mp.newMap(20000,
                                maptype='CHAINING',
                                loadfactor=0.8,
                                comparefunction=compare)
    catalog['production_countries'] = mp.newMap(200,
                                maptype='CHAINING',
                                loadfactor=0.8,
                                comparefunction=compare)
    catalog['release_date'] = mp.newMap(400000,
                                   maptype='CHAINING',
                                   loadfactor=1,
                                   comparefunction=compare)
    catalog['vote_count'] = mp.newMap(400000,
                                   maptype='CHAINING',
                                   loadfactor=1,
                                   comparefunction=compare)
    catalog['vote_average'] = mp.newMap(400000,
                                   maptype='CHAINING',
                                   loadfactor=1,
                                   comparefunction=compare)
    catalog['actor_name'] = mp.newMap(1000000,
                                   maptype='CHAINING',
                                   loadfactor=0.8,
                                   comparefunction=compare)
    catalog['director_name'] = mp.newMap(100000,
                                   maptype='CHAINING',
                                   loadfactor=0.8,
                                   comparefunction=compare)
    

    return catalog

def addId(catalog, details):
    lt.addLast(catalog["id"],details["\ufeffid"])

def addgenre(catalog,details):
    genres = details["genres"].rsplit("|")
    for g in genres:
        if mp.get(catalog["genres"],g)==None:
            genl=lt.newList(datastructure="ARRAY_LIST",cmpfunction=None)
            lt.addLast(genl,details["\ufeffid"])
            mp.put(catalog["genres"],g,genl)
        else:
            a = mp.get(catalog["genres"],g)
            lt.addLast(a["value"],details["\ufeffid"])

def addtitle(catalog,details):
    mp.put(catalog["original_title"],details["\ufeffid"],details["original_title"])

def addCompanies(catalog,details):
    if mp.get(catalog["production_companies"],details["production_companies"].lower())==None:
        genl=lt.newList(datastructure="ARRAY_LIST",cmpfunction=None)
        lt.addLast(genl,details["\ufeffid"])
        mp.put(catalog["production_companies"],details["production_companies"].lower(),genl)
    else:
        a = mp.get(catalog["production_companies"],details["production_companies"].lower())
        lt.addLast(a["value"],details["\ufeffid"])

def addCountries(catalog,details):
    if mp.get(catalog["production_countries"],details["production_countries"])==None:
        genl=lt.newList(datastructure="ARRAY_LIST",cmpfunction=None)
        lt.addLast(genl,details["\ufeffid"])
        mp.put(catalog["production_countries"],details["production_countries"],genl)
    else:
        a = mp.get(catalog["production_countries"],details["production_countries"])
        lt.addLast(a["value"],details["\ufeffid"])

def addVoteCount(catalog,details):
    mp.put(catalog["vote_count"],details["\ufeffid"],details["vote_count"])

def addVoteAverage(catalog,details):
    mp.put(catalog["vote_average"],details["\ufeffid"],details["vote_average"])

def addActors(catalog,casting):
    actors = []
    actors.append(casting["actor1_name"])
    actors.append(casting["actor2_name"])
    actors.append(casting["actor3_name"])
    actors.append(casting["actor4_name"])
    actors.append(casting["actor5_name"])
    for a in actors:
        if mp.get(catalog["actor_name"],a)==None:
            genl=lt.newList(datastructure="ARRAY_LIST",cmpfunction=None)
            lt.addLast(genl,casting["id"])
            mp.put(catalog["actor_name"],a,genl)
        else:
            b = mp.get(catalog["actor_name"],a)
            lt.addLast(b["value"],casting["id"])

def addDirector(catalog,casting):
    if mp.get(catalog["director_name"],casting["director_name"])==None:
        genl=lt.newList(datastructure="ARRAY_LIST",cmpfunction=None)
        lt.addLast(genl,casting["id"])
        mp.put(catalog["director_name"],casting["director_name"],genl)
    else:
        a = mp.get(catalog["director_name"],casting["director_name"])
        lt.addLast(a["value"],casting["id"])


# -----------------------------------------------------

# ==============================
# Funciones de consulta
# ==============================

def moviesSize(catalog):
    return lt.size(catalog["id"])


def getMovieNameByPos(catalog, pos):
    peli = mp.get(catalog["original_title"],pos)
    return peli

def getMovieDateByPos(catalog, pos):
    peli = mp.getElement(catalog["release_date"],pos) 
    return peli

def getMovieVoteCountByPos(catalog,pos):
    peli = mp.getElement(catalog["vote_count"],pos) 
    return peli

def getMovieVoteAverageByPos(catalog,pos):
    peli = mp.getElement(catalog["vote_average"],pos) 
    return peli

def discoverProducerCompany(catalog,company):
    idpelis = mp.get(catalog["production_companies"],company.lower())
    try:
        iterator = it.newIterator(idpelis["value"])
        count = lt.size(idpelis["value"])
        pelis = []
        sprom = 0
        while it.hasNext(iterator):
            element = it.next(iterator)
            peli = mp.get(catalog["original_title"],element)
            pelis.append(peli["value"])
            average = mp.get(catalog["vote_average"],element)
            sprom+= float(average["value"])
        prom = round(sprom/count,2)
        res = (pelis,count,prom)
    except:
        res = None
    return res
    


    

# ==============================
# Funciones de Comparacion
def compare(keyname, value):

    compare = me.getKey(value)
    if (keyname == compare):
        return 0
    elif (keyname > compare):
        return 1
    else:
        return -1
# ==============================


