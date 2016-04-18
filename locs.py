from instagram.client import InstagramAPI

api = InstagramAPI(client_id='ade077a508f241b599aa55d924730a10', client_secret='85a2c94c85d844b79d39e86e7d8d84a7')

from itertools import product
import numpy as np

coordinates = list(product(np.arange(50.40,50.47,0.005), np.arange(30.47,30.60,0.001)))

print coordinates

users = set()

for coord in coordinates:
    try:
        locations_list = api.location_search(lat=coord[0],lng=coord[1])
        for location in locations_list:
            medias = api.location_recent_media(location_id=location.id)[0]
            for media in medias:
                print media.user
    except:
        pass