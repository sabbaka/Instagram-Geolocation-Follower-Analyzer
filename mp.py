import multiprocessing as mp
from follower import Follower
from instadb import Session
from lib import api


session = Session()


def get_followers(user_id):
    followed_by, next_ = api.user_followed_by(user_id=user_id)
    while next_:
        more_followed_by, next_ = api.user_followed_by(user_id=user_id, with_next_url=next_)
        followed_by.extend(more_followed_by)
    for follower in followed_by:
        session.add(Follower(user_id=follower.id))
        session.commit()


# followed_by = get_followers('1921850126')


def worker_func(x):
    return x * x


# def iter_followers():
#     next_ = True
#     while next_:
#         more_followed_by, next_ = api.user_followed_by(user_id=user_id, with_next_url=next_)
#     for follower in more_followed_by:
#         session.add(Follower(user_id=follower.id))
#         session.commit()
#
#     while ne
#     followed_by, next_ = api.user_followed_by(user_id=user_id)



def get_followers_by_pool():
    workers_pool = mp.Pool(processes=5)

    # task_data = xrange(1,500000)

    for result in workers_pool.imap_unordered(worker_func, task_data):
        followed_by
        yield result

    workers_pool.close()
    return
