from sqlalchemy.orm import mapper

from lib import get_followers
from lib import get_geos
from follower import Follower

from instadb import geo_table
from instadb import Session


session = Session()

mapper(Follower, geo_table)

def test_func():
    for follower in session.query(Follower).order_by(Follower.user_id):
        print follower.__dict__

test_func()

for follower in session.query(Follower).order_by(Follower.user_id):
    # follower.geotag = get_geos(follower.user_id)
    follower.geotag = '1'

session.commit()
