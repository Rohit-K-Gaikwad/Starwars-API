"""
    This module defines pydantic (provides Py3 data-classes validation out of the box) models used
    for validation and (de)serialization in API requests/responses.
"""

from typing import Optional, List
from models.basemodel import Base


class PyStarships(Base):
    """
        Pydantic models class meant to validate the data for `Starship` object from single resource
        endpoint (https://swapi.dev/api/starships/) from starwars API.
    """
    # attribute fields
    name: str
    model: str
    manufacturer: str
    cost_in_credits: str
    length: str
    max_atmosphering_speed: str
    crew: str
    passengers: str
    cargo_capacity: str
    consumables: str
    hyperdrive_rating: str
    MGLT: str
    starship_class: str

    # relationship fields
    pilots: Optional[List[str]]
    films: Optional[List[str]]


if __name__ == "__main__":

    data = {"name": "CR90 corvette",
            "model": "CR90 corvette",
            "manufacturer": "Corellian Engineering Corporation",
            "cost_in_credits": "3500000",
            "length": "150",
            "max_atmosphering_speed": "950",
            "crew": "30-165",
            "passengers": "600",
            "cargo_capacity": "3000000",
            "consumables": "1 year",
            "hyperdrive_rating": "2.0",
            "MGLT": "60",
            "starship_class": "corvette",
            "pilots": [],
            "films": [
                    "https://swapi.dev/api/films/1/",
                    "https://swapi.dev/api/films/3/",
                    "https://swapi.dev/api/films/6/"
                        ],
            "created": "2014-12-10T14:20:33.369000Z",
            "edited": "2014-12-20T21:23:49.867000Z",
            "url": "https://swapi.dev/api/starships/2/"
            }

    obj = PyStarships(**data)
    print(obj)
