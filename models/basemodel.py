""" Pydantic Model for validation and (de)serialization in API requests/responses."""

from pydantic import BaseModel
from datetime import datetime


class Base(BaseModel):
    """Pydantic models class meant to validate the data for `All resource` object from
    single (https://swapi.dev/api/people/) resource endpoint from starwars API particularly
    for `url`,`created`,`edited`.
    """

    url: str
    created: datetime
    edited: datetime


if __name__ == "__main__":
    data = {
        "created": "2014-12-10T16:36:50.509000Z",
        "edited": "2014-12-10T16:36:50.509000Z",
        "url": "https://swapi.dev/api/people/1",
    }

    obj = Base(**data)
