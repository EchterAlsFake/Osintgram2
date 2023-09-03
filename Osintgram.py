"""

Copyright (C) 2023  Johannes Habel | EchterAlsFake

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# This Python file uses the following encoding: utf-8
import sys
import os
import json
from src.logger import logger
from instagrapi import Client
from instagrapi.mixins.challenge import ChallengeChoice

from PySide6.QtWidgets import QApplication, QWidget, QInputDialog

# Important:
# You need to run the following command to generate the ui_login_form.py file
#     pyside6-uic form.ui -o ui_login_form.py, or
#     pyside2-uic form.ui -o ui_login_form.py
from src.ui_login_form import Ui_Login_Widget


"""
Important information:

The 2FA feature is disabled, because it is NOT working.
(at least for me)

If you have 2FA via SMS or Email, you can enable it by setting

'enable_experimental_two_factor_authentication' = True

Just use the usual log in procedure and you will be prompted 
to enter the 2FA code.

If you get a 401, 400, or 405 Error, please disable it back to default.
The codes will be send in english language.

"""

enable_experimental_two_factor_authentication = False


class Widget_LogIn(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cl = Client()
        if enable_experimental_two_factor_authentication:
            self.cl.challenge_code_handler = self.challenge_code_handler

        self.ui = Ui_Login_Widget()
        self.ui.setupUi(self)
        self.session_id_value = None
        self.session_token()

        self.ui.pushButton.clicked.connect(self.login)


    def get_2fa_code(self, text):
        print("Executed")
        text, ok = QInputDialog.getText(self, "Two Factor Authentication Code", text)
        self.show()
        if ok and text:
            return text

        else:
            return False

    def challenge_code_handler(self, username, choice):
        print("Executed")
        if choice == ChallengeChoice.SMS:
            print("Executed")
            return self.get_2fa_code(text="Enter 2FA from your SMS:")

        elif choice == ChallengeChoice.EMAIL:
            print("Executed")
            return self.get_2fa_code(text="Enter 2FA from your Email:")

    def session_token(self):
        if os.path.isfile("session.json"):

            with open("session.json", "r") as file:
                session_data = json.load(file)

            self.session_id_value = session_data["session_id"]
            logger(msg=f"Found Session Token: {self.session_id_value}")
            self.login(session_id=self.session_id_value)

    def create_session_file(self, session_id):
        session_data = {
            "session_id": session_id
        }

        with open("session.json", "w") as file:
            json.dump(session_data, file)


    def login(self, session_id=False):

        if session_id is False:
            logger("Trying to Login...")
            password = self.ui.lineedit_password.text()
            username = self.ui.lineedit_username.text()

            self.cl.login(username, password)
            logger(msg=f"Login Success!   User: {self.cl.user_id}")

            if os.path.isfile("session.json"):
                os.remove("session.json")

            session = self.cl.sessionid
            logger(msg=f"Found Session Token: {session} Saving for net login...")
            self.create_session_file(session)


        else:
            self.cl.login_by_sessionid(str(session_id))

        Osintgram(client=self.cl)


class Osintgram:

    def __init__(self, client):
        super().__init__()














if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget_LogIn()
    widget.show()
    sys.exit(app.exec())








