# This is the extension for the widget.py
# Please don't change, except you know what you are doing.
# License: GPLv3
import wget
from instagrapi import Client
from colorama import *
from tqdm import tqdm
from ui_form import Ui_Inst_downloader_widget
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
        self.ui = Ui_Inst_downloader_widget()
        self.ui.setupUi(self)
        self.ui.push_buton_download_photos.setDisabled(True)
        self.ui.push_button_download_propic.setDisabled(True)
        self.ui.push_button_submit.setDisabled(True)
        self.ui.push_button_login.clicked.connect(self.login)
        self.ui.push_button_submit.clicked.connect(self.get_profile_info)
        self.ui.push_buton_download_photos.clicked.connect(self.download_images)
        self.ui.push_button_download_propic.clicked.connect(self.download_propic)
        self.cl = Client()
        if os.path.isdir("output"):
            pass

        elif not os.path.isdir("output"):
            os.mkdir("output")


    def login(self):
        email = self.ui.line_edit_email.text()
        password = self.ui.line_edit_password.text()

        # Create worker
        self.login_worker = LoginWorker(email, password)
        # Connect worker signal to slot
        self.login_worker.status_signal.connect(self.update_login_status)
        # Start worker
        self.login_worker.start()

    def update_login_status(self, progress, status):
        self.ui.prgressbar_login.setValue(progress)
        print(status)
        if progress == 100:
            self.ui.line_edit_target.setDisabled(False)
            self.ui.line_edit_target.clear()
            self.ui.push_button_submit.setDisabled(False)

    def get_profile_info(self):
        self.target_name = self.ui.line_edit_target.text()
        self.target_id = self.cl.user_id_from_username(self.target_name)
        self.ui.line_edit_id.setText(str(self.target_id))

        # Create worker
        self.profile_info_worker = ProfileInfoWorker(self.cl, self.target_name)
        # Connect worker signal to slot
        self.profile_info_worker.info_signal.connect(self.update_profile_info)
        # Start worker
        self.profile_info_worker.start()

    def update_profile_info(self, data, images):
        self.data = data
        self.images = images
        # Update UI with data...
        # ...
        self.ui.line_edit_full_name.setText(str(self.data['full_name']))
        self.ui.line_edit_verified.setText(str(self.data['is_verified']))
        self.ui.line_edit_follower_count.setText(str(self.data['follower_count']))
        self.ui.line_edit_following_count.setText(str(self.data['following_count']))
        self.ui.line_edit_total_images.setText(str(len(self.images)))
        self.ui.progressbar_photos.setMaximum(len(self.images))
        self.ui.push_buton_download_photos.setDisabled(False)
        self.ui.push_button_download_propic.setDisabled(False)

    def download_images(self):
        # Create worker
        self.download_images_worker = DownloadImagesWorker(self.images)
        # Connect worker signal to slot
        self.download_images_worker.progress_signal.connect(self.update_download_progress)
        # Start worker
        self.download_images_worker.start()

    def update_download_progress(self, progress):
        self.ui.progressbar_photos.setValue(progress)

    def download_propic(self):

        self.ui.progressbar_propic.setValue(0)
        url = self.data['profile_pic_url_hd']
        wget.download(url, out="output/")
        self.ui.progressbar_propic.setValue(100)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())








