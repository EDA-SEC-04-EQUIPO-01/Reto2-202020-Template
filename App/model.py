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
               'vote_count': None} #Va

    catalog['id'] = lt.newList('SINGLE_LINKED', compare)
    catalog['genres'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compare)
    catalog['original_title'] = mp.newMap(500,
                                 maptype='CHAINING',
                                 loadfactor=0.7,
                                 comparefunction=compare)
    catalog['production_companies'] = mp.newMap(1000,
                                maptype='CHAINING',
                                loadfactor=0.7,
                                comparefunction=compare)
    catalog['production_countries'] = mp.newMap(1000,
                                  maptype='CHAINING',
                                  loadfactor=0.7,
                                  comparefunction=compare)
    catalog['release_date'] = mp.newMap(500,
                                 maptype='CHAINING',
                                 loadfactor=0.7,
                                 comparefunction=compare)
    catalog['vote_average'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compare)
    catalog['vote_count'] = mp.newMap(1000,
                                maptype='CHAINING',
                                loadfactor=0.7,
                                comparefunction=compare)

    return catalog

def newCatalogCasting():

    catalog = {'id': None, #Va
               'actor1_name': None, #Va
               'actor2_name': None, #Va
               'actor3_name': None, #Va
               'actor4_name': None, #Va
               'actor5_name': None, #Va
               'director_name': None} #Va

    catalog['id'] = lt.newList('SINGLE_LINKED', compare)
    catalog['actor1_name'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compare)
    catalog['actor2_name'] = mp.newMap(1000,
                                maptype='CHAINING',
                                loadfactor=0.7,
                                comparefunction=compare)
    catalog['actor3_name'] = mp.newMap(500,
                                 maptype='CHAINING',
                                 loadfactor=0.7,
                                 comparefunction=compare)
    catalog['actor4_name'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compare)
    catalog['actor5_name'] = mp.newMap(1000,
                                  maptype='CHAINING',
                                  loadfactor=0.7,
                                  comparefunction=compare)
    catalog['director_name'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compare)

    return catalog

# -----------------------------------------------------

# ==============================
# Funciones de consulta
# ==============================



# ==============================
# Funciones de Comparacion
def compare():
    pass
# ==============================


