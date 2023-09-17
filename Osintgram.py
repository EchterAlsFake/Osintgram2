"""
Copyright (C) 2023 EchterAlsFake

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or any
later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import contextlib
import instagrapi.exceptions
import wget
import os
import json

from logger import logger
from instagrapi import Client
from colorama import *
from tqdm import tqdm

__version__ = "1.0"
__author__ = "Johannes Habel | EchterAlsFake"


def replace_unencodable_with_space(s, encoding='utf-8'):
    result = []
    for c in s:
        try:
            c.encode(encoding)
            result.append(c)
        except UnicodeEncodeError:
            result.append(' ')
    return ''.join(result)


def create_workspace(target_name):
    folders = ["album", "igtv", "photos", "story", "profile_pic", "location", "photos_captions", "comments",
               "followers", "followings", "followers_email", "followings_email", "followers_number",
               "followings_number",
               "user_info"]
    if not os.path.exists(target_name):
        os.mkdir(target_name)

    for folder in folders:
        if not os.path.exists(f"{target_name}{os.sep}{folder}"):
            os.mkdir(f"{target_name}{os.sep}{folder}")


input("""
Licensed Under GNU General Public License v3 (GPLv3)

Disclaimer:

Usage of this tool is in violation of Instagram's Terms of Service, and could result in the suspension or banning of 
your account. Legal repercussions may also be a possibility, although unlikely. The user assumes all responsibility 
for any consequences arising from the utilization of this tool. I am not liable for any actions taken against your 
account.

This tool is designed to assist cybersecurity analysts and is not intended for unauthorized surveillance or espionage 
activities.

The original concept for a similar tool, named Osintgram, was developed by 'Datalux.' You can find his project here: 
https://github.com/Datalux/Osintgram

By proceeding, you acknowledge that I bear no liability for any repercussions and that you are using this tool entirely 
at your own risk.

Are you prepared to accept the potential consequences?

Press Enter to continue if you are.
""")


class Osintgram:
    """
Tries to be as Osintgram from Datalux, which is sadly dead, because the API is not working properly.
My version of Osintgram uses a really stable API called 'instagrapi'
    """

    def __init__(self):
        self.z = f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET}"
        self.username = None
        self.password = None
        self.logged_in = False
        self.photo_data = []
        self.video_data = []
        self.igtv_data = []
        self.reel_data = []
        self.album_data = []
        self.followers = None
        self.followings = None
        self.stories = []
        self.medias_export = None
        self.target = False
        self.cl = Client()
        while True:
            try:
                self.menu()

            except KeyboardInterrupt:
                exit(0)

            except instagrapi.exceptions.LoginRequired:
                logger("Instagram wants you to login. Please change your IP or Login to continue", level=1)

            except instagrapi.exceptions.ChallengeRequired:
                logger("You need to solve a challenge. Go to instagram.com to do this!", level=1)

            except instagrapi.exceptions.UserNotFound:
                logger("The user was not found. Try again", level=1)

            except instagrapi.exceptions.PrivateAccount:
                logger("The User's account is private. You need to log in and follow the account in order to retrieve "
                       "information", level=1)

            except instagrapi.exceptions.PleaseWaitFewMinutes:
                logger("Timed out by instagram. Please wait a few minutes, change IP and try again!", level=1)

    def menu(self):

        options_map = {
            "0": "login",
            "1": "get_location",
            "2": "get_photos_captions",
            "3": "get_comments",
            "4": "get_followers",
            "5": "get_followings",
            "6": lambda: self.get_email(mode="6"),
            "7": lambda: self.get_email(mode="7"),
            "8": lambda: self.get_number(mode="8"),
            "9": lambda: self.get_number(mode="9"),
            "10": "get_info",
            "11": "get_likes",
            "12": "get_media_type",
            "13": "download_photos",
            "14": "download_propic",
            "15": "download_stories",
            "16": "download_album",
            "17": "get_igtv",
            "18": "exit"
        }

        options = input(f"""{Fore.LIGHTWHITE_EX}
T) Set Target
0) - Login             Needed for private account's you are following to
1) - addrs           Get all registered addressed by target photos
2) - captions        Get user's photos captions
3) - comments        Get total comments of target's posts
4) - followers       Get target followers
5) - followings      Get users followed by target
6) - fwersemail      Get email of target followers
7) - fwingsemail     Get email of users followed by target
8) - fwersnumber     Get phone number of target followers
9) - fwingsnumber    Get phone number of users followed by target
10) - info            Get target info
11) - likes           Get total likes of target's posts
12) - mediatype       Get user's posts type (photo or video)
13) - photos          Download user's photos in output folder
14) - propic          Download user's profile picture
15) - stories         Download user's stories
16) - album           Download user's album
17) - igtv            Get user's IGTV
18) - Exit  
-------------------=>:""")
        if options != "T" and options != "18" and options != "0" and not self.target:
            self.get_target()

        elif options == "T":
            self.get_target()

        try:
            method = options_map.get(options, None)
            if method:
                if callable(method):
                    method()
                else:
                    getattr(self, method)()

        except AttributeError:
            exit()

    def get_target(self):
        self.username = input(f"{self.z}{Fore.LIGHTCYAN_EX}Enter target --=>:")
        self.clear_lists()
        target_id = self.get_target_id()
        info = self.cl.user_info(target_id)
        logger(f"{Fore.LIGHTCYAN_EX}Target: {info.full_name}")
        self.target = target_id
        self.get_media_raw()
        create_workspace(self.username)

    def login(self, password_login=False):
        if not os.path.isfile("session.json") or password_login:

            if os.path.exists("session.json"):
                os.remove("session.json")

            logger("There is no session.json file. Logging in with username and password...")
            self.username = input(f"{self.z}{Fore.LIGHTCYAN_EX}Enter username --=>:")
            self.password = input(f"{self.z}{Fore.LIGHTCYAN_EX}Enter password --=>:")

            try:
                self.cl.login(self.username, self.password)
                self.logged_in = True
                logger(f"{Fore.LIGHTGREEN_EX}Login successful!")
                session_id = self.cl.sessionid
                session_data = {
                    "session_id": session_id}

                with open("session.json", "w") as file:
                    json.dump(session_data, file)

                logger("Saved Session ID")

            except instagrapi.exceptions.BadPassword or instagrapi.exceptions.BadCredentials:
                logger(f"{Fore.LIGHTWHITE_EX}Wrong credentials. Please try again.", level=1)
                self.login(password_login=True)

        else:
            with open("session.json", "r") as file:
                session_data = json.load(file)

            session_id_value = session_data["session_id"]
            logger(f"{Fore.LIGHTGREEN_EX}Found Session ID: {session_id_value}:")

            try:
                self.cl.login_by_sessionid(session_id_value)
                self.logged_in = True
                logger(f"{Fore.LIGHTGREEN_EX}Login successful!  Session ID: {self.cl.sessionid}")

            except instagrapi.exceptions:
                logger("Session ID is out of date. Recreating new session ID...", level=1)
                self.login(password_login=True)

    def get_target_id(self):
        return self.cl.user_id_from_username(self.username)

    def get_media_raw(self):
        logger(f"Retrieving media objects for: {self.target}")
        medias = self.cl.user_medias_v1(user_id=self.get_target_id())
        self.medias_export = medias
        logger(f"Found {len(medias)} media files{Fore.RESET}")
        for media in medias:
            if media.media_type == 1:
                self.photo_data.append(media)

            elif media.media_type == 2 and media.product_type == "feed":
                self.video_data.append(media)

            elif media.media_type == 2 and media.product_type == "igtv":
                self.igtv_data.append(media)

            elif media.media_type == 2 and media.product_type == "clips":
                self.reel_data.append(media)

            elif media.media_type == 8:
                self.album_data.append(media)

    def clear_lists(self):
        self.video_data = []
        self.reel_data = []
        self.album_data = []
        self.igtv_data = []
        self.photo_data = []
        self.followers = None
        self.followings = None

    def get_location(self):

        medias = self.photo_data + self.igtv_data + self.album_data + self.reel_data + self.stories

        latitudes = []
        longitudes = []

        with open(f"{self.username}{os.sep}location{os.sep}location_data.txt", "a") as location_file:
            for media in medias:
                with contextlib.suppress(AttributeError):
                    latitudes.append(media.location.lat)
                    longitudes.append(media.location.lng)
                    data = f"Latitude:  {media.location.lat} : Longitude: {media.location.lng}"
                    location_file.write(f"{data}\n")

            if len(latitudes) and len(longitudes) == 0:
                logger(f"{Fore.LIGHTYELLOW_EX} No location data found. Sorry.")

    def download_album(self):
        for item in tqdm(self.album_data):
            self.cl.album_download(item.pk, folder=f"{self.username}{os.sep}album{os.sep}")

        logger("Finished downloading :)")

    def get_photos_captions(self):
        if len(self.photo_data) == 0 or self.photo_data is None:
            logger(msg="Target has no photos...", level=1)
            self.menu()

        else:
            with open(f"{self.username}{os.sep}photos_captions.txt", "w") as caption_file:
                for media in self.photo_data:
                    data = f"""
Media ID: {media.id}
Caption: {media.caption_text}"""

                    print(data)
                    caption_file.write(f"{data}\n")

        input(f"{Fore.LIGHTYELLOW_EX}Press ENTER to continue...")

    def get_comments(self):
        data = self.photo_data + self.igtv_data + self.reel_data + self.video_data + self.album_data
        media_ids = [item.id for item in data]

        with open(f"{self.username}{os.sep}comments{os.sep}comments.txt") as comments_file:
            for id in media_ids:
                comments = self.cl.media_comments(media_id=id)
                logger(f"{Fore.LIGHTGREEN_EX}Found {len(comments)} comments in Media: {id}")
                for comment in comments:
                    text = comment.text
                    created = comment.created_at_utc
                    likes = comment.like_count
                    user = comment.user.username
                    data = (f"""
    User: {user}
    Commented at: {created}
    Likes: {likes}
    Text: {text}""")
                    logger(data)
                    comments_file.write(f"{data}\n")

    def get_followers(self):
        user_id = self.get_target_id()
        amount = input(f"{Fore.LIGHTYELLOW_EX}Enter amount of followings you want to get  (0 for all) --=>:")
        followings = self.cl.user_followers_v1(user_id, amount=int(amount))
        for counter, follower in enumerate(followings):
            logger(f"{counter}) Username: {follower.username}")

    def get_followings(self):
        user_id = self.get_target_id()
        amount = input(f"{self.z}{Fore.LIGHTYELLOW_EX}Enter amount of followings you want to get  (0 for all) --=>:")
        followings = self.cl.user_following_v1(user_id, amount=int(amount))
        for counter, follower in enumerate(followings):
            logger(f"{counter}) Username: {follower.username}")

    def get_email(self, mode):
        amount = input(
            f"{self.z}{Fore.LIGHTYELLOW_EX}For how much followers / following you want to get emails for (0 for all)--=>:")
        user_id = self.get_target_id()
        if mode == "6":
            followers = self.cl.user_followers(user_id, amount=int(amount))
            open("")
        elif mode == "7":
            followers = self.cl.user_following(user_id, amount=int(amount))

        emails = []
        user_names = []
        valid_users = []

        for follower in tqdm(followers):
            user_names.append(follower.username)
            logger(f"{Fore.LIGHTMAGENTA_EX} Appended: {follower.username}")

        for username in tqdm(user_names):
            try:
                email = self.cl.user_info_by_username(username)
                if email.public_email is not None:
                    emails.append(email.public_email)
                    valid_users.append(email.username)

            except AttributeError:
                pass

        with open(f"{self.username}{os.sep}followers_email{os.sep}emails.txt", "w") as emails_file:
            if len(emails) == 0:
                logger(msg="Sorry, but none of the users have a public email address :(", level=1)

            else:
                for counter, email in enumerate(emails):
                    data = f"{counter}) User: {user_names[counter]} Email: {email}"
                    logger(data)
                    emails_file.write(f"{data}\n")

    def get_number(self, mode):
        if mode == "8":
            followers = self.followers

        elif mode == "9":
            followers = self.followings

        valid_users = []
        numbers = []
        codes = []

        usernames = [follower.username for follower in followers]
        for username in usernames:
            user_info = self.cl.user_info(user_id=self.cl.user_id_from_username(username))

            if user_info.public_phone_country_code is not None:
                codes.append(user_info.public_phone_country_code)
                if username not in valid_users:
                    valid_users.append(username)

            if user_info.public_phone_number is not None:
                numbers.append(user_info.public_phone_number)
                if username not in valid_users:
                    valid_users.append(username)

        with open(f"{self.username}{os.sep}followers_number{os.sep}numbers.txt", "w") as followers_number_file:
            for counter, user in enumerate(valid_users):
                data = f"{Fore.LIGHTCYAN_EX}{counter}) Found Number {numbers[counter]} with Code: {codes[counter]} for User: {user}"
                logger(data)
                followers_number_file.write(f"{data}\n")

    def get_igtv(self):
        if len(self.igtv_data) == 0 or self.igtv_data is None:
            logger("User has not IGTV data", level=1)

        else:
            for item in tqdm(self.igtv_data):
                pk = item.pk
                self.cl.igtv_download(pk, folder=f"{self.username}{os.sep}igtv{os.sep}")

    def get_info(self):

        id = self.get_target_id()
        info = self.cl.user_info(id)

        full_name = info.full_name
        latitude = info.latitude
        longitude = info.longitude
        contact_phone = info.contact_phone_number
        business_contact_method = info.business_contact_method
        business_category_name = info.business_category_name
        public_phone_number = info.public_phone_number
        public_country_code = info.public_phone_country_code
        public_email = info.public_email
        category = info.category
        account_type = info.account_type
        address_steet = info.address_street
        biography = info.biography
        city_id = info.city_id
        city_name = info.city_name
        external_url = info.external_url
        follower_count = info.follower_count
        following_count = info.following_count
        profile_pic = info.profile_pic_url_hd
        pk = info.pk
        zip = info.zip
        media = info.media_count
        text = f"""
-----------------Information for {full_name}--------------------------------------
If something has 'None' as answer, it means, that there's no information about it.
----------------------------------------------------------------------------------

Full Name: {full_name}
Biography: {biography}
Follower Count: {follower_count}
Following Count: {following_count}
Latitude: {latitude}
Longitude: {longitude}
Contact Phone: {contact_phone}
Business contact method: {business_contact_method}
Business category name: {business_category_name}
Public Phone Number: {public_phone_number}
Public Phone country code: {public_country_code}
Public E-Mail: {public_email}
Category: {category}
Account type: {account_type}
Address street: {address_steet}
City ID: {city_id}
City Name: {city_name}
External URL: {external_url}
Profile Picture: {profile_pic}
PK: {pk}
ZIP: {zip}
Total Media: {media}
"""
        filtered_text = replace_unencodable_with_space(text)
        logger(filtered_text)
        with open(f"{self.username}{os.sep}user_info{os.sep}user_info.txt", "w") as user_info:
            user_info.write(filtered_text)

    def get_likes(self):
        likes = 0

        x = self.cl.user_medias_v1(user_id=self.get_target_id())
        for item in x:
            like_count = item.like_count
            like_count = int(like_count)
            likes += like_count

        logger(f"Total Likes: {likes}")

    def get_media_type(self):

        photos = len(self.photo_data)
        reels = len(self.reel_data)
        igtv = len(self.igtv_data)
        video = len(self.video_data)
        album = len(self.album_data)

        logger(f"""
    
Photos: {photos}
Reels:  {reels}
IGTV:   {igtv}
Video:  {video}
Album:  {album}""")

    def download_photos(self):
        for photo in tqdm(self.photo_data):
            pk = photo.pk
            self.cl.photo_download(pk, folder=f"{self.username}{os.sep}photos{os.sep}")

    def download_propic(self):
        user_id = self.get_target_id()
        user_info = self.cl.user_info_v1(user_id)
        picture = user_info.profile_pic_url_hd
        wget.download(picture, out=f"{self.username}{os.sep}profile_pic{os.sep}")
        logger(f"Downloaded profile picture!")

    def download_stories(self):
        amount = input(
            f"{self.z}{Fore.LIGHTYELLOW_EX}Enter the amount of stories you want to download (0 for all) --=>:")
        stories = self.cl.user_stories(user_id=self.get_target_id(), amount=int(amount))

        for story in stories:
            self.stories.append(story.pk)

        for pk in tqdm(self.stories):
            self.cl.story_download(pk, folder=f"{self.username}{os.sep}stories{os.sep}")

        logger(f"Downloaded {len(stories)} stories")


if __name__ == "__main__":
    Osintgram()
