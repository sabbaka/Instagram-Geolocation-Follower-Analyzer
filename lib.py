from instagram.client import InstagramAPI
from instagram.bind import InstagramAPIError


api = InstagramAPI(client_id='bc3f22e5807c4e5aa9e1c9e5bf391f77', client_secret='4f88a95213ae4e57a70f318b7f6ac81c')

def get_popular_media():
    print api.media_popular(count=20)


def get_followers(user_id):
    followed_by, next_ = api.user_followed_by(user_id=user_id)
    while next_:
        more_followed_by, next_ = api.user_followed_by(user_id=user_id, with_next_url=next_)
        followed_by.extend(more_followed_by)
    return followed_by


def get_geos_for_followers(followed_by):
    for key in followed_by:
        try:
            recent_media, next_ = api.user_recent_media(user_id=key.id,count='10')
            for media in recent_media:
                if hasattr(media, 'location'):
                    print key.username
                    print key.id
                    print media.location
                    return media.location
        except InstagramAPIError as e:
           if (e.status_code == 400):
              print "User is set to private."
              return "User is set to private."


def get_geos(user_id):
    try:
        recent_media, next_ = api.user_recent_media(user_id=user_id,count='10')
        print recent_media
        for media in recent_media:
            if hasattr(media, 'location'):
                print media.location
                return media.location
    except InstagramAPIError as e:
       if (e.status_code == 400):
          print "User is set to private."
          return "User is set to private."
