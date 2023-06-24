
from instagrapi import Client

email = ""
deine_mutter = ""

cl = Client()
cl.login(email, deine_mutter)

id = cl.user_id_from_username("oisrzr")
medias = cl.user_medias(id)

for media in medias:
    print(media.location)