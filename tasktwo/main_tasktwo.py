import json
from flask import Blueprint, Response
from task_two import (
    first_film_data,
    characters_data_,
    planets_data_,
    species_data_,
    starships_data_,
    vehicles_data_,
)


v2 = Blueprint("v2", __name__, url_prefix="/v2")


@v2.get("/tasktwo")
def task_two_welcome():
    first_result = first_film_data()
    return Response(json.dumps(first_result), status=201, mimetype="application/json")


@v2.route("/tasktwo/<resource>")
def task_two(resource):
    first_result = first_film_data()

    if resource == "characters":
        char_result = characters_data_(first_result, "characters")
        return Response(json.dumps(char_result), status=201, mimetype="application/json")

    if resource == "planets":
        planet_result = planets_data_(first_result, "planets")
        return Response(json.dumps(planet_result), status=201, mimetype="application/json")

    if resource == "vehicles":
        vehicle_result = vehicles_data_(first_result, "vehicles")
        return Response(json.dumps(vehicle_result), status=201, mimetype="application/json")

    if resource == "species":
        species_result = species_data_(first_result, "species")
        return Response(json.dumps(species_result), status=201, mimetype="application/json")

    if resource == "starships":
        starships_result = starships_data_(first_result, "starships")
        return Response(json.dumps(starships_result), status=201, mimetype="application/json")
