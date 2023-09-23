# This Python file uses the following encoding: utf-8
import sys
from instagrapi import Client
from instagrapi import exceptions

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Osintgram


class Osintgram(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Osintgram()
        self.ui.setupUi(self)
        self.c = Client()
        self.username = None
        self.buttons_pressed()

    def buttons_pressed(self):
        self.ui.button_login.clicked.connect(self.login)




    def ui_popup(self, text):
        qmsg_box = QMessageBox()
        qmsg_box.setText(str(text))
        qmsg_box.show()


    def login(self):
        username = self.ui.lineedit_username.text()
        password = self.ui.lineedit_password.text()

        try:
            self.c.login(username, password)
            session_id = self.c.sessionid
            self.ui_popup("Successfully logged in, saved Session ID for next startup.")

        except exceptions.BadPassword:
            self.ui_popup(text="Invalid Credentials. Please try again!")


    def get_user_id(self):
        self.username = self.ui.lineedit_target()
        return self.c.user_id_from_username(username=self.username)


    def get_media_raw(self):
        medias = self.c.user_medias(user_id=self.get_user_id())
        for media in medias:

















if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Osintgram()
    widget.show()
    sys.exit(app.exec())
