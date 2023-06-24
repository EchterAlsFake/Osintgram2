# This is the extension for the widget.py
# Please don't change, except you know what you are doing.
# License: GPLv3
import wget
from instagrapi import Client, exceptions
from colorama import *
from ui_form import Ui_widget
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtCore import QThread, Signal
import sys
import random
import json

class LoginWorker(QThread):
    finished_signal = Signal(str)

    def __init__(self, cl, username, password):
        super().__init__()
        self.cl = cl
        self.username = username
        self.password = password

    def run(self):
        try:
            self.cl.login(username=self.username, password=self.password)
            self.finished_signal.emit(self.cl.username)
        except exceptions.BadPassword:
            self.finished_signal.emit("BadPassword")
        except exceptions.ChallengeRequired:
            self.finished_signal.emit("ChallengeRequired")
        except exceptions.TwoFactorRequired:
            self.finished_signal.emit("TwoFactorRequired")

class MediaIDWorker(QThread):
    def __init__(self, cl, target):
        super().__init__()
        self.cl = cl
        self.target = target

    def run(self):
        self.media_ids = [media.id for media in self.cl.user_medias(self.target)]

class CommentWorker(QThread):
    progress_signal = Signal(int)

    def __init__(self, cl, media_ids):
        super().__init__()
        self.cl = cl
        self.media_ids = media_ids
        self.comments_data = []

    def run(self):
        counter = 0
        for comment_id in self.media_ids:
            comment = self.cl.media_comments(comment_id)
            for cmd in comment:
                text = cmd.text
                user = cmd.user.full_name
                comment_data = {"username": user, "text": text,
                                "id": cmd.pk}
                self.comments_data.append(comment_data)

            counter += 1
            self.progress_signal.emit(counter)

class DownloadPhotosWorker(QThread):
    progress_signal = Signal(int)

    def __init__(self, media_list):
        super().__init__()
        self.media_list = media_list

    def run(self):
        counter = 0
        for url in self.media_list:
            random_name = random.randint(1000000, 9999999)
            wget.download(url, out=f"{random_name}.jpg")
            counter += 1
            self.progress_signal.emit(counter)

class GetMediaWorker(QThread):
    finished_signal = Signal(list)

    def __init__(self, cl, target):
        super().__init__()
        self.cl = cl
        self.target = target

    def run(self):
        medias = self.cl.user_medias(int(self.target))
        media_list = [media.thumbnail_url for media in medias if media.thumbnail_url is not None]
        self.finished_signal.emit(media_list)

class Widget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.login_worker = None
        self.z = f"{Fore.LIGHTGREEN_EX}[+]"
        self.ui = Ui_widget()
        self.ui.setupUi(self)
        self.ui.button_login.clicked.connect(self.login)
        self.ui.button_photos.clicked.connect(self.get_photos)
        self.ui.button_profile_pic.clicked.connect(self.get_thumbnail)
        self.ui.button_download_comments.clicked.connect(self.get_comments)
        self.ui.button_locations.clicked.connect(self.get_locations)

    def get_locations(self):

        qmsg_box = QMessageBox()
        qmsg_box.setText("This feature is currently not working. Since instagram strips out the metadata, it's getting hard to find a way ;) ")
        qmsg_box.exec()

    def login(self):
        self.ui.lineedit_status.setText("Logging in.  Please note, that this can take up to 10 seconds...")
        self.ui.progressbar_login.setRange(0, 0)
        self.cl = Client()
        username_zt = self.ui.lineedit_email.text()
        password_zt = self.ui.lineedit_password.text()

        self.login_worker = LoginWorker(self.cl, username_zt, password_zt)
        self.login_worker.finished_signal.connect(self.on_login_finished)
        self.login_worker.start()

    def on_login_finished(self, result):
        if result == "BadPassword":
            self._extracted_from_on_login_finished_3(
                "Incorrect password. Try again!", "Incorrect password. Try again!")
        elif result == "ChallengeRequired":
            msgbox = QMessageBox()
            msgbox.setText("""You need to solve a challenge. Go into your web browser, go to instagram and login in as
            you would normally do. You will most likely be required to solve a re-captcha or some other stuff. After 
            that, you can login with Osintgram again.""")
            self._extracted_from_on_login_finished_3("""You need to solve a challenge. Go into your web browser, go to 
instagram and login in as you would normally do. You will most likely be required to solve a re-captcha or some other 
stuff. After that, you can login with Osintgram again.""")
            msgbox.exec()
        elif result == "TwoFactorRequired":
            self._extracted_from_on_login_finished_3(
                "Two Factor is required. Please remove it from your Account, as it's not supported yet!",
                """Two Factor is required. Please remove it from your Account, 
            as it's not supported yet!""",)
        else:
            self.ui.lineedit_status.setText(f"Logged in as: {result}")
            self.ui.progressbar_login.setRange(0, 100)
            self.ui.progressbar_login.setValue(100)

    def _extracted_from_on_login_finished_3(self, arg0, arg1):
        msgbox = QMessageBox()
        msgbox.setText(arg0)
        msgbox.exec()
        self._extracted_from_on_login_finished_3(arg1)

    def get_photos(self):
        self.ui.progressbar_photos.setRange(0, 0)
        target = self.get_target()
        if target == False:
            return

        self.get_media_worker = GetMediaWorker(self.cl, target)
        self.get_media_worker.finished_signal.connect(self.start_download_photos_worker)
        self.get_media_worker.start()

    def start_download_photos_worker(self, media_list):
        self.ui.progressbar_photos.setMaximum(len(media_list))
        self.download_photos_worker = DownloadPhotosWorker(media_list)
        self.download_photos_worker.progress_signal.connect(self.ui.progressbar_photos.setValue)
        self.download_photos_worker.finished.connect(self.on_photos_downloaded)
        self.download_photos_worker.start()

    def on_photos_downloaded(self):
        self.ui.lineedit_status.setText("Downloading complete.")
        self.ui.progressbar_photos.setRange(0, 100)
        self.ui.progressbar_photos.setValue(100)

    def get_target(self):
        name = self.ui.lineedit_target.text()
        try:
            return self.cl.user_id_from_username(name)

        except Exception as e:
            qmsg = QMessageBox()
            qmsg.setText(str(e))
            qmsg.exec()
            return False

    def get_thumbnail(self):

        target = self.get_target()

        self.ui.progressbar_profile_pic.setMaximum(1)
        self.ui.progressbar_profile_pic.setValue(0)
        self.ui.lineedit_status.setText("Downloading profile picture...")

        profile_picture = self.cl.user_info(target).profile_pic_url_hd
        wget.download(url=profile_picture, out=f"Profile_Picture_HD_{target}.jpg")
        self.ui.progressbar_profile_pic.setValue(1)
        self.ui.lineedit_status.setText("Profile Picture Download complete.")

    def get_comments(self):
        target = self.get_target()
        if target != False:

            self.ui.progressbar_comments.setRange(0, 0)

            self.media_id_worker = MediaIDWorker(self.cl, target)
            self.media_id_worker.finished.connect(self.start_comment_worker)
            self.media_id_worker.start()

    def start_comment_worker(self):
        self.ui.progressbar_comments.setRange(0, len(self.media_id_worker.media_ids))

        self.comment_worker = CommentWorker(self.cl, self.media_id_worker.media_ids)
        self.comment_worker.progress_signal.connect(self.ui.progressbar_comments.setValue)
        self.comment_worker.finished.connect(self.on_comment_worker_finished)
        self.comment_worker.start()

    def on_comment_worker_finished(self):
        self.ui.lineedit_status.setText("Saving comments to 'comments_data.json'")
        with open('comments_data.json', 'w') as f:
            json.dump(self.comment_worker.comments_data, f)
            self.ui.lineedit_status.setText("Comments saved to 'comments_data.json'")
            for comment_data in self.comment_worker.comments_data:
                print(
                    f"Username: {comment_data['username']}, Text: {comment_data['text']}, ID: {comment_data['id']}")
        print("Done :) ")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
