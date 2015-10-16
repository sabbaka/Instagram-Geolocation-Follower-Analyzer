import multiprocessing as mps
from lib import api
from follower import Follower
from instadb import Session

session = Session()

def parse_follower(follower_info):
    # do some hard work here
    session.add(Follower(user_id=follower_info.id))
    session.commit()
    return follower_info.id


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

    for info in get_followers_info(user_id=1921850126):
        # do something with data which parsed by parse_follower
        print info
