"""
1. TODO - import all resource classes here -> Done
2. TODO - get count of each resource       -> Done
3. TODO - get singular resource URL from each resource
    - for example,
    - hit plural URL of starships and that will list all starships data
    - iterate on each starship data and capture singular URLs
    - all_starship_data = data.get("results")
    - you will iterate on `all_starship_data`,
4. TODO - pull data from random 3 "singular" resource URLs
    - utilize`utils` package to produce random 3 numbers from resource ids
    - and pull data for them
5. TODO - convert the script into CLI application
6. TODO - pretty pprint output (from ppprint import ppprint)
"""
import argparse
from pprint import pprint

from utils.randgen import ProduceNumbers
from utils.fetch_data import hit_url
from utils.timing import timeit

# resource classes
from resources.R_Characters import RCharacters
from resources.R_Films import RFilms
from resources.R_Planets import RPlanets
from resources.R_Species import RSpecies
from resources.R_Starships import RStarships
from resources.R_Vehicles import RVehicles

# pydantic models
from models.datamodels.Py_Characters import PyCharacters
from models.datamodels.Py_Films import PyFilms
from models.datamodels.Py_Planets import PyPlanets
from models.datamodels.Py_Vehicles import PyVehicles
from models.datamodels.Py_Species import PySpecies
from models.datamodels.Py_Starships import PyStarships


def characters_data():
    """
    Getting count of Characters; Validating Characters data; Generates list of all Characters
    URLs
    """

    character_obj = RCharacters()
    total_characters = character_obj.get_count()
    print(f"\nGetting Characters Count :: ", end="")
    pprint(total_characters)

    character_data = character_obj.get_sample_data()
    character_data = PyCharacters(**character_data)
    print(f"\nValidating Character Data :: \n")
    pprint(character_data)

    global character_urls
    character_urls = character_obj.get_resource_urls()
    print(f"\nGetting list of all Character URLs::")
    pprint(character_urls)
    return character_urls


def films_data():
    """
    Getting count of Films; Validating Films data; Generates list of all Films
    URLs
    """
    film_obj = RFilms()
    total_films = film_obj.get_count()
    print(f"\nGetting Films Count :: ", end="")
    pprint(total_films)

    film_data = film_obj.get_sample_data()
    film_data = PyFilms(**film_data)
    print(f"\nValidating Film Data is successfully completed\n")
    # pprint(film_data)

    global film_urls
    film_urls = film_obj.get_resource_urls()
    print(f"\nGetting list of all Film URLs::")
    pprint(film_urls)
    return film_urls


def planets_data():
    """
    Getting count of Planets; Validating Planets data; Generates list of all Planets
    URLs
    """
    planet_obj = RPlanets()
    total_planets = planet_obj.get_count()
    print(f"\nGetting Planets Count :: ", end="")
    pprint(total_planets)

    planet_data = planet_obj.get_sample_data()
    planet_data = PyPlanets(**planet_data)
    print(f"\nValidating Planet Data :: \n")
    pprint(planet_data)

    global planet_urls
    planet_urls = planet_obj.get_resource_urls()
    print(f"\nGetting list of all Planet URLs::")
    pprint(planet_urls)
    return planet_urls


def species_data():
    """
    Getting count of Species; Validating Species data; Generates list of all Species
    URLs
    """
    specie_obj = RSpecies()
    total_species = specie_obj.get_count()
    print(f"\nGetting Species Count :: ", end="")
    pprint(total_species)

    specie_data = specie_obj.get_sample_data()
    specie_data = PySpecies(**specie_data)
    print(f"\nValidating Species Data :: \n")
    pprint(specie_data)

    global specie_urls
    specie_urls = specie_obj.get_resource_urls()
    print(f"\nGetting list of all Species URLs::")
    pprint(specie_urls)
    return specie_urls


def starships_data():
    """
    Getting count of Starships; Validating Starships data; Generates list of all Starships
    URLs
    """
    starship_obj = RStarships()
    total_starships = starship_obj.get_count()
    print(f"\nGetting Starships Count :: ", end="")
    pprint(total_starships)

    starship_data = starship_obj.get_sample_data(2)
    starship_data = PyStarships(**starship_data)
    print(f"\nValidating Starship Data :: \n")
    pprint(starship_data)

    global starship_urls
    starship_urls = starship_obj.get_resource_urls()
    print(f"\nGetting list of all Starship URLs::")
    pprint(starship_urls)
    return starship_urls


def vehicles_data():
    """
    Getting count of Vehicles; Validating Vehicles data; Generates list of all Vehicles
    URLs
    """
    vehicle_obj = RVehicles()
    total_vehicles = vehicle_obj.get_count()
    print(f"\nGetting Vehicles Count :: ", end="")
    pprint(total_vehicles)

    vehicle_data = vehicle_obj.get_sample_data(4)
    vehicle_data = PyVehicles(**vehicle_data)
    print(f"\nValidating Vehicle Data :: \n")
    pprint(vehicle_data)

    global vehicle_urls
    vehicle_urls = vehicle_obj.get_resource_urls()
    print(f"\nGetting list of all Vehicle URLs::")
    pprint(vehicle_urls)
    return vehicle_urls


@timeit
def main_task():
    characters_data()
    films_data()
    planets_data()
    species_data()
    starships_data()
    vehicles_data()


@timeit
def random_data():
    """
    Generates Three random numbers and fetch data for each resource's given by user, default:people
    Returns: List

    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--limit", default=3, type=int)
    parser.add_argument("-s", "--start", default=1, type=int)
    parser.add_argument("-e", "--end", default=8, type=int)
    parser.add_argument(
        "-r",
        "--resource",
        default="people",
        choices=["films", "planets", "people", "starships", "species", "vehicles"],
    )
    argument = parser.parse_args()
    print(f"\nPassed arguments are -> {argument}")

    obj = ProduceNumbers(argument.start, argument.end, argument.limit)

    random_resources_numbers = [element for element in obj]

    for number in random_resources_numbers:
        if argument.resource == "films":
            print(f"\nGenerating the data for {argument.resource} id :-> {number}\n")
            # response_url = get_url(character_urls[item], argument.resource)
            data = hit_url(film_urls[number])
            data = data.json()
            pprint(data)

        if argument.resource == "planets":
            print(f"\nGenerating the data for {argument.resource} id :-> {number}\n")
            # response_url = get_url(character_urls[item], argument.resource)
            data = hit_url(planet_urls[number])
            data = data.json()
            pprint(data)

        if argument.resource == "species":
            print(f"\nGenerating the data for {argument.resource} id :-> {number}\n")
            # response_url = get_url(character_urls[item], argument.resource)
            data = hit_url(specie_urls[number])
            data = data.json()
            pprint(data)

        if argument.resource == "starships":
            print(f"\nGenerating the data for {argument.resource} id :-> {number}\n")
            # response_url = get_url(character_urls[item], argument.resource)
            data = hit_url(starship_urls[number])
            data = data.json()
            pprint(data)

        if argument.resource == "vehicles":
            print(f"\nGenerating the data for {argument.resource} id :-> {number}\n")
            # response_url = get_url(character_urls[item], argument.resource)
            data = hit_url(vehicle_urls[number])
            data = data.json()
            pprint(data)

        else:
            print(f"\nGenerating the data for {argument.resource} id :-> {number}\n")
            # response_url = get_url(character_urls[item], argument.resource)
            data = hit_url(character_urls[number])
            data = data.json()
            pprint(data)


if __name__ == "__main__":
    main_task()
    random_data()
