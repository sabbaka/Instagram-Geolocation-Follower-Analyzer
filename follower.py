class Follower(object):
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return "<('%s','%s', '%s')>" % (self.user_id, self.longitude, self.latitude)


