"""
TODO

1. Pull data for the first movie ("A New Hope") and save in DB.

2. Replace the data for each endpoint listed in the JSON object and insert
that data into database table

For example - "A new hope" movie has following resource endpoints -

- characters 15
- planets  7
- starships   10
- vehicles  5
- species  40


"""

from utils.fetch_data import hit_url
<<<<<<< HEAD
from utils.timing import timeit
from resources.R_Films import RFilms   # resource model
from resources.R_Characters import RCharacters
from models.datamodels.Py_Films import PyFilms  # pydantic
from models.datamodels.Py_Characters import PyCharacters

=======
from resources.R_Films import RFilms   # resource model
from models.datamodels.Py_Films import PyFilms  # pydantic model
>>>>>>> 3972742614d8274c76d079fd813259e2793a146d

from dal.db_conn_helper import get_db_conn
from dal.dml import insert_resource


<<<<<<< HEAD
@timeit
def store_characters():
    characters = film_data.characters
    characters_data = []

    char_columns = [
        "name",
        "height",
        "mass",
        "hair_color",
        "skin_color",
        "eye_color",
        "birth_year",
        "gender",
        "homeworld",
    ]

    for character in characters:
        response = hit_url(character)
        char = response.json()
        char = PyCharacters(**char)
        char_values = [
            char.name,
            char.height,
            char.mass,
            char.hair_color,
            char.skin_color,
            char.eye_color,
            char.birth_year,
            char.gender,
            char.homeworld,
        ]

        char_id = int(character.split("/")[-2])
        result = insert_resource(
            "characters",
            "char_id",
            char_id,
            char_columns,
            char_values
        )
        characters_data.append(char)
    return characters_data
=======
def char_(char_data_):
    char_data = []
    for url in char_data_:
        char = hit_url(url)
        charr = char.json()
        char_data.append(charr.get("name"))

    return char_data


def planet_(pla_data_):
    pla_data = []
    for url in pla_data_:
        planet = hit_url(url)
        plaa = planet.json()
        pla_data.append(plaa.get("name"))
    return pla_data
>>>>>>> 3972742614d8274c76d079fd813259e2793a146d


if __name__ == "__main__":
    data = RFilms().get_sample_data(id_=1)
    film_data = PyFilms(**data)
    conn = get_db_conn()   # create DB connection
    char = film_data.characters

    film_columns = [
        "title",
        "episode_id",
        "opening_crawl",
        "director",
        "producer",
        "release_date",
        "created",
        "edited",
        "url",
<<<<<<< HEAD
=======
        "characters",
        "planets",
>>>>>>> 3972742614d8274c76d079fd813259e2793a146d
    ]

    film_values = [
        film_data.title,
        film_data.episode_id,
        film_data.opening_crawl,
        film_data.director,
        film_data.producer,
        film_data.release_date,
        film_data.created.strftime("%y-%m-%d"),
        film_data.edited.strftime("%y-%m-%d"),
        film_data.url,
<<<<<<< HEAD
    ]
=======
        str(char_(film_data.characters)),
        str(planet_(film_data.planets)),

    ]
    breakpoint()
>>>>>>> 3972742614d8274c76d079fd813259e2793a146d

    result = insert_resource(
        "film", "film_id", film_data.episode_id, film_columns, film_values
    )

<<<<<<< HEAD
    character_data = store_characters()

=======
>>>>>>> 3972742614d8274c76d079fd813259e2793a146d
    # TODO
    # capture all characters
    # film_data.characters
    # only values will change
    # column list can be once created and re-used

    # TODO
    # capture all planets
    # film_data.planets
    # only values will change
    # column list can be once created and re-us
