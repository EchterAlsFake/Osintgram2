# This is the extension for the widget.py
# Please don't change, except you know what you are doing.
# License: GPLv3
import wget
from instagrapi import Client
from colorama import *
from tqdm import tqdm
from ui_form import Ui_Form
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QThread, Signal
import os
import sys

images = []
class LoginWorker(QThread):
    status_signal = Signal(int, str)  # Sends progress percentage and status message

    def __init__(self, email, password):
        super().__init__()
        self.email = email
        self.password = password

    def run(self):
        try:
            print(Fore.LIGHTGREEN_EX + "[+]" + Fore.LIGHTCYAN_EX + "Trying to login...")
            cl = Client()
            self.status_signal.emit(10, "Connecting...")
            try:
                cl.login(self.email, self.password)
                self.status_signal.emit(100, "Login successful")
            except Exception as e:
                self.status_signal.emit(0, "ERROR: " + str(e))
        except Exception as e:
            self.status_signal.emit(0, "ERROR: " + str(e))

from PySide6.QtCore import QThread, Signal

class ProfileInfoWorker(QThread):
    info_signal = Signal(object, object)  # Sends profile info dictionary

    def __init__(self, client, target_name):
        super().__init__()
        self.cl = client
        self.target_name = target_name

    def run(self):
        print("Connected.")
        target_id = self.cl.user_id_from_username(self.target_name)
        print("1")
        profile_info = self.cl.user_info(target_id)
        properties = ['profile_pic_url_hd', 'account_type', 'address_street', 'biography', 'contact_phone_number',
                      'follower_count', 'following_count', 'full_name', 'public_email', 'is_verified']
        print("2")
        data = {}
        print("3")
        for prop in tqdm(properties):
            data[prop] = getattr(profile_info, prop)
            if data[prop] is None:
                data[prop] = "This information is not available / provided"
            if prop == 'is_verified':
                data[prop] = "Yes" if data[prop] else "No"
        print("4")
        medias = self.cl.user_medias(target_id)
        images = []
        for item in medias:
            if not item.thumbnail_url is None:
                images.append(item.thumbnail_url)

        print("5")
        self.info_signal.emit(data, images)

class DownloadImagesWorker(QThread):
    progress_signal = Signal(int)  # Sends download progress

    def __init__(self, images):
        super().__init__()
        self.images = images

    def run(self):
        counter = 0
        for image in self.images:
            wget.download(image, out="output/")
            counter += 1
            self.progress_signal.emit(counter)



class Widget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.login_worker = None
        self.z = Fore.LIGHTGREEN_EX + "[+]"
        self.ui = Ui_Form()
        self.ui.setupUi(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())








