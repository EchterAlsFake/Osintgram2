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
import os
try:
    from instagrapi import Client
except Exception as e:
    with open("/storage/emulated/0/Osintgram_log.txt", "w") as f:
        f.close()

    with open("/storage/emulated/0/Osintgram_log.txt", "w") as f:
        f.write(str(e))


root_path = "/storage/emulated/0"

__version__ = "1.1_android_debug"
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


def create_workspace(target_name, hashtag_name=False):


    folders = ["album", "igtv", "photos", "story", "profile_pic", "location", "photos_captions", "comments",
               "followers", "followings", "followers_email", "followings_email", "followers_number",
               "followings_number",
               "user_info"]

    if not os.path.exists(target_name):
        os.mkdir(f"{root_path}{os.sep}{target_name}")

    for folder in folders:
        if not os.path.exists(f"{root_path}{os.sep}{target_name}{os.sep}{folder}"):
            os.mkdir(f"{root_path}{os.sep}{target_name}{os.sep}{folder}")


from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.textfield import MDTextField
from kivymd.color_definitions import colors

KV = '''
Screen:
    MDBoxLayout:
        orientation: "vertical"
        spacing: "10dp"
        padding: "10dp"

        MDBoxLayout:
            MDLabel:
                text: "Username"
            MDTextField:
                id: username_input
                hint_text: "Enter username"

        MDBoxLayout:
            MDLabel:
                text: "Password"
            MDTextField:
                id: password_input
                hint_text: "Enter password"
                password: True

        MDBoxLayout:
            MDLabel:
                text: "Target:"
            MDTextField:
                id: target_input
                hint_text: "Enter Target"
                password: False


        MDFillRoundFlatButton:
            text: "Login"
            on_press: app.on_login()
            md_bg_color: app.theme_cls.accent_color
            line_color: app.theme_cls.primary_color

        MDFillRoundFlatButton:
            text: "Get Photos"
            on_press: app.on_get_photos()
            md_bg_color: app.theme_cls.accent_color
            line_color: app.theme_cls.primary_color

        MDProgressBar:
            id: progress_bar
            value: 0
'''

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Purple'
        self.theme_cls.accent_palette = 'Purple'
        self.cl = Client()
        return Builder.load_string(KV)

    def on_login(self):
        username = self.root.ids.username_input.text
        password = self.root.ids.password_input.text
        print(f"Logging in with username: {username}, password: {password}")
        self.cl.login(username, password)
        print(f"Logged in!")



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

    def on_get_photos(self):
        progress_bar = self.root.ids.progress_bar
        total = len(self.photo_data)
        progress_bar.max = int(total)

        for counter, photo in enumerate(self.photo_data):
            self.cl.photo_download(media_pk=photo.pk, folder=f"{root_path}{os.sep}photos{os.sep}")
            progress_bar.value = counter  # Update progress bar value based on your logic




    def get_target_id(self):
        target = self.root.ids.target_input.text
        create_workspace(target)
        id = self.cl.user_id_from_username(target)
        print(f"Target: {target}")
        medias = self.cl.user_medias(id)
        data = self.sort_data_types(medias)
        self.photo_data = data[0]
        self.video_data = data[1]
        self.igtv_data = data[2]
        self.reel_data = data[3]
        self.album_data = data[4]






if __name__ == "__main__":
    MainApp().run()
