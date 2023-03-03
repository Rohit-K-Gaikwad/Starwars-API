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
from models.datamodels.Py_Films import PyFilms  # pydantic model
from models.datamodels.Py_Characters import PyCharacters
from models.datamodels.Py_Planets import PyPlanets
from models.datamodels.Py_Species import PySpecies
from models.datamodels.Py_Vehicles import PyVehicles
from models.datamodels.Py_Starships import PyStarships

from dal.db_conn_helper import get_db_conn
from dal.dml import insert_resource
from utils.fetch_data import hit_url
from utils.timing import timeit


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
        "homeworld"
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
            char.homeworld
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


@timeit
def store_planets():
    planets = film_data.planets
    planets_data = []

    planets_columns = [
        "name",
        "orbital_period",
        "gravity",
        "climate",
        "rotation_period",
        "surface_water",
        "population",
        "terrain",
    ]

    for planet in planets:
        response = hit_url(planet)
        pla_ = response.json()
        pla_ = PyPlanets(**pla_)
        planets_values = [
            pla_.name,
            pla_.orbital_period,
            pla_.gravity,
            pla_.climate,
            pla_.rotation_period,
            pla_.surface_water,
            pla_.population,
            pla_.terrain,

            ]

        planet_id = int(planet.split("/")[-2])
        result = insert_resource(
            "planet",
            "planet_id",
            planet_id,
            planets_columns,
            planets_values
        )
        planets_data.append(pla_)
    return planets_data


@timeit
def store_starships():
    starships = film_data.starships
    starships_data = []

    starships_columns = [
        "name",
        "MGLT",
        "cargo_capacity",
        "consumables",
        "cost_in_credits",
        "hyperdrive_rating",
        "manufacturer",
        "model",
        "starship_class",
        "passengers"
    ]

    for starship in starships:
        response = hit_url(starship)
        star_ = response.json()
        star_ = PyStarships(**star_)
        starships_values = [
            star_.name,
            star_.MGLT,
            star_.cargo_capacity,
            star_.consumables,
            star_.cost_in_credits,
            # star_.crew,
            star_.hyperdrive_rating,
            star_.manufacturer,
            # star_.max_atmosphering_speed,
            star_.model,
            star_.starship_class,
            star_.passengers

        ]
        starship_id = int(starship.split("/")[-2])
        result = insert_resource(
            "starship",
            "starship_id",
            starship_id,
            starships_columns,
            starships_values
        )
        starships_data.append(star_)
    return starships_data


@timeit
def store_vehicles():
    vehicles = film_data.vehicles
    vehicles_data = []

    vehicles_columns = [
        "name",
        "cargo_capacity",
        "consumables",
        "cost_in_credits",
        "crew",
        "manufacturer",
        "max_atmosphering_speed",
        "model",
        "vehicle_class",
    ]

    for vehicle in vehicles:
        response = hit_url(vehicle)
        veh_ = response.json()
        veh_ = PyVehicles(**veh_)
        vehicles_values = [
            veh_.name,
            veh_.cargo_capacity,
            veh_.consumables,
            veh_.cost_in_credits,
            veh_.crew,
            veh_.manufacturer,
            veh_.max_atmosphering_speed,
            veh_.model,
            veh_.vehicle_class
        ]
        vehicle_id = int(vehicle.split("/")[-2])
        result = insert_resource(
            "vehicle",
            "vehicle_id",
            vehicle_id,
            vehicles_columns,
            vehicles_values
        )
        vehicles_data.append(veh_)
    return vehicles_data


@timeit
def store_species():
    species = film_data.species
    species_data = []

    species_columns = [
        "name",
        "average_height",
        "average_lifespan",
        "classification",
        "designation",
        "eye_colors",
        "hair_colors",
        "skin_colors",
    ]

    for specie in species:
        response = hit_url(specie)
        spe_ = response.json()
        spe_ = PySpecies(**spe_)
        species_values = [
            spe_.name,
            spe_.average_height,
            spe_.average_lifespan,
            spe_.classification,
            spe_.designation,
            spe_.eye_colors,
            spe_.hair_colors,
            spe_.skin_colors

            ]

        specie_id = int(specie.split("/")[-2])
        result = insert_resource(
            "species",
            "species_id",
            specie_id,
            species_columns,
            species_values
        )
        species_data.append(spe_)
    return species_data


if __name__ == "__main__":
    data = RFilms().get_sample_data(id_=1)
    film_data = PyFilms(**data)

    # create DB connection
    conn = get_db_conn()

    film_columns = [
        "title",
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
        film_data.opening_crawl,
        film_data.director,
        film_data.producer,
        film_data.release_date,
        film_data.created.strftime("%y-%m-%d"),
        film_data.edited.strftime("%y-%m-%d"),
        film_data.url,
    ]

    result = insert_resource(
        "film", "film_id", film_data.episode_id, film_columns, film_values
    )

    # TODO
    # capture all characters
    # film_data.characters
    # only values will change
    # column list can be once created and re-used

    character_data = store_characters()
    # planet_data = store_planets()
    # starships_data = store_starships()
    # vehicle_data = store_vehicles()
    # species_data = store_species()
