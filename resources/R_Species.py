from resources.base import ResourceBase
from utils.fetch_data import hit_url


class RSpecies(ResourceBase):
    """
    Species class related functionality
    """

    def __init__(self):
        super().__init__()
        self.relative_url = "/api/species/"

    def get_count(self):
        complete_url = self.home_url + self.relative_url
        response = hit_url(complete_url)
        res_data = response.json()
        count = res_data.get("count")
        return count

    def get_resource_urls(self):
        urls = []
        i = 0
        url = self.home_url + self.relative_url
        response = hit_url(url)
        res_data = response.json()
        foo = res_data.get("results")
        while i < len(foo):
            urls.append(foo[i]["url"])
            i += 1
        return urls

    def get_sample_data(self, id_=1):
        absolute_url = self.home_url + self.relative_url + f"{id_}"
        response = hit_url(absolute_url)
        res_data = response.json()
        return res_data
