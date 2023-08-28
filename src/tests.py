
from instagrapi import Client

email = "echteralsfake4"
deine_mutter = input("Password:")

cl = Client()
cl.login(email, deine_mutter)

media_url = "https://www.instagram.com/p/Cv9aF8wAEHI/"

file = cl.photo_download_by_url_origin(media_url)

with open("fortnite.jpg", "w") as f:
    f.close()


with open("fortnite.jpg", "wb") as f:
    f.write(file)
