from instagram_private_api import Client, ClientCompatPatch, ClientError, ClientLoginError
from settings import inst_username, inst_password

import hashlib
import string
import random
import datetime




# user_name = inst_username
# password = inst_password
#
# api = Client(username=user_name, password=password)
# results = api.feed_timeline()
# items = [item for item in results.get('feed_items', [])
#          if item.get('media_or_ad')]
#
# print(api.current_user())

# usernames = []
#
# for item in items:
#     # Manually patch the entity to match the public api as closely as possible, optional
#     # To automatically patch entities, initialise the Client with auto_patch=True
#     ClientCompatPatch.media(item['media_or_ad'])
#     likers = api.media_likers(media_id=item['media_or_ad']['id'])
#     for liker in range(len(likers)):
#         usernames.append(likers['users'][liker]['username'])
#
#
# print(usernames)


def get_media_likers(self, media_id):
    url = "media/{media_id}/likers/?".format(media_id=media_id)
    return self.send_request(url)




