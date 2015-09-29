from sqlalchemy.orm import mapper

from lib import get_followers
from lib import get_geos
from follower import Follower

from instadb import geo_table
from instadb import Session


session = Session()

followed_by = get_followers('1921850126')

mapper(Follower, geo_table)
# fill db with followers, step 1
for follower in followed_by:
    print follower.id
    session.add(Follower(user_id=follower.id))

session.commit()

#TODO fill DB with GEOS
# get_geos_for_followers(followed_by)

# for follower in session.query(Follower).order_by(Follower.user_id):
#     follower.geotag = get_geos(follower.user_id)

