import requests
import json
from flask import Blueprint, Response
from task_one import get_url
from utils.randgen import ProduceNumbers


v1 = Blueprint("v1", __name__, url_prefix="/v1")


@v1.get("/welcome")
def welcome():
    return "WELCOME"


@v1.get("/taskone/<resource>/<int:count>/<int:start>/<int:end>")
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
