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
               'director_name': None, #Va
               'director_id':None} #Va
    catalog['id']=lt.newList("ARRAY_LIST",cmpfunction=compare_num)
    catalog['genres'] = mp.newMap(50,
                                   maptype='CHAINING',
                                   loadfactor=0.8,
                                   comparefunction=compare_str)
    catalog['original_title'] = mp.newMap(400000,
                                 maptype='CHAINING',
                                 loadfactor=1,
                                 comparefunction=compare_num)
    catalog['production_companies'] = mp.newMap(350000,
                                maptype='CHAINING',
                                loadfactor=0.8,
                                comparefunction=compare_str)
    catalog['production_countries'] = mp.newMap(200,
                                maptype='CHAINING',
                                loadfactor=0.8,
                                comparefunction=compare_str)
    catalog['release_date'] = mp.newMap(400000,
                                   maptype='CHAINING',
                                   loadfactor=1,
                                   comparefunction=compare_num)
    catalog['vote_count'] = mp.newMap(400000,
                                   maptype='CHAINING',
                                   loadfactor=1,
                                   comparefunction=compare_num)
    catalog['vote_average'] = mp.newMap(400000,
                                   maptype='CHAINING',
                                   loadfactor=1,
                                   comparefunction=compare_num)
    catalog['actor_name'] = mp.newMap(1000000,
                                   maptype='CHAINING',
                                   loadfactor=0.8,
                                   comparefunction=compare_str)
    catalog['director_name'] = mp.newMap(350000,
                                   maptype='CHAINING',
                                   loadfactor=0.8,
                                   comparefunction=compare_str)
    catalog['director_id'] = mp.newMap(400000,
                                   maptype='CHAINING',
                                   loadfactor=0.8,
                                   comparefunction=compare_num)
    

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
    if mp.get(catalog["production_countries"],details["production_countries"].lower())==None:
        genl=lt.newList(datastructure="ARRAY_LIST",cmpfunction=None)
        lt.addLast(genl,details["\ufeffid"])
        mp.put(catalog["production_countries"],details["production_countries"].lower(),genl)
    else:
        a = mp.get(catalog["production_countries"],details["production_countries"].lower())
        lt.addLast(a["value"],details["\ufeffid"])

def addReleaseDate(catalog,details):
    mp.put(catalog["release_date"],details["\ufeffid"],details["release_date"])

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
    if mp.get(catalog["director_name"],casting["director_name"].lower())==None:
        genl=lt.newList(datastructure="ARRAY_LIST",cmpfunction=None)
        lt.addLast(genl,casting["id"])
        mp.put(catalog["director_name"],casting["director_name"].lower(),genl)
    else:
        a = mp.get(catalog["director_name"],casting["director_name"].lower())
        lt.addLast(a["value"],casting["id"])

def addDirectorId(catalog,casting):
    mp.put(catalog["director_id"],casting["id"],casting["director_name"])


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
        iterator = it.newIterator(me.getValue(idpelis))
        count = lt.size(me.getValue(idpelis))
        pelis = lt.newList("ARRAY_LIST")
        sprom = 0
        while it.hasNext(iterator):
            element = it.next(iterator)
            peli = mp.get(catalog["original_title"],element)
            lt.addLast(pelis,me.getValue(peli))
            average = mp.get(catalog["vote_average"],element)
            sprom+= float(me.getValue(average))
        prom = round(sprom/count,2)
        res = (pelis,count,prom)
    except:
        res = None
    return res

def discoverDirector(catalog,director_name):
    idpelis = mp.get(catalog["director_name"],director_name.lower())
    try:
        iterator = it.newIterator(me.getValue(idpelis))
        count = lt.size(me.getValue(idpelis))
        pelis = lt.newList("ARRAY_LIST")
        sprom = 0
        while it.hasNext(iterator):
            element = it.next(iterator)
            peli = mp.get(catalog["original_title"],element)
            lt.addLast(pelis,me.getValue(peli))
            average = mp.get(catalog["vote_average"],element)
            sprom+= float(me.getValue(average))
        prom = round(sprom/count,2)
        res = (pelis,count,prom) 
    except:
        res = None
    return res


def getActorInformation(catalog,actor):
    idactors = mp.get(catalog["actor_name"], actor)
    actores_directores = {}
    peliculas = []
    mayor_director = ""
    prom = []
    apariciones = 0
    try:
        cantidad_peliculas = lt.size(me.getValue(idactors)) 
        iterator = it.newIterator(me.getValue(idactors))
        while it.hasNext(iterator):
            element = it.next(iterator)
            nombre_pelis = me.getValue(mp.get(catalog["original_title"], element))
            peliculas.append(nombre_pelis)
            prom.append(me.getValue((mp.get(catalog["vote_average"], element))))
            director = me.getValue(mp.get(catalog["director_id"], element))
            if actores_directores.get(director, None)==None:
                actores_directores[director]=1
            else:
                actores_directores[director]+=1
            if actores_directores[director]>apariciones:
                mayor_director = director
                apariciones = actores_directores[director]
            retorno = (peliculas, cantidad_peliculas, prom, mayor_director)
    except:
        retorno = None

    return retorno


def moviesByGenre(catalog,genero):
    idgeneros = mp.get(catalog["genres"],genero)
    try:
        iterator = it.newIterator(me.getValue(idgeneros))
        cantidad = lt.size(me.getValue(idgeneros))
        peli_genero = lt.newList("ARRAY_LIST")
        votos = 0
        while it.hasNext(iterator):
            element = it.next(iterator)
            nombres_peli = mp.get(catalog["original_title"],element)
            lt.addLast(peli_genero,me.getValue(nombres_peli))
            average = mp.get(catalog["vote_average"],element)
            votos+= float(me.getValue(average))
        promedio = round(votos/cantidad,2)
        res = (cantidad,promedio,peli_genero)
    except:
        res = None
    return res

def discoverMoviesByCountry(catalog,country):
    idpelis = mp.get(catalog["production_countries"],country.lower())

    try:
        iterator = it.newIterator(me.getValue(idpelis))
        pelis = lt.newList("ARRAY_LIST")
        count = lt.size(idpelis)
        while it.hasNext(iterator):
            element = it.next(iterator)
            try:
                nombre = me.getValue(mp.get(catalog["original_title"],element))
                fecha = me.getValue(mp.get(catalog["release_date"],element))
                fechad = fecha.rsplit("/")
                año = fechad[2]
                director = me.getValue(mp.get(catalog["director_id"],element))
                peli = {"Título":nombre,"Año de lanzamiento":año,"Director":director}
                lt.addLast(pelis,peli)
            except:
                pass 
        res = (pelis,count)
    except:
        res = None
    return res
   

    

# ==============================
# Funciones de Comparacion
def compare_str(keyname, value):

    compare = me.getKey(value)
    if (keyname == compare):
        return 0
    elif (keyname > compare):
        return 1
    else:
        return -1

def compare_num(keyname, value):

    compare = float(me.getKey(value))
    if (float(keyname) == compare):
        return 0
    elif (float(keyname) > compare):
        return 1
    else:
        return -1
# ==============================