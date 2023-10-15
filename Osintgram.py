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
import wget
import os
import json
import argparse

from logger import logger
from instagrapi import Client, exceptions
from colorama import *
from tqdm import tqdm
from hue_shift import return_color, reset

__version__ = "1.2"
__author__ = "Johannes Habel | EchterAlsFake"
__license__ = "GPL v3"
__source__ = "https://github.com/EchterAlsFake/Osintgram2"


def replace_unencodable_with_space(s, encoding='utf-8'):
    """Needed for Accounts with chinese or in general non utf-8 encoding"""
    result = []
    for c in s:
        try:
            c.encode(encoding)
            result.append(c)
        except UnicodeEncodeError:
            result.append(' ')
    return ''.join(result)


def create_workspace(target_name, hashtag_name=False):
    """Created a workspace for every target / hashtag"""
    folders = ["album", "igtv", "photos", "stories", "profile_pic", "location", "photos_captions", "comments",
               "followers", "followings", "followers_email", "followings_email", "followers_number",
               "followings_number",
               "user_info"]

    hashtag_medias = ["igtv", "photos", "stories", "clips"]

    if not os.path.exists(target_name):
        os.mkdir(target_name)

    if hashtag_name is not False:
        if not os.path.exists(hashtag_name):
            os.mkdir(hashtag_name)

            for folder in hashtag_medias:
                if not os.path.exists(f"{hashtag_name}{os.sep}{folder}"):
                    os.mkdir(f"{hashtag_name}{os.sep}{folder}")

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


Other information:

If you login and it says Invalid credentials even if you are sure they are correct, then you got added to the login
blacklist on Instagram. You can still login via the Web Browser. Open the developer tools, go to 'Application' and
then go to the Cookies section. There you'll find your Session ID. Copy the value, create a file: session.json
and write the following in it:

{ 'session_id' : '<your_session_id>' }

If you get timed out even with login create a new account for Instagram. If that doesn't work, restart your WiFi Router
to get a new IP address assigned. If that doesn't work use another device. Change your device fingerprint and name.

I know it's ugly, but it's the only way we get it working. 


Press Enter to continue...
""")


class Osintgram:
    """
Tries to be as Osintgram from Datalux, which is sadly dead, because the API is not working properly.
My version of Osintgram uses a really stable API called 'instagrapi'
    """

    def __init__(self):
        self.z = f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET}"
        self.photo_data = []
        self.video_data = []
        self.igtv_data = []
        self.reel_data = []
        self.album_data = []
        self.stories = []
        self.followers = None
        self.followings = None
        self.medias_export = None
        self.target = False
        self.cl = Client()
        while True:
            try:
                self.menu()

            except KeyboardInterrupt:
                exit(0)

            except exceptions.LoginRequired as e:
                logger(f"Instagram wants you to login. Please change your IP or Login to continue : {e}", level=1)

            except exceptions.ChallengeRequired:
                logger("You need to solve a challenge. Go to instagram.com to do this!", level=1)

            except exceptions.UserNotFound:
                logger("The user was not found. Try again", level=1)

            except exceptions.PrivateAccount:
                logger("The User's account is private. You need to log in and follow the account in order to retrieve "
                       "information", level=1)

            except exceptions.PleaseWaitFewMinutes:
                logger("Timed out by instagram. Please wait a few minutes, change IP and try again!", level=1)

            except exceptions.ClientJSONDecodeError:
                logger("Instagram API returned different Data than expected. This is likely because you got blocked."
                       "Go to Instagram.com and see if a pop up with a challenge appears.", level=1)

            except exceptions.ClientUnauthorizedError:
                logger("Go to Instagram.com and solve a challenge", level=1)

    def menu(self):

        if self.target is not False:
            if self.check_account_type():
                color = Fore.LIGHTGREEN_EX

            elif not self.check_account_type():
                color = Fore.LIGHTRED_EX
        else:
            color = Fore.LIGHTWHITE_EX

        options_map = {
            "0": "login",
            "1": "get_location",
            "2": "get_photos_captions",
            "3": "get_comments",
            "4": "get_followers",
            "5": "get_followings",
            "6": lambda: self.get_follower_ings_data(mode="email", follow_mode="8"),
            "7": lambda: self.get_follower_ings_data(mode="email", follow_mode="9"),
            "8": lambda: self.get_follower_ings_data(mode="phone", follow_mode="8"),
            "9": lambda: self.get_follower_ings_data(mode="phone", follow_mode="9"),
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
{Fore.LIGHTGREEN_EX}GREEN: {Fore.LIGHTWHITE_EX}Works
{Fore.LIGHTWHITE_EX}White: Unknown / Undefined
{Fore.LIGHTRED_EX}Red:   {Fore.LIGHTWHITE_EX}Needs login
        
T) Set Target
0) - Login             Needed for private account's you are following to
{color}1) - addrs             Get all registered addressed by target photos
{color}2) - captions          Get user's photos captions
{color}3) - comments          Get total comments of target's posts
{color}4) - followers         Get target followers
{color}5) - followings        Get users followed by target
{color}6) - fwersemail        Get email of target followers
{color}7) - fwingsemail       Get email of users followed by target
{color}8) - fwersnumber       Get phone number of target followers
{color}9) - fwingsnumber      Get phone number of users followed by target
{Fore.LIGHTGREEN_EX}10) - info             Get target info
{color}11) - likes            Get total likes of target's posts
{color}12) - mediatype        Get user's posts type (photo or video)
{color}13) - photos           Download user's photos in output folder
{Fore.LIGHTGREEN_EX}14) - propic           Download user's profile picture
{color}15) - stories          Download user's stories
{color}16) - album            Download user's album
{color}17) - igtv             Get user's IGTV
{Fore.LIGHTWHITE_EX}18) - hashtag_media    Get all media files from a specific hashtag
{Fore.LIGHTWHITE_EX}19) - hashtag_search   Search for hashtags with a search query
20) - Exit  
-------------------=>:""")

        excluded_numbers = {9, 11, 13, 15, 4, 5, 6, 7, 8}
        excluded_numbers_target = {0, 18, 19, 20}
        need_media_request_range = [i for i in range(1, 18) if i not in excluded_numbers]
        need_target_being_set = [i for i in range(1, 20) if i not in excluded_numbers_target]
        deprecated = {4, 5, 6, 7, 8, 9}  # Use set for better performance

        if options == "T":
            self.get_target()
            return  # To exit early from the function if the option is "T"

        int_options = int(options)

        if int_options in deprecated:
            _ = input(f"""
WARNING:

Since the old Osintgram Instagram has changed a lot of things on their API.
It's now much more restricted and we can't do so much things with excessive speeds like back than.

I can load 2 follower objects per second. 
1000 followers would take 500 seconds (8.3 minutes) to load.

The chances of getting timed out are high.

Do you really want to continue?

1) Yes
2) No
""")
            if _ != "1":
                self.menu()
                return

        if int_options in need_target_being_set:
            self.get_target()

        if int_options in need_media_request_range or int_options != 20:
            self.media()

        if int_options == 20:
            exit(0)

        method = options_map.get(options, None)
        if method:
            if callable(method):
                method()
            else:
                getattr(self, method)()

    def login(self, password_login=False):
        print("Login called")
        if not os.path.isfile("session.json") or password_login:

            if os.path.exists("session.json"):
                os.remove("session.json")

            try:
                username = input(f"{return_color()}Username: {reset()}")
                password = input(f"{return_color()}Password: {reset()}")
                self.cl.login(username, password)
                logger(f"{return_color()}Login Successful!{reset()}")
                session_id = self.cl.sessionid
                session_data = {
                    "session_id": session_id}

                with open("session.json", "w") as file:
                    json.dump(session_data, file)

            except exceptions.BadPassword or exceptions.BadCredentials:
                logger("Invalid credentials!", level=1)
                self.login(password_login=True)

        else:
            with open("session.json", "r") as file:
                session_data = json.load(file)

            session_id_value = session_data["session_id"]
            try:
                self.cl.login_by_sessionid(session_id_value)
                logger(f"{return_color()}Login Successful!{reset()}")

            except exceptions.BadPassword or exceptions.BadCredentials:
                logger(f"Login with Session ID failed.  Probably because it's out of date. Please try with password...")
                self.login(password_login=True)

    def get_target(self):
        self.target = input(f"{self.z}{return_color()}Enter target --=>:{reset()}")
        self.clear_lists()
        target_id = self.get_target_id()
        logger(f"{return_color()}Verified Target as User: {target_id}{reset()}")
        create_workspace(self.target)
        self.medias_export = False

    def check_account_type(self):
        """Checks if target is private account or not"""

        try:
            self.cl.user_medias(user_id=self.get_target_id(), amount=1)
            return True

        except exceptions.PrivateAccount or exceptions.PrivateError:
            return False

    def media(self):
        if self.medias_export is False:
            self.get_media_raw()

    def get_target_id(self):
        return self.cl.user_id_from_username(self.target)

    def get_media_raw(self):
        request_speed = input(f"""
In order to load the media objects, we need to adjust the speed of the API. Higher speeds will increase the chance of
getting banned or a complete fail of the operation.

The media objects must only be loaded once for a target in a terminal session. It can then be reused, when using other
functions such as get IGTV or get Albums.

Enter between 1 - 100 (default: 50) -->:
""")

        if not int(request_speed) in range(0, 100):
            print("Invalid input. Please enter a number between 0 and 100")
            self.get_media_raw()

        end_cursor = None
        counter = 0
        all_medias = []
        user_info = self.cl.user_info(self.get_target_id())
        total_posts = user_info.media_count

        pbar = tqdm(total=total_posts, desc="Fetching media")

        while True:
            medias, end_cursor = self.cl.user_medias_paginated(self.get_target_id(), amount=int(request_speed),
                                                               end_cursor=end_cursor)
            counter += len(medias)  # Increment counter by actual fetched count
            pbar.update(len(medias))  # Update progress bar by actual fetched count
            all_medias.extend(medias)

            if counter >= total_posts:
                break

        data = self.sort_data_types(medias)
        self.photo_data = data[0]
        self.video_data = data[1]
        self.igtv_data = data[2]
        self.reel_data = data[3]
        self.album_data = data[4]
        self.medias_export = True

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

        with open(f"{self.target}{os.sep}location{os.sep}location_data.txt", "a") as location_file:
            for media in medias:
                with contextlib.suppress(AttributeError):
                    print(media.pk)
                    latitudes.append(media.location.lat)
                    longitudes.append(media.location.lng)
                    data = f"Latitude:  {media.location.lat} : Longitude: {media.location.lng}"
                    print(data)
                    location_file.write(f"{data}\n")

            if len(latitudes) == 0 and len(longitudes) == 0:
                logger(f"{return_color()} No location data found. Sorry.")

    def download_album(self):
        for item in tqdm(self.album_data):
            self.cl.album_download(item.pk, folder=f"{self.target}{os.sep}album{os.sep}")

        logger("Finished downloading :)")

    def get_photos_captions(self):
        if len(self.photo_data) == 0 or self.photo_data is None:
            logger(msg="Target has no photos...", level=1)
            self.menu()

        else:
            with open(f"{self.target}{os.sep}photos_captions.txt", "w") as caption_file:
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

        with open(f"{self.target}{os.sep}comments{os.sep}comments.txt") as comments_file:
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
                    print(data)
                    comments_file.write(f"{data}\n")

    def get_followers(self):
        _ = input(f"{self.z}{return_color()}Enter amount of followers you want to get (0 for all) --=>:")
        amount_per_request = int(input(f"""
We need to adjust the API speed. Please set in range of 0 - 100
The more followers the Target has, the less should be the speed.

Enter between 0 - 100 (default: 50) -->:"""))

        if not amount_per_request in range(0, 100):
            logger("Invalid input. Please enter a number between 0 and 100", level=1)

        if int(_) == 0:
            user_info = self.cl.user_info(self.get_target_id())
            total_followers = user_info.follower_count

        else:
            total_followers = int(_)

        pbar = tqdm(total=total_followers, desc="Fetching followers")

        all_followers = []
        end_cursor = None

        while True:
            followers = self.cl.user_followers_gql_chunk(self.get_target_id(),
                                                         max_amount=amount_per_request,
                                                         end_cursor=end_cursor)
            print(end_cursor)

            pbar.update(len(followers))
            all_followers.extend(followers)
            # Break condition if there's no more data (no end_cursor)
            if len(all_followers) >= total_followers:
                self.followers = followers
                break

        pbar.close()

    def get_followings(self):
        _ = input(f"{self.z}{return_color()}Enter amount of followers you want to get (0 for all) --=>:")
        amount_per_request = int(input(f"""
        We need to adjust the API speed. Please set in range of 0 - 100
        The more followers the Target has, the less should be the speed.

        Enter between 0 - 100 (default: 50) -->:"""))

        if not amount_per_request in range(0, 100):
            logger("Invalid input. Please enter a number between 0 and 100", level=1)

        if int(_) == 0:
            user_info = self.cl.user_info(self.get_target_id())
            total_followers = user_info.follower_count

        else:
            total_followers = int(_)

        pbar = tqdm(total=total_followers, desc="Fetching followers")

        all_followers = []

        while True:
            following = self.cl.user_following(self.get_target_id(), amount=amount_per_request)

            pbar.update(len(following))
            all_followers.extend(following)

            if len(all_followers) >= total_followers:
                self.followers = following
                break

        pbar.close()

    def get_follower_ings_data(self, follow_mode, mode):
        if follow_mode == "8":
            if self.followers is None or len(self.followings) == 0:
                self.get_followers()
            followers = self.followers

        elif follow_mode == "9":
            if self.followings is None or len(self.followers) == 0:
                self.get_followings()
            followers = self.followings

        valid_users = []
        usernames = []
        emails = []
        codes = []
        numbers = []

        for follower_object in followers:
            for follower in follower_object:
                try:
                    usernames.append(follower.username)
                except AttributeError:
                    pass

        for username in usernames:
            user_info = self.cl.user_info(user_id=self.cl.user_id_from_username(username))

            if mode == "email":
                try:
                    if user_info.public_email is not None:
                        emails.append(user_info.public_email)
                        valid_users.append(user_info.username)
                except AttributeError:
                    pass

            else:
                if user_info.public_phone_country_code is not None:
                    codes.append(user_info.public_phone_country_code)
                    if username not in valid_users:
                        valid_users.append(username)

                if user_info.public_phone_number is not None:
                    numbers.append(user_info.public_phone_number)
                    if username not in valid_users:
                        valid_users.append(username)

        if mode == "email":
            with open(f"{self.target}{os.sep}followers_email{os.sep}emails.txt", "w") as emails_file:
                if len(emails) == 0:
                    logger(msg="Sorry, but none of the users have a public email address :(", level=1)
                else:
                    for counter, email in enumerate(emails):
                        data = f"{counter}) User: {valid_users[counter]} Email: {email}"
                        logger(data)
                        emails_file.write(f"{data}\n")

        else:
            with open(f"{self.target}{os.sep}followers_number{os.sep}numbers.txt", "w") as followers_number_file:
                if len(numbers) == 0:
                    logger(msg="Sorry, but none of the users have a public phone number :(", level=1)
                else:
                    for counter, user in enumerate(valid_users):
                        data = (
                            f"{return_color()}{counter}) Found Number {numbers[counter]} with Code: {codes[counter]} for "
                            f"User: {user}")
                        logger(data)
                        followers_number_file.write(f"{data}\n")

    def get_igtv(self):
        if len(self.igtv_data) == 0 or self.igtv_data is None:
            logger("User has not IGTV data", level=1)

        else:
            for item in tqdm(self.igtv_data):
                pk = item.pk
                self.cl.igtv_download(pk, folder=f"{self.target}{os.sep}igtv{os.sep}")

    def get_info(self):
        if not self.target:
            target = input(
                f"{return_color()}Enter Target  (Private verification will be skipped. Do not report errors here!) -->:")
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
            with open(f"{self.target}{os.sep}user_info{os.sep}user_info.txt", "w") as user_info:
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
{return_color()}Album:  {album}
""")

    def download_photos(self):
        for photo in tqdm(self.photo_data):
            pk = photo.pk
            self.cl.photo_download(pk, folder=f"{self.target}{os.sep}photos{os.sep}")

    def download_propic(self):
        if not self.target:
            target = input(
                f"{return_color()}Enter Target  (Private verification will be skipped. Do not report errors here!) -->:")

        else:
            target = self.target

        user_id = self.cl.user_id_from_username(target)
        user_info = self.cl.user_info(user_id)
        picture = user_info.profile_pic_url_hd
        if self.target is None:
            wget.download(picture)

        else:
            wget.download(picture, out=f"{self.target}{os.sep}profile_pic{os.sep}")

        logger(f"Downloaded profile picture!")

    def download_stories(self):
        amount = input(
            f"{self.z}{return_color()}Enter the amount of stories you want to download (0 for all) --=>:")
        stories = self.cl.user_stories_v1(self.get_target_id(), amount=int(amount))

        for story in tqdm(stories):
            pk = story.pk
            logger(f"Downloading Story: {pk}")
            self.cl.story_download(int(pk), folder=f"{self.target}{os.sep}stories{os.sep}")

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
    proceed()
    Osintgram()


def help():
    print("""
-h | --help    : Displays this help message
-c | --no-color: Disabled the random colors
-v | --version : Shows the current version
-s | --source  : Shows the source of this project
-l | --license : Shows the license""")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--no-color", help="Disables most of the terminal colors", action="store_true")
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
