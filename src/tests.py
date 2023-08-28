
from instagrapi import Client

email = "echteralsfake4"
deine_mutter = input("Password:")

cl = Client()
cl.login(email, deine_mutter)

media_url = "https://www.instagram.com/p/Cwa3jEGguAX/"
media_pk = cl.media_pk_from_url(media_url)
story_pk = cl.story_pk_from_url("https://www.instagram.com/stories/nadyadorofeeva/3178875165663678569/")

"""
Photo download test:
"""

# cl.photo_download(media_pk) # Passed

"""
Video download test:

Info for myself:

It seems like for the API reels and videos are the same.
So if I download a reel with the download_video method it still works."""

# cl.video_download(media_pk) # Passed

cl.story_download(story_pk=story_pk)