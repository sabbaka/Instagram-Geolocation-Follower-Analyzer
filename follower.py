class Follower(object):
    def __init__(self, user_id, owner):
        self.user_id = user_id
        self.owner = owner

    def __repr__(self):
        return "<('%s','%s','%s','%s','%s')>" % (self.user_id, self.longitude, self.latitude, self.country, self.owner)


