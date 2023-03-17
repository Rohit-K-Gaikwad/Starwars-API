import requests
import json

from flask import Flask, Response

from task_one import get_url
from utils.randgen import ProduceNumbers
from utils.fetch_data import hit_url
from task_two import (
    first_film_data,
    characters_data_,
    planets_data_,
    species_data_,
    starships_data_,
    vehicles_data_,
)
from task_three import (
    characters_data,
    films_data,
    planets_data,
    species_data,
    starships_data,
    vehicles_data,
)

app = Flask(__name__)


@app.route("/welcome")
def welcome():
    return "Welcome to SWAPI Project"


@app.route("/taskone/<resource>/<int:count>/<int:start>/<int:end>")
def task_one(resource, count, start, end):
    obj = ProduceNumbers(start, end, count)

    resources = [element for element in obj]
    print(f"resources - {resources}")

    print(
        f"[ INFO ] produced {len(resources)}"
        f" random resource ids in range({start}, {end})."
    )

    data = []
    for resource_id in resources:
        print(f"[ INFO ] fetching data for resource_id {resource_id}...")
        url_ = get_url(resource_id, resource)

        # `requests.get()` returns a HttpResponse
        res = requests.get(url_)
        print(f"res.status_code = {res.status_code}")

        if res.status_code == 200:
            # getting dict value from response object
            result = res.json()

            # capturing name from dict object
            data.append(result.get("name"))

    output = {"count": len(data), "names": data}

    return Response(json.dumps(output), status=201, mimetype="application/json")


@app.route("/tasktwo")
def task_two_welcome():
    first_result = first_film_data()
    return Response(json.dumps(first_result), status=201, mimetype="application/json")


@app.route("/tasktwo/<resource>")
def task_two(resource):
    first_result = first_film_data()

    if resource == "characters":
        char_result = characters_data_(first_result, "characters")
        return Response(
            json.dumps(char_result), status=201, mimetype="application/json"
        )

    if resource == "planets":
        planet_result = planets_data_(first_result, "planets")
        return Response(
            json.dumps(planet_result), status=201, mimetype="application/json"
        )

    if resource == "vehicles":
        vehicle_result = vehicles_data_(first_result, "vehicles")
        return Response(
            json.dumps(vehicle_result), status=201, mimetype="application/json"
        )

    if resource == "species":
        species_result = species_data_(first_result, "species")
        return Response(
            json.dumps(species_result), status=201, mimetype="application/json"
        )

    if resource == "starships":
        starships_result = starships_data_(first_result, "starships")
        return Response(
            json.dumps(starships_result), status=201, mimetype="application/json"
        )


@app.route("/taskthree/<resource>")
def task_three(resource, limit=3, start=1, end=8):
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


if __name__ == "__main__":
    app.run(host="localhost", port=10000, debug=True)
