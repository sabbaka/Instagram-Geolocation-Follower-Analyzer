from instagram.client import InstagramAPI

api = InstagramAPI(client_id='ade077a508f241b599aa55d924730a10', client_secret='85a2c94c85d844b79d39e86e7d8d84a7')


def locs_parse_():
    locations = set()
    users = set()
    locs = api.location_search(lat=42.15, lng=24.75)
    for loc in locs:
        print loc
        locations.add(loc)
        # locs.extend(api.location_search(lat=loc.point.latitude, lng=loc.point.longitude))
        # if len(locations) == 20:
        #     break
    return locations


def locs_parse():
    locations = set()
    users = set()
    locs = api.location_search(lat=42.15, lng=24.75)
    while len(locations) < 10:
        for loc in locs:
            print loc
            locations.add(loc)
    for location in locations:
        try:
            medias = api.location_recent_media(location_id=location.id)[0]
            for media in medias:
                print media.user
                users.add(media.user)
        except:
            pass
    print len(users)
    print users
    return users

locs_parse()


# print coord.locs_search()

# for coord in coordinates:
#     try:
#         locations_list = api.location_search(lat=coord[0],lng=coord[1])
#         for location in locations_list:
#             medias = api.location_recent_media(location_id=location.id)[0]
#             for media in medias:
#                 print media.user
#     except:
#         pass