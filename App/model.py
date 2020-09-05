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
    
    catalog = {'id': None,
               'budget': None,
               'genres': None,
               'imdb_id': None,
               'original_language': None,
               'original_title': None,
               'overview': None,
               'popularity': None,
               'production_companies': None,
               'production_countries': None,
               'release_date': None,
               'revenue': None,
               'runtime': None,
               'spoken_languages': None,
               'status': None,
               'tagline': None,
               'title': None,
               'vote_average': None,
               'vote_count': None,
               'production_companies_number': None,
               'production_countries_number': None,
               'spoken_languages_number': None}

    catalog['id'] = lt.newList('SINGLE_LINKED', compare)
    catalog['budget'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compare)
    catalog['genres'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compare)
    catalog['imdb_id'] = mp.newMap(1000,
                                maptype='CHAINING',
                                loadfactor=0.7,
                                comparefunction=compare)
    catalog['original_language'] = mp.newMap(1000,
                                  maptype='CHAINING',
                                  loadfactor=0.7,
                                  comparefunction=compare)
    catalog['original_title'] = mp.newMap(500,
                                 maptype='CHAINING',
                                 loadfactor=0.7,
                                 comparefunction=compare)
    catalog['overview'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compare)
    catalog['popularity'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
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
    catalog['revenue'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compare)
    catalog['runtime'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compare)
    catalog['spoken_languages'] = mp.newMap(1000,
                                maptype='CHAINING',
                                loadfactor=0.7,
                                comparefunction=compare)
    catalog['status'] = mp.newMap(1000,
                                  maptype='CHAINING',
                                  loadfactor=0.7,
                                  comparefunction=compare)
    catalog['tagline'] = mp.newMap(500,
                                 maptype='CHAINING',
                                 loadfactor=0.7,
                                 comparefunction=compare)
    catalog['title'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compare)
    catalog['vote_average'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compare)
    catalog['vote_count'] = mp.newMap(1000,
                                maptype='CHAINING',
                                loadfactor=0.7,
                                comparefunction=compare)
    catalog['production_companies_number'] = mp.newMap(1000,
                                  maptype='CHAINING',
                                  loadfactor=0.7,
                                  comparefunction=compare)
    catalog['production_countries_number'] = mp.newMap(500,
                                 maptype='CHAINING',
                                 loadfactor=0.7,
                                 comparefunction=compare)
    catalog['spoken_languages_number'] = mp.newMap(500,
                                 maptype='CHAINING',
                                 loadfactor=0.7,
                                 comparefunction=compare)

    return catalog

def newCatalogCasting():

    catalog = {'id': None,
               'actor1_name': None,
               'actor1_gender': None,
               'actor2_name': None,
               'actor2_gender': None,
               'actor3_name': None,
               'actor3_gender': None,
               'actor4_name': None,
               'actor4_gender': None,
               'actor5_name': None,
               'actor5_gender': None,
               'actor_number': None,
               'director_name': None,
               'director_gender': None,
               'director_number': None,
               'producer_name': None,
               'producer_number': None,
               'screeplay_name': None,
               'editor_name': None}

    catalog['id'] = lt.newList('SINGLE_LINKED', compare)
    catalog['actor1_name'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compare)
    catalog['actor1_gender'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compare)
    catalog['actor2_name'] = mp.newMap(1000,
                                maptype='CHAINING',
                                loadfactor=0.7,
                                comparefunction=compare)
    catalog['actor2_gender'] = mp.newMap(1000,
                                  maptype='CHAINING',
                                  loadfactor=0.7,
                                  comparefunction=compare)
    catalog['actor3_name'] = mp.newMap(500,
                                 maptype='CHAINING',
                                 loadfactor=0.7,
                                 comparefunction=compare)
    catalog['actor3_gender'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compare)
    catalog['actor4_name'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compare)
    catalog['actor4_gender'] = mp.newMap(1000,
                                maptype='CHAINING',
                                loadfactor=0.7,
                                comparefunction=compare)
    catalog['actor5_name'] = mp.newMap(1000,
                                  maptype='CHAINING',
                                  loadfactor=0.7,
                                  comparefunction=compare)
    catalog['actor5_gender'] = mp.newMap(500,
                                 maptype='CHAINING',
                                 loadfactor=0.7,
                                 comparefunction=compare)
    catalog['actor_number'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compare)
    catalog['director_name'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compare)
    catalog['director_gender'] = mp.newMap(1000,
                                maptype='CHAINING',
                                loadfactor=0.7,
                                comparefunction=compare)
    catalog['director_number'] = mp.newMap(1000,
                                  maptype='CHAINING',
                                  loadfactor=0.7,
                                  comparefunction=compare)
    catalog['producer_name'] = mp.newMap(500,
                                 maptype='CHAINING',
                                 loadfactor=0.7,
                                 comparefunction=compare)
    catalog['producer_number'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compare)
    catalog['screeplay_name'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compare)
    catalog['editor_name'] = mp.newMap(1000,
                                maptype='CHAINING',
                                loadfactor=0.7,
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


