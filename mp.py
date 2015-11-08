import multiprocessing as mps
from instagram.client import InstagramAPI
from lib import api
from follower import Follower
from instadb import Session
from lib import get_geos
import sys
from random import randint


apis = [InstagramAPI(client_id='bc3f22e5807c4e5aa9e1c9e5bf391f77', client_secret='4f88a95213ae4e57a70f318b7f6ac81c'),
       InstagramAPI(client_id='ade077a508f241b599aa55d924730a10', client_secret='85a2c94c85d844b79d39e86e7d8d84a7')]

api = apis[randint(0, len(apis) - 1)]

print api

session = Session()

def parse_follower(follower_info):
    flw = session.query(Follower).filter(Follower.user_id==follower_info.id, Follower.owner == sys.argv[-1]).first()
    if flw is None:
        location = get_geos(follower_info.id)
        if hasattr(location, 'point'):
            if(location.point != None):
                # follower_info.country = location.point.latitude
                follower_info.latitude = location.point.latitude
                follower_info.longitude = location.point.longitude
                # follower_info.country = locate_country(follower_info.latitude, follower_info.longitude)
                # follower_info.country = locate_country(location.point.latitude, location.point.longitude)
                return follower_info
    return False


def followers_iter(user_id):
    more_followed_by, next_ = api.user_followed_by(user_id=user_id)

    while next_:
        for follower in more_followed_by:
            yield follower

        more_followed_by, next_ = api.user_followed_by(user_id=user_id, with_next_url=next_)

    return


def get_followers_info(user_id):

    workers_pool = mps.Pool()

    for follower_info in workers_pool.imap_unordered(parse_follower, followers_iter(user_id)):
        yield follower_info

    workers_pool.close()
    return


if __name__ == "__main__":
    if len(sys.argv) >= 1:
        # for info in get_followers_info(user_id=1921850126):
        for info in get_followers_info(user_id=sys.argv[-1]):
            if info is not False:
                # do something with data which parsed by parse_follower
                flw = Follower(user_id=info.id, owner=sys.argv[-1])
                flw.latitude = info.latitude
                flw.longitude = info.longitude
                # flw.country = info.country
                # session.add(Follower(user_id=info.id,country=info.country))
                # session.commit()
                session.add(flw)
                session.commit()
                execfile("lcountry.py")
                print info
