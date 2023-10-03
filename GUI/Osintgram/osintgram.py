import sys
import os
import json

from instagrapi import Client
from instagrapi import exceptions
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from ui_form import Ui_Osintgram


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


def ui_popup(text):
    qmsg_box = QMessageBox()
    qmsg_box.setText(str(text))
    qmsg_box.exec()


class Osintgram(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Osintgram()
        self.ui.setupUi(self)
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
        self.medias_requested = False
        self.cl = Client()
        self.username = None
        self.buttons_pressed()

    def buttons_pressed(self):
        self.ui.button_login.clicked.connect(self.login)
        self.ui.button_photos.clicked.connect(self.download_photos)
        self.ui.button_igtv.clicked.connect(self.get_igtv)
        self.ui.button_get_likes.clicked.connect(self.get_likes)

    def login(self, password_login=False):
        username = self.ui.lineedit_username.text()
        password = self.ui.lineedit_password.text()

        if not os.path.isfile("session.json") or password_login:

            if os.path.exists("session.json"):
                os.remove("session.json")

            try:
                self.cl.login(username, password)
                self.logged_in = True
                ui_popup(f"Login successful!")
                session_id = self.cl.sessionid
                session_data = {
                    "session_id": session_id}

                with open("session.json", "w") as file:
                    json.dump(session_data, file)

            except exceptions.BadPassword or exceptions.BadCredentials:
                ui_popup(f"Wrong credentials. Please try again.")
                self.login(password_login=True)

        else:
            with open("session.json", "r") as file:
                session_data = json.load(file)

            session_id_value = session_data["session_id"]
            try:
                self.cl.login_by_sessionid(session_id_value)
                self.logged_in = True
                ui_popup(f"Login successful!  Session ID: {self.cl.sessionid}")

            except exceptions:
                ui_popup("Session ID is out of date. Recreating new session ID...")
                self.login(password_login=True)

    def get_media_raw(self):
        medias = self.cl.user_medias_v1(user_id=self.get_user_id())
        self.medias_export = medias
        self.ui.lineedit_media.setText(str(len(medias)))
        create_workspace(self.ui.lineedit_target.text())
        data = self.sort_data_types(medias)
        self.photo_data = data[0]
        self.video_data = data[1]
        self.igtv_data = data[2]
        self.reel_data = data[3]
        self.album_data = data[4]

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

    def clear_lists(self):
        self.video_data = []
        self.reel_data = []
        self.album_data = []
        self.igtv_data = []
        self.photo_data = []
        self.followers = None
        self.followings = None


    def get_user_id(self):
        self.username = self.ui.lineedit_target.text()
        return self.cl.user_id_from_username(username=self.username)

    def download_photos(self):
        if not self.medias_requested:
            self.get_media_raw()

        self.ui.progressBar.setMaximum(len(self.photo_data))

        for counter, photo in enumerate(self.photo_data):
            pk = photo.pk
            self.cl.photo_download(pk, folder=f"{self.username}{os.sep}photos{os.sep}")
            self.ui.progressBar.setValue(counter)


    def get_igtv(self):
        if len(self.igtv_data) == 0 or self.igtv_data is None:
            ui_popup("User has not IGTV data")

        else:
            self.ui.progressBar.setMaximum(len(self.igtv_data))
            for counter, item in enumerate(self.igtv_data):
                pk = item.pk
                self.cl.igtv_download(pk, folder=f"{self.username}{os.sep}igtv{os.sep}")
                self.ui.progressBar.setValue(counter)

    def get_likes(self):
        likes = 0

        x = self.cl.user_medias_v1(user_id=self.get_user_id())
        for item in x:
            like_count = item.like_count
            like_count = int(like_count)
            likes += like_count

        ui_popup(f"Total Likes: {likes}")









if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        widget = Osintgram()
        widget.show()
        sys.exit(app.exec())

    except KeyboardInterrupt:
        exit(0)

    except exceptions.LoginRequired as e:
        ui_popup(f"Instagram wants you to login. Please change your IP or Login to continue : {e}")

    except exceptions.ChallengeRequired:
        ui_popup("You need to solve a challenge. Go to instagram.com to do this!")

    except exceptions.UserNotFound:
        ui_popup("The user was not found. Try again")

    except exceptions.PrivateAccount:
        ui_popup("The User's account is private. You need to log in and follow the account in order to retrieve "
               "information")

    except exceptions.PleaseWaitFewMinutes:
        ui_popup("Timed out by instagram. Please wait a few minutes, change IP and try again!")
