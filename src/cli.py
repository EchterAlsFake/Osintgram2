import contextlib
import instagrapi.exceptions
from instagrapi import Client
import wget
import os
from colorama import *
from time import sleep
from datetime import datetime
from getpass import getpass
import json

class Osintgram_advanced():

    def __init__(self):
        self.z = f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET}"
        self.x = f"{Fore.LIGHTRED_EX}[~]{Fore.RESET}"
        self.username = None
        self.password = None
        self.target = "Not specified"
        self.cl = Client()
        self.login()
        self.menu()

    def login(self):

        self.username = input(f"{self.z}{Fore.LIGHTCYAN_EX}Please enter your Instagram username: {Fore.RESET}")
        self.password = getpass("Please enter your Instagram password: ")

        try:

            self.cl.login_by_sessionid()
            session_id = self.cl.sessionid
            print(f"{self.z}{Fore.LIGHTGREEN_EX}Login successful!  Session ID: {session_id}{Fore.RESET}")

        except instagrapi.exceptions.BadPassword:
            print(f"{self.x}{Fore.LIGHTRED_EX}Incorrect password!{Fore.RESET}")
            self.login()

        except instagrapi.exceptions.ChallengeRequired:
            print(f"{self.x}{Fore.LIGHTRED_EX}You need to solve a challenge. Go to instagram.com and solve it. Then try again.{Fore.RESET}")


    def menu(self):

        options = input(f"""
        
        Information: 
        
        If an option is marked with a * it means, that you can be blocked
        for using it, as it makes a lot of requests to the Instagram API.
        
1) Set target      (Not needed if you only use functions for your account)
2) Account page (your account)
3) Target options
4) Credits
5) Export Session ID for further use  (This is HIGHLY recommended for EVERYONE)
6) Exit""")

        if options == "1":
            self.set_target()

        elif options == "2":
            self.account_page()


    def set_target(self):

        target = input(f"""
Please enter the account name of the instagram account you want to do stuff with --=>:""")

        """
        Just checking if the account exists...
        """

        try:
            user_id = self.cl.user_id_from_username(target)
            information = self.cl.user_info(user_id)
            url = information.external_url
            full_name = information.full_name

        except instagrapi.exceptions.UserNotFound:
            print(f"{self.x}{Fore.LIGHTRED_EX}Account not found!{Fore.RESET}")
            self.set_target()


        _ = input(f"""
Please check the information:

User ID: {user_id}
Full Name: {full_name}
External URL: {url}

Are you sure that this is the corrent account? 

1) Yes
2) No, let me change
----------------------=>:""")

        if _ == "1":
            self.target = target
            print(f"{self.z}{Fore.LIGHTGREEN_EX}Target set!{Fore.RESET}")

        elif _ == "2":
            self.set_target()

        else:
            self.set_target()

    def account_page(self):

        options = input(f"""
        
        
----------------------------------------------------------------
            Follower related stuff
----------------------------------------------------------------

1) Unfollow someone (Gives a list of everyone and you can choose)
2) Follow someone
3) Remove followers
4) Mute posts from follower
5) unmute posts from follower
6) mute stories from follower
7) enable posts notification from someone
8) disable posts notification from someone
9) enable video notifications from someone
10) disable video notifications from someone
11) enable story notifications from someone
12) disable story notifications from someone
13) enable reels notifications from someone
14) disable reels notifications from someone
15) add someone as close friend
16) remove someone as close friend


------------------------------------------
        Mass scraping:
------------------------------------------

17) Download all profile pictures from your followers * 
18) Download all profile pictures from your following * 


--------------------------------------------
        Options for your account:
--------------------------------------------

19) View your information
20) Change your E-Mail, phone number, username, full name, biography
21) Change your profile picture
22) Send confirmation code to new E-Mail address
23) Send confirmation code to new phone number


--------------------------------------------
        Media upload:
--------------------------------------------

Nothing here...


-----------------------------------=>:""")


        if options == "1":
            self.get_follower_list()
    def get_follower_list(self):
        username = self.cl.username
        user_id = self.cl.user_id_from_username("leomessi")
        print(f"{self.z}{Fore.LIGHTGREEN_EX}User: {username}{Fore.RESET}")
        follower_list = self.cl.user_followers(user_id=user_id)
        for follower in follower_list:
            print(follower)


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
        self.target = "Not specified"
        self.cl = Client()
        self.login()
        while True:
            self.menu()


    def menu(self):

        options = input(f"""
T) - Set target
1) - addrs           Get all registered addressed by target photos
2) - captions        Get user's photos captions
3) - comments        Get total comments of target's posts
4) - followers       Get target followers
5) - followings      Get users followed by target
6) - fwersemail      Get email of target followers
7) - fwingsemail     Get email of users followed by target
8) - fwersnumber     Get phone number of target followers
9) - fwingsnumber    Get phone number of users followed by target
10) - hashtags        Get hashtags used by target
11) - info            Get target info
12) - likes           Get total likes of target's posts
13) - mediatype       Get user's posts type (photo or video)
14) - photodes        Get description of target's photos
15) - photos          Download user's photos in output folder
16) - propic          Download user's profile picture
17) - stories         Download user's stories  
18) - tagged          Get list of users tagged by target
19) - wcommented      Get a list of user who commented target's photos
20) - wtagged         Get a list of user who tagged target

-------------------=>:""")

        if options == "1":
            if len(self.photo_data) == 0 or self.photo_data is None:
                print("No photo data.  Checking for media.....")
                self.get_media()

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


        elif options == "T":
            self.username = input(f"{self.z}{Fore.LIGHTCYAN_EX}Enter target --=>:")
            self.verify_target()




    def login(self, password_login=False):

        if not os.path.isfile("session.json") or password_login:
            print(f"{self.z}There is no session.json file. Logging in with username and password...")

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
        self.get_media()

    def get_media(self):
        target_id = self.get_target_id()
        print(f"{self.z}{Fore.LIGHTGREEN_EX}Target ID: {target_id}{Fore.RESET}")
        medias = self.cl.user_medias_v1(user_id=target_id)
        print(f"{self.z}{Fore.LIGHTGREEN_EX}Found {len(medias)} media files{Fore.RESET}")
        for media in medias:
            print(media.media_type)
            if media.media_type == 1:
                self.photo_data.append(media)
                print(f"{self.z}{Fore.LIGHTGREEN_EX}Appended: Photo")

            elif media.media_type == 2 and media.product_type == "feed":
                self.video_data.append(media)
                print(f"{self.z}{Fore.LIGHTGREEN_EX}Appended: Video")

            elif media.media_type == 2 and media.product_type == "igtv":
                self.igtv_data.append(media)
                print(f"{self.z}{Fore.LIGHTGREEN_EX}Appended: IGTV")

            elif media.media_type == 2 and media.product_type == "clips":
                self.reel_data.append(media)
                print(f"{self.z}{Fore.LIGHTGREEN_EX}Appended: Reel")

            elif media.media_type == 8:
                self.album_data.append(media)
                print(f"{self.z}{Fore.LIGHTGREEN_EX}Appended: Album")


        print(f"""
Photos: {len(self.photo_data)}
Videos: {len(self.video_data)}
IGTV: {len(self.igtv_data)}
Reels: {len(self.reel_data)}
Albums: {len(self.album_data)}
""")





Osintgram_like_datalux()
