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

from resources.R_Films import RFilms   # resource model
from models.datamodels.Py_Films import PyFilms # pydantic model

from dal.db_conn_helper import get_db_conn
from dal.dml import insert_resource


if __name__ == "__main__":
    data = RFilms().get_sample_data(id_=1)
    film_data = PyFilms(**data)
    conn = get_db_conn()   # create DB connection

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

    ]
    breakpoint()

    result = insert_resource(
        "film", "film_id", film_data.episode_id, film_columns, film_values
    )

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
