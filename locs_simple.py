from instagram.client import InstagramAPI
import pickle

api = InstagramAPI(client_id='ade077a508f241b599aa55d924730a10', client_secret='85a2c94c85d844b79d39e86e7d8d84a7')


def locs_parse_(lat=50.45127, lng=30.51346):
    locations = set()
    for loc in api.location_search(lat=lat, lng=lng):
        locations.add(loc)
    locations_ = set()
    for loc in locations:
        for loc in api.location_search(lat=loc.point.latitude, lng=loc.point.longitude):
            print len(locations_)
            locations_.add(loc)
    final_locations = locations | locations_
    print len(final_locations)
    f = open('kiev_locs.txt', 'w')
    pickle.dump(final_locations, f)
    return final_locations

def search_people(locations):
    users = set()
    for location in locations:
        try:
            medias = api.location_recent_media(location_id=location.id)[0]
            for media in medias:
                print media.user
                users.add(media.user)
                print len(users)
        except:
            pass
    f = open('kiev_users.txt', 'w')
    pickle.dump(users, f)
    return users


# def locs_parse():
#     locations = set()
#     users = set()
#     locs = api.location_search(lat=42.15, lng=24.75)
#     print len(locs)
#     for loc in locs:
#         print loc
#         locations.add(loc)
#     for location in locations:
#         try:
#             medias = api.location_recent_media(location_id=location.id)[0]
#             for media in medias:
#                 print media.user
#                 users.add(media.user)
#         except:
#             pass
#     print len(users)
#     print users
#     locations_2 = set()
#     for loc in locations:
#         locations_2 = api.location_search(lat=locations[0].loc.point.latitude, lng=locations[0].loc.point.longitude)
#         break
#     for location in locations_2:
#         try:
#             medias = api.location_recent_media(location_id=location.id)[0]
#             for media in medias:
#                 print media.user
#                 users.add(media.user)
#         except:
#             pass
#     print len(users)
#     print users
#     return users

if __name__ == "__main__":
    locs_parse_()
    search_people(pickle.load(open('kiev_locs.txt', 'r')))

# locs_parse_()


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