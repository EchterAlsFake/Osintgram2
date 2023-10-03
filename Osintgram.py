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
import argparse

from logger import logger
from instagrapi import Client
from colorama import *
from tqdm import tqdm
from hue_shift import return_color, reset

__version__ = "1.1"
__author__ = "Johannes Habel | EchterAlsFake"
__license__ = "GPL v3"
__source__ = "https://github.com/EchterAlsFake/Osintgram2"



def replace_unencodable_with_space(s, encoding='utf-8'):
    result = []
    for c in s:
        try:
            c.encode(encoding)
            result.append(c)
        except UnicodeEncodeError:
            result.append(' ')
    return ''.join(result)


def create_workspace(target_name, hashtag_name=False):
    folders = ["album", "igtv", "photos", "story", "profile_pic", "location", "photos_captions", "comments",
               "followers", "followings", "followers_email", "followings_email", "followers_number",
               "followings_number",
               "user_info"]

    if not os.path.exists(target_name):
        os.mkdir(target_name)

    for folder in folders:
        if not os.path.exists(f"{target_name}{os.sep}{folder}"):
            os.mkdir(f"{target_name}{os.sep}{folder}")


def proceed():
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

            except instagrapi.exceptions.LoginRequired as e:
                logger(f"Instagram wants you to login. Please change your IP or Login to continue : {e}", level=1)

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
            "18": "get_hashtags_media",
            "19": "search_hashtags",
            "20": "exit()"
        }

        options = input(f"""{Fore.LIGHTWHITE_EX}
{Fore.LIGHTRED_EX}RED{Fore.LIGHTWHITE_EX}:   Needs Login
{Fore.LIGHTGREEN_EX}GREEN{Fore.LIGHTWHITE_EX}: Works with private accounts you don't follow
{return_color()}Note: Most features for Private accounts need a log in and you need to follow them!{reset()}

{return_color()}T) Set Target{reset()}
0) - {return_color()}Login{reset()}             Needed for private account's you are following to
1) - {return_color()}addrs{reset()}             Get all registered addressed by target photos
2) - {return_color()}captions{reset()}          Get user's photos captions
3) - {return_color()}comments{reset()}          Get total comments of target's posts
4) - {return_color()}followers{reset()}         Get target followers
5) - {return_color()}followings{reset()}        Get users followed by target
6) - {return_color()}fwersemail{reset()}        Get email of target followers
7) - {return_color()}fwingsemail{reset()}       Get email of users followed by target
8) - {return_color()}fwersnumber{reset()}       Get phone number of target followers
9) - {return_color()}fwingsnumber{reset()}      Get phone number of users followed by target
{Fore.LIGHTGREEN_EX}10) - info{reset()}             Get target info
11) - {return_color()}likes{reset()}            Get total likes of target's posts
12) - {return_color()}mediatype{reset()}        Get user's posts type (photo or video)
13) - {return_color()}photos{reset()}           Download user's photos in output folder
{Fore.LIGHTGREEN_EX}14) - propic{reset()}           Download user's profile picture
15) - {return_color()}stories{reset()}          Download user's stories
16) - {return_color()}album{reset()}            Download user's album
17) - {return_color()}igtv{reset()}             Get user's IGTV
{Fore.LIGHTRED_EX}18) - hashtag_media{reset()}    Get all media files from a specific hashtag
19) - {return_color()}hashtag_search{reset()}   Search for hashtags with a search query
{Fore.LIGHTWHITE_EX}20) - Exit{reset()}  
{return_color()}-------------------=>:{reset()}""")

        if (options != "T" and options != "20" and options != "0" and options != "19" and
                options != "18" and options != "14" and options != "10" and not self.target):

            self.get_target()

        elif options == "T":
            self.get_target()

        elif options == "20":
            exit()

        elif options == "14":
            self.download_propic()

        elif options == "10":
            self.get_info()

        method = options_map.get(options, None)
        if method:
            if callable(method):
                method()
            else:
                getattr(self, method)()

    def login(self, password_login=False):
        username = input(f"{return_color()}Username: {reset()}")
        password = input(f"{return_color()}Password: {reset()}")

        if not os.path.isfile("session.json") or password_login:

            if os.path.exists("session.json"):
                os.remove("session.json")

            try:
                self.cl.login(username, password)
                self.logged_in = True
                logger(f"{return_color()}Login Successful!{reset()}")
                session_id = self.cl.sessionid
                session_data = {
                    "session_id": session_id}

                with open("session.json", "w") as file:
                    json.dump(session_data, file)

            except instagrapi.exceptions.BadPassword or instagrapi.exceptions.BadCredentials:
                self.login(password_login=True)

        else:
            with open("session.json", "r") as file:
                session_data = json.load(file)

            session_id_value = session_data["session_id"]
            try:
                self.cl.login_by_sessionid(session_id_value)
                self.logged_in = True
                logger(f"{return_color()}Login Successful!{reset()}")

            except instagrapi.exceptions:
                self.login(password_login=True)

    def get_target(self):
        try:
            self.username = input(f"{self.z}{return_color()}Enter target --=>:{reset()}")
            self.clear_lists()
            target_id = self.get_target_id()
            info = self.cl.user_info(target_id)
            logger(f"{return_color()}Target: {reset()}{info.full_name}")
            self.target = self.username
            self.get_media_raw()
            create_workspace(self.username)

        except instagrapi.exceptions.PrivateAccount or instagrapi.exceptions.PrivateError:
            logger(f"{Fore.LIGHTMAGENTA_EX}User is a private account. Log in to your account and follow him / her",
                   level=1)
            self.get_target()

    def get_target_id(self):
        return self.cl.user_id_from_username(self.username)

    def get_media_raw(self):
        logger(f"Retrieving media objects for: {self.target}")
        medias = self.cl.user_medias_v1(user_id=self.get_target_id())
        self.medias_export = medias
        logger(f"Found {len(medias)} media files{Fore.RESET}")
        data = self.sort_data_types(medias)
        self.photo_data = data[0]
        self.video_data = data[1]
        self.igtv_data = data[2]
        self.reel_data = data[3]
        self.album_data = data[4]

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
                logger(f"{return_color()} No location data found. Sorry.")

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

        input(f"{return_color()}Press ENTER to continue...")

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
{return_color()}User: {user}
{return_color()}Commented at: {created}
{return_color()}Likes: {likes}
{return_color()}Text: {text}""")
                    logger(data)
                    comments_file.write(f"{data}\n")

    def get_followers(self):
        user_id = self.get_target_id()
        amount = input(f"{return_color()}Enter amount of followings you want to get  (0 for all) --=>:")
        followings = self.cl.user_followers_v1(user_id, amount=int(amount))
        for counter, follower in enumerate(followings):
            logger(f"{counter}) Username: {follower.username}")

    def get_followings(self):
        user_id = self.get_target_id()
        amount = input(f"{self.z}{return_color()}Enter amount of followings you want to get  (0 for all) --=>:")
        followings = self.cl.user_following_v1(user_id, amount=int(amount))
        for counter, follower in enumerate(followings):
            logger(f"{counter}) Username: {follower.username}")

    def get_email(self, mode):
        amount = input(
            f"{self.z}{return_color()}For how much followers / following you want to get emails for (0 for all)--=>:")
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
            logger(f"{return_color()} Appended: {follower.username}")

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
                data = f"{return_color()}{counter}) Found Number {numbers[counter]} with Code: {codes[counter]} for User: {user}"
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
        if not self.target:
            target = input(f"{return_color()}Enter Target  (Private verification will be skipped. Do not report errors here!) -->:")
            info = self.cl.user_info_by_username(target)
            write_data = False

        else:
            id = self.get_target_id()
            info = self.cl.user_info(id)
            write_data = True

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

{return_color()}Full Name: {full_name}
{return_color()}Biography: {biography}
{return_color()}Follower Count: {follower_count}
{return_color()}Following Count: {following_count}
{return_color()}Latitude: {latitude}
{return_color()}Longitude: {longitude}
{return_color()}Contact Phone: {contact_phone}
{return_color()}Business contact method: {business_contact_method}
{return_color()}Business category name: {business_category_name}
{return_color()}Public Phone Number: {public_phone_number}
{return_color()}Public Phone country code: {public_country_code}
{return_color()}Public E-Mail: {public_email}
{return_color()}Category: {category}
{return_color()}Account type: {account_type}
{return_color()}Address street: {address_steet}
{return_color()}City ID: {city_id}
{return_color()}City Name: {city_name}
{return_color()}External URL: {external_url}
{return_color()}Profile Picture: {profile_pic}
{return_color()}PK: {pk}
{return_color()}ZIP: {zip}
{return_color()}Total Media: {media}
"""
        filtered_text = replace_unencodable_with_space(text)
        logger(filtered_text)
        if write_data:
            with open(f"{self.username}{os.sep}user_info{os.sep}user_info.txt", "w") as user_info:
                user_info.write(filtered_text)

    def sort_data_types(self, data_packet):

        photo_data = []
        video_data = []
        igtv_data = []
        reel_data = []
        album_data = []


        for item in data_packet:
            if item.media_type == 1:
                photo_data.append(item)

            elif item.media_type == 2 and item.product_type == "feed":
                video_data.append(item)

            elif item.media_type == 2 and item.product_type == "igtv":
                igtv_data.append(item)

            elif item.media_type == 2 and item.product_type == "clips":
                reel_data.append(item)

            elif item.media_type == 8:
                album_data.append(item)

        return [photo_data, video_data, igtv_data, reel_data, album_data]

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
    
{return_color()}Photos: {photos}
{return_color()}Reels:  {reels}
{return_color()}IGTV:   {igtv}
{return_color()}Video:  {video}
{return_color()}Album:  {album}""")

    def download_photos(self):
        for photo in tqdm(self.photo_data):
            pk = photo.pk
            self.cl.photo_download(pk, folder=f"{self.username}{os.sep}photos{os.sep}")

    def download_propic(self):
        if not self.target:
            target = input(f"{return_color()}Enter Target  (Private verification will be skipped. Do not report errors here!) -->:")

        else:
            target = self.target

        user_id = self.cl.user_id_from_username(target)
        user_info = self.cl.user_info(user_id)
        picture = user_info.profile_pic_url_hd
        if self.username is None:
            username = target
            wget.download(picture)

        else:
            wget.download(picture, out=f"{self.username}{os.sep}profile_pic{os.sep}")

        logger(f"Downloaded profile picture!")

    def download_stories(self):
        amount = input(
            f"{self.z}{return_color()}Enter the amount of stories you want to download (0 for all) --=>:")
        stories = self.cl.user_stories(user_id=self.get_target_id(), amount=int(amount))

        for story in stories:
            self.stories.append(story.pk)

        for pk in tqdm(self.stories):
            self.cl.story_download(pk, folder=f"{self.username}{os.sep}stories{os.sep}")

        logger(f"Downloaded {len(stories)} stories")

    def get_hashtags_media(self):
        hashtag = input(f"{self.z}{return_color()}Enter the hashtag without # -->:")
        mode = input(f"""
{return_color()}Pick the sorting:

{return_color()}clips)   Clips hashtag medias
{return_color()}recent)  Recent hashtag medias
{return_color()}top)     Top hashtag medias
{return_color()}------------------=>:""")

        amount = input(f"{self.z}{return_color()}Enter the amount (0 for all) -->:")
        hashtag_object = self.cl.hashtag_medias_v1(name=str(hashtag), tab_key=str(mode), amount=int(amount))
        logger(f"{return_color()}Done")
        data = self.sort_data_types(hashtag_object)
        photo_data = data[0]
        video_data = data[1]
        igtv_data = data[2]
        reel_data = data[3]
        album_data = data[4]

        select_downloads = input(f"""
{return_color()}Select the type of media you want to download:

{return_color()}1) Photos : {len(photo_data)}
{return_color()}2) Videos : {len(video_data)}
{return_color()}3) IGTV   : {len(album_data)}
{return_color()}4) Reels  : {len(reel_data)}
{return_color()}5) Albums : {len(album_data)}
{return_color()}-----------------(separate with comma e.g 1,2,3) --=>:""")

        folders = ["photos", "videos", "igtv", "reels", "albums"]

        if not os.path.exists(hashtag):
            os.mkdir(hashtag)

        for folder in folders:
            if not os.path.exists(f"{hashtag}{os.sep}{folder}"):
                os.mkdir(f"{hashtag}{os.sep}{folder}")

        choices = select_downloads.split(",")
        for choice in choices:
            if choice == "1":
                for photo in tqdm(photo_data):
                    self.cl.photo_download(media_pk=photo.pk, folder=f"{hashtag}{os.sep}photos{os.sep}")

            if choice == "2":
                for video in tqdm(video_data):
                    self.cl.video_download(media_pk=video.pk, folder=f"{hashtag}{os.sep}videos{os.sep}")

            if choice == "3":
                for igtv in tqdm(igtv_data):
                    self.cl.igtv_download(media_pk=igtv.pk, folder=f"{hashtag}{os.sep}igtv{os.sep}")

            if choice == "4":
                for reel in tqdm(reel_data):
                    self.cl.clip_download(media_pk=reel.pk, folder=f"{hashtag}{os.sep}reels{os.sep}")

            if choice == "5":
                for album in tqdm(album_data):
                    self.cl.album_download(media_pk=album.pk, folder=f"{hashtag}{os.sep}albums{os.sep}")


        logger(f"{return_color()}All done :)")

    def search_hashtags(self):
        query = input(f"{self.z}{return_color()}Enter search query --=>:")
        hashtags = self.cl.search_hashtags(query)
        for hashtag in hashtags:
            print(f"""
{return_color()}ID: {hashtag.id}
{return_color()}Name: {hashtag.name}
{return_color()}Media Count: {hashtag.media_count}
{return_color()}----------------------------------""")


def execute():
    try:
        proceed()
        Osintgram()

    except instagrapi.exceptions.PrivateAccount:
        logger("You are trying to access a private account. Please login and follow that person!")

    except instagrapi.exceptions.PleaseWaitFewMinutes:
        logger(
            "Please wait a few minutes, change IP, or Login and try again! This is a restriction from Instagram.")

    except instagrapi.exceptions.ChallengeRequired:
        logger(
            "Instagram wants you to solve a challenge. Please go to https://instagram.com, solve it and try again")

    except instagrapi.exceptions.UserNotFound:
        logger("The User was not found.  Maybe a typo?")

    except instagrapi.exceptions.LoginRequired:
        logger("You must login!  (requested by Instagram)")

    except instagrapi.exceptions.HashtagNotFound:
        logger("The hashtag was not found. Maybe a typo?")

def help():
    print("""
-h | --help    : Displays this help message
-c | --no-color: Disabled the random colors
-v | --version : Shows the current version
-s | --source  : Shows the source of this project
-l | --license : Shows the license""")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--no-color", help="Disables terminal colors", action="store_true")
    parser.add_argument("-v", "--version", help="Shows version information", action="store_true")
    parser.add_argument("-s", "--source", help="Shows the Source of this project", action="store_true")
    parser.add_argument("-l", "--license", help="Shows License information", action="store_true")
    args = parser.parse_args()

    if args.no_color:
        def return_color():
            return Fore.LIGHTWHITE_EX

        execute()

    elif args.version:
        print(__version__)

    elif args.source:
        print(__source__)

    elif args.license:
        print(__license__)

    else:
        execute()



