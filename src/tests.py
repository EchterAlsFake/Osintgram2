
from instagrapi import Client


cl = Client()
cl.login("", "")
c  =cl.user_followers_v1()
usernames = []

for follower in c:
    usernames.append(follower.username)

for username in usernames:

    info = cl.user_info_by_username(username)
    info.public_email
