import json
from flask import Blueprint, Response

from utils.randgen import ProduceNumbers
from utils.fetch_data import hit_url
from task_three import (
    characters_data,
    films_data,
    planets_data,
    species_data,
    starships_data,
    vehicles_data,
)

v3 = Blueprint("v3", __name__, url_prefix="/v3")


@v3.route("/welcome")
def welcome():
    return "TASK THREE"


@v3.route("/taskthree/<resource>")
def task_three(resource, limit=3, start=0, end=6):
    char_data = []
    film_data = []
    planet_data = []
    specie_data = []
    starship_data = []
    vehicle_data = []

    obj = ProduceNumbers(start, end, limit - 1)

    random_resources_numbers = [element for element in obj]

    for number in random_resources_numbers:
        if resource == "films":
            data = hit_url(films_data()[number])
            data = data.json()
            film_data.append(data)

        if resource == "planets":
            data = hit_url(planets_data()[number])
            data = data.json()
            planet_data.append(data)

        if resource == "species":
            data = hit_url(species_data()[number])
            data = data.json()
            specie_data.append(data)

        if resource == "starships":
            data = hit_url(starships_data()[number])
            data = data.json()
            starship_data.append(data)

        if resource == "vehicles":
            data = hit_url(vehicles_data()[number])
            data = data.json()
            vehicle_data.append(data)

        else:
            data = hit_url(characters_data()[number])
            data = data.json()
            char_data.append(data)

    if resource == "characters":
        char_response = {"count": len(char_data), "characters": char_data}
        return char_response
    if resource == "films":
        films_response = {"count": len(film_data), "films": film_data}
        return films_response
    if resource == "planets":
        planets_response = {"count": len(planet_data), "planets": planet_data}
        return planets_response
    if resource == "species":
        species_response = {"count": len(specie_data), "species": specie_data}
        return species_response
    if resource == "starships":
        starships_response = {"count": len(starship_data), "starships": starship_data}
        return starships_response
    if resource == "vehicles":
        vehicles_response = {"count": len(vehicle_data), "vehicles": vehicle_data}
        return vehicles_response
