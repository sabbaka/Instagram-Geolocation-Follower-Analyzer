from follower import Follower
from instadb import Session
from getdatadb import locate_country


session = Session()

counter = 0

def fill_countries():
    for follower in session.query(Follower).all():
        if follower.country is None:
            follower.country = locate_country(follower.latitude, follower.longitude)
            session.commit()
            fill_countries()

fill_countries()
