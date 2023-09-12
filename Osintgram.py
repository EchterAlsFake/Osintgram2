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

from instagrapi import Client
from colorama import *
from tqdm import tqdm

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
    if not os.path.exists(target_name):
        os.mkdir(target_name)



input("""
Licensed under GPLv3

DISCLAIMER!

This tool is NOT allowed by Instagram.com
It's against their ToS and you will get banned for it and you could even get into legal trouble!
Of course second will probably not happen, but I am not liable for what happens to your account.
When using this tool you know what you do and it's not my responsibility to protect your account.

This tool is made to help cyber security analysts and not some random kids to spy on someone.

The original creator of a similar tool also called Osintgram is 'Datalux'.
You can find his project here: https://github.com/Datalux/Osintgram

By continuing you accept that I am not liable for anything and that you do everything
at your own risk.

Can you live with the consequences?

Press enter if you can...
""")


class Osintgram_like_datalux():
    """
Tries to be as Osintgram from Datalux, which is sadly dead, because the API is not working properly.
My version of Osintgram uses a really stable API called 'instagrapi'
    """

    def __init__(self):
        self.z = f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET}"
        self.x = f"{Fore.LIGHTRED_EX}[~]{Fore.RESET}"
        self.username = None
        self.password = None
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
        self.login()
        while True:
            self.menu()

    def menu(self):

        options = input(f"""{Fore.LIGHTWHITE_EX}
T) Set Target
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
16) - Exit  

-------------------=>:""")
        if options == "1":
            if not self.target:
                self.get_target()

            self.get_location()

        elif options == "2":
            if not self.target:
                self.get_target()

            self.get_photos_captions()

        elif options == "3":
            if not self.target:
                self.get_target()

            self.get_comments()

        elif options == "4":
            if not self.target:
                self.get_target()

            self.get_followers()

        elif options == "5":
            if not self.target:
                self.get_target()

            self.get_followings()

        elif options == "6":
            if not self.target:
                self.get_target()

            self.get_email(mode="6")

        elif options == "7":
            if not self.target:
                self.get_target()

            self.get_email(mode="7")

        elif options == "8":
            if not self.target:
                self.get_target()

            self.get_number(mode="8")

        elif options == "9":
            if not self.target:
                self.get_target()

            self.get_number(mode="9")

        elif options == "10":
            if not self.target:
                self.get_target()

            self.get_info()

        elif options == "11":
            if not self.target:
                self.get_target()

            self.get_likes()

        elif options == "12":
            if not self.target:
                self.get_target()

            self.get_media_type()

        elif options == "13":
            if not self.target:
                self.get_target()

            self.download_photos()

        elif options == "14":
            if not self.target:
                self.get_target()

            self.download_propic()

        elif options == "15":
            if not self.target:
                self.get_target()

            self.download_stories()

        elif options == "16":
            exit(0)

        elif options == "T":
            self.get_target()


    def get_target(self):
        self.username = input(f"{self.z}{Fore.LIGHTCYAN_EX}Enter target --=>:")
        self.clear_lists()
        self.verify_target()

    def login(self, password_login=False):

        if not os.path.isfile("session.json") or password_login:
            print(f"{self.z}There is no session.json file. Logging in with username and password...")
            if not self.target:
                self.get_target()
            self.username = input(f"{self.z}{Fore.LIGHTCYAN_EX}Enter username --=>:")
            self.password = input(f"{self.z}{Fore.LIGHTCYAN_EX}Enter password --=>:")
            try:
                self.cl.login(self.username, self.password)
                print(f"{self.z}{Fore.LIGHTGREEN_EX}Login successful!")
                session_id = self.cl.sessionid
                session_data = {
                    "session_id": session_id
                }
                with open("session.json", "w") as file:
                    json.dump(session_data, file)

                print(f"{self.z}{Fore.LIGHTGREEN_EX}Saved Session ID")

            except instagrapi.exceptions.BadPassword or instagrapi.exceptions.BadCredentials:
                print(f"{self.x}{Fore.LIGHTWHITE_EX}Wrong credentials. Please try again.")
                self.login(password_login=True)


        else:

            with open("session.json", "r") as file:
                session_data = json.load(file)

            session_id_value = session_data["session_id"]
            print(f"{self.z}{Fore.LIGHTGREEN_EX}Found Session ID: {session_id_value}:")
            try:

                self.cl.login_by_sessionid(session_id_value)
                print(f"{self.z}{Fore.LIGHTGREEN_EX}Login successful!  Session ID: {self.cl.sessionid}")

            except instagrapi.exceptions.BadPassword:
                print(f"{self.x}{Fore.LIGHTRED_EX}Incorrect password!{Fore.RESET}")
                self.login()

    def get_target_id(self):
        return self.cl.user_id_from_username(self.username)

    def verify_target(self):
        target_id = self.get_target_id()
        info = self.cl.user_info(target_id)
        print(f"{self.z}{Fore.LIGHTCYAN_EX}Target: {info.full_name}")
        self.target = target_id
        self.get_media_raw()

    def get_followers_raw(self):
        target_id = self.get_target_id()
        print(f"{self.z}{Fore.LIGHTMAGENTA_EX}Requesting followers of {target_id}{Fore.RESET}")
        self.followers = self.cl.user_followers(user_id=target_id)

    def get_followings_raw(self):
        target_id = self.get_target_id()
        print(f"{self.z}{Fore.LIGHTMAGENTA_EX}Requesting followings of {target_id}{Fore.RESET}")
        self.followings = self.cl.user_following(user_id=target_id)

    def get_media_raw(self):
        print(f"{self.z}{Fore.LIGHTCYAN_EX}Requesting media objects for target: {self.target}")
        medias = self.cl.user_medias_v1(user_id=self.get_target_id())
        self.medias_export = medias
        print(f"{self.z}{Fore.LIGHTGREEN_EX}Found {len(medias)} media files{Fore.RESET}")
        for media in medias:
            print(media.media_type)
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
        if len(self.photo_data) == 0 or self.photo_data is None:
            print("No photo data.  Checking for media.....")
            self.get_media_raw()

        latitudes = []
        longitudes = []

        for media in self.photo_data:
            with contextlib.suppress(AttributeError):
                latitudes.append(media.location.lat)
                longitudes.append(media.location.lng)
                print(f"""
        {self.z}Found Location: {media.location.lat} : {media.location.lng}  First is lat, second is long.
        """)
        if len(latitudes) and not longitudes:
            print(f"{self.x}{Fore.LIGHTYELLOW_EX} No location data found. Sorry.")

    def get_photos_captions(self):

        if len(self.photo_data) == 0 or self.photo_data is None:
            self.get_media_raw()

        for media in self.photo_data:
            print(f"""
Media ID: {media.id}
Caption: {media.caption_text}
""")

        input(f"{self.z}{Fore.LIGHTYELLOW_EX}Press ENTER to continue...")

    def get_comments(self):
        data = self.photo_data + self.igtv_data + self.reel_data + self.video_data + self.album_data
        media_ids = [item.id for item in data]

        for id in media_ids:
            comments = self.cl.media_comments(media_id=id)
            print(f"{self.z}{Fore.LIGHTGREEN_EX}Found {len(comments)} comments in Media: {id}")
            for comment in comments:
                text = comment.text
                created = comment.created_at_utc
                likes = comment.like_count
                user = comment.user.username

                print(f"""
User: {user}
Commented at: {created}
Likes: {likes}
Text: {text}
                     
                """)

    def get_followers(self):

        user_id = self.get_target_id()
        amount = input(f"{self.z}{Fore.LIGHTYELLOW_EX}Enter amount of followings you want to get  (0 for all) --=>:")
        followings = self.cl.user_followers_v1(user_id, amount=int(amount))
        for counter, follower in enumerate(followings):
            print(f"{counter}) Username: {follower.username}")

    def get_followings(self):
        user_id = self.get_target_id()
        amount = input(f"{self.z}{Fore.LIGHTYELLOW_EX}Enter amount of followings you want to get  (0 for all) --=>:")
        followings = self.cl.user_following_v1(user_id, amount=int(amount))
        for counter, follower in enumerate(followings):
            print(f"{counter}) Username: {follower.username}")

    def get_email(self, mode):

        amount = input(
            f"{self.z}{Fore.LIGHTYELLOW_EX}For how much followers / following you want to get emails for (10 followers will take like 20-30 seconds) --=>:")
        user_id = self.get_target_id()
        if mode == "6":
            followers = self.cl.user_followers_v1(user_id, amount=int(amount))

        elif mode == "7":
            followers = self.cl.user_following_v1(user_id, amount=int(amount))

        emails = []
        user_names = []
        valid_users = []

        for follower in followers:
            user_names.append(follower.username)
            print(f"{self.z}{Fore.LIGHTMAGENTA_EX} Appended: {follower.username}")

        for username in user_names:
            try:
                email = self.cl.user_info_by_username(username)
                if email is not None:
                    emails.append(email.public_email)
                    valid_users.append(email.username)
                    print(f"{self.z}{Fore.LIGHTMAGENTA_EX} Appended: Valid User: {email.username}")

                else:
                    print(f"User: {username} Does not have a public email.")

            except AttributeError:
                pass

        for counter, email in enumerate(emails):
            print(f"{counter}) User: {user_names[counter]} Email: {email}")

    def get_number(self, mode):

        if mode == "8":
            if len(self.followers) == 0 or self.followers is None:
                self.get_followers()

            followers = self.followers

        elif mode == "9":
            if len(self.followings) == 0 or self.followings is None:
                self.get_followings()

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

        for counter, user in enumerate(valid_users):
            print(
                f"{self.z}{Fore.LIGHTCYAN_EX}{counter}) Found Number {numbers[counter]} with Code: {codes[counter]} for User: {user}")

    def get_info(self):

        id = self.get_target_id()
        info = self.cl.user_info_v1(id)

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
Business catefory name: {business_category_name}
Public Phone Number: {public_phone_number}
Public Phone country code: {public_country_code}
Public E-Mail: {public_email}
Catefory: {category}
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
        print(filtered_text)
        input("Press enter to continue...")

    def get_likes(self):
        likes = 0

        x = self.cl.user_medias_v1(user_id=self.get_target_id())
        for item in x:
            like_count = item.like_count
            like_count = int(like_count)
            likes += like_count

        print(f"Total Likes: {likes}")

    def get_media_type(self):

        photos = len(self.photo_data)
        reels = len(self.reel_data)
        igtv = len(self.igtv_data)
        video = len(self.video_data)
        album = len(self.album_data)

        print(f"""
    
Photos: {photos}
Reels:  {reels}
IGTV:   {igtv}
Video:  {video}
Album:  {album}""")

        input("Press Enter to continue...")

    def download_photos(self):

        for photo in tqdm(self.photo_data):
            pk = photo.pk
            if not os.path.exists("output"):
                os.mkdir("output")

            self.cl.photo_download(pk, folder="output")

    def download_propic(self):
        user_id = self.get_target_id()
        user_info = self.cl.user_info_v1(user_id)
        picture = user_info.profile_pic_url_hd
        wget.download(picture)
        print(f"{self.z}{Fore.LIGHTCYAN_EX}Downloaded profile picture!")

    def download_stories(self):
        amount = input(
            f"{self.z}{Fore.LIGHTYELLOW_EX}Enter the amount of stories you want to download (0 for all) --=>:")
        stories = self.cl.user_stories(user_id=self.get_target_id(), amount=int(amount))

        for story in stories:
            self.stories.append(story.pk)

        for pk in tqdm(self.stories):
            self.cl.story_download(pk, folder="output")

        print(f"{self.z}{Fore.LIGHTYELLOW_EX}Downloaded {len(stories)} stories")


if __name__ == "__main__":
    try:
        Osintgram_like_datalux()

    except KeyboardInterrupt:
        exit(0)

    except instagrapi.exceptions.LoginRequired:
        print("Instagram Error: Go to Instagram.com, solve the challenge and try again!")

    except instagrapi.exceptions.ChallengeRequired:
        print("You need to solve a challenge. Go to instagram.com to do this!")

    except instagrapi.exceptions.UserNotFound:
        print("The user was not found. Try again")

    except instagrapi.exceptions.ClientError:
        print("Client Error: Use a different account or restart!")