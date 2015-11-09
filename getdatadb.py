from lib import get_followers
from lib import get_geos
from follower import Follower

from instadb import geo_table
from instadb import Session
from geopy.geocoders import Nominatim
from sqlalchemy import func


def followers_from_db():
    session = Session()
    return session.query(Follower).order_by(Follower.user_id)


def test_func():
    session = Session()
    for follower in session.query(Follower).all():
        print follower


def with_country():
    session = Session()
    for follower in session.query(Follower).filter(Follower.country != None).all():
        print follower.country
    count = session.query(Follower.country, func.count(Follower.country)).group_by(Follower.country).all()
    for el in count:
        print el[0], el[1]


def load_geos_test():
    session = Session()
    for follower in session.query(Follower).order_by(Follower.user_id):
        follower.geotag = get_geos(follower.user_id)
    session.commit()


def set_country():
    session = Session()
    for follower in session.query(Follower).order_by(Follower.user_id):
        if hasattr(follower, 'latitude') and hasattr(follower, 'longitude') and follower.country is None:
            country = locate_country(follower.latitude, follower.longitude)
            if country:
                follower.country = country
                session.commit()


def locate_country(latitude, longitude):
    geo_locator = Nominatim()
    location = geo_locator.reverse(query=(latitude, longitude), language='en', timeout=120)
    if location != None:
        try:
            # print location
            return location.raw['address']['country']
        except:
            return False

def locate_country_code(latitude, longitude):
    geo_locator = Nominatim()
    location = geo_locator.reverse(query=(latitude, longitude), language='en', timeout=120)
    if location != None:
        try:
            # print location
            return location.raw['address']['country_code']
        except:
            return False
