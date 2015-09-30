from sqlalchemy.orm import mapper

from lib import get_followers
from lib import get_geos
from follower import Follower

from instadb import geo_table
from instadb import Session


session = Session()

followed_by = get_followers('1921850126')

# mapper(Follower, geo_table)
# fill db with followers, step 1
for follower in followed_by:
    print follower.id
    session.add(Follower(user_id=follower.id))
session.commit()

#TODO fill DB with GEOS
# get_geos_for_followers(followed_by)

for follower in session.query(Follower).order_by(Follower.user_id):
    location = get_geos(follower.user_id)
    # if hasattr(location, 'id'):
    #     follower.location_id = location.id
    if hasattr(location, 'point'):
        if(location.point != None):
            follower.latitude = location.point.latitude
            follower.longitude = location.point.longitude
            session.commit()
