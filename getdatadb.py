from lib import get_followers
from lib import get_geos
from follower import Follower

from instadb import geo_table
from instadb import Session
from geopy.geocoders import Nominatim


def followers_from_db():
    session = Session()
    return session.query(Follower).order_by(Follower.user_id)


def test_func():
    session = Session()
    for follower in session.query(Follower).all():
        print follower


def load_geos_test():
    session = Session()
    for follower in session.query(Follower).order_by(Follower.user_id):
        follower.geotag = get_geos(follower.user_id)
    session.commit()


def locate_country(latitude, longitude):
    geo_locator = Nominatim()
    location = geo_locator.reverse(query=(latitude, longitude), language='en')
    if location != None:
        return location.raw['address']['country']
