# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Login_Widget(object):
    def setupUi(self, Login_Widget):
        if not Login_Widget.objectName():
            Login_Widget.setObjectName(u"Login_Widget")
        Login_Widget.resize(655, 107)
        Login_Widget.setStyleSheet(u"background-color: black;\n"
"border-radius: 5px;")
        self.gridLayout = QGridLayout(Login_Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_username = QLabel(Login_Widget)
        self.label_username.setObjectName(u"label_username")
        self.label_username.setStyleSheet(u"color: white;")

        self.horizontalLayout.addWidget(self.label_username)

        self.lineedit_username = QLineEdit(Login_Widget)
        self.lineedit_username.setObjectName(u"lineedit_username")
        self.lineedit_username.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #757575;\n"
"    border-radius: 12px;\n"
"    padding: 0 8px;\n"
"    background: rgb(94, 92, 100);  /* setzt den Hintergrund auf Schwarz */\n"
"    color: #FFFFFF;  /* setzt die Textfarbe auf Wei\u00df */\n"
"    font-size: 16px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: rgb(107, 0, 255)\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background: #444444;  /* setzt den Hintergrund auf ein dunkles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    color: #aaaaaa;  /* setzt die Textfarbe auf ein helles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    border-color: #aaaaaa;\n"
"}")

        self.horizontalLayout.addWidget(self.lineedit_username)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_password = QLabel(Login_Widget)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setStyleSheet(u"color: white;")

        self.horizontalLayout_2.addWidget(self.label_password)

        self.lineedit_password = QLineEdit(Login_Widget)
        self.lineedit_password.setObjectName(u"lineedit_password")
        self.lineedit_password.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #757575;\n"
"    border-radius: 12px;\n"
"    padding: 0 8px;\n"
"    background: rgb(94, 92, 100);  /* setzt den Hintergrund auf Schwarz */\n"
"    color: #FFFFFF;  /* setzt die Textfarbe auf Wei\u00df */\n"
"    font-size: 16px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: rgb(107, 0, 255)\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background: #444444;  /* setzt den Hintergrund auf ein dunkles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    color: #aaaaaa;  /* setzt die Textfarbe auf ein helles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    border-color: #aaaaaa;\n"
"}")
        self.lineedit_password.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.lineedit_password)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.pushButton = QPushButton(Login_Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"        background-color: #5a2a82; /* base violet color */\n"
"        color: #ffffff; /* white text */\n"
"        border: none;\n"
"        border-radius: 10px; /* reduced rounded corner radius */\n"
"        padding: 5px 10px; /* reduced button padding */\n"
"        font-size: 12px;\n"
"        outline: none;\n"
"    }\n"
"    \n"
"    QPushButton:hover {\n"
"        background-color: #7b3ca3; /* slightly lighter violet when hovered */\n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: #481f61; /* darker violet when pressed */\n"
"    }\n"
"\n"
"    QPushButton:disabled {\n"
"        background-color: #3f1d4d; /* even darker shade when button is disabled */\n"
"        color: #8a7b9a; /* greyish text */\n"
"    }")

        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)


        self.retranslateUi(Login_Widget)

        QMetaObject.connectSlotsByName(Login_Widget)
    # setupUi

    def retranslateUi(self, Login_Widget):
        Login_Widget.setWindowTitle(QCoreApplication.translate("Login_Widget", u"Widget", None))
        self.label_username.setText(QCoreApplication.translate("Login_Widget", u"Username:", None))
        self.label_password.setText(QCoreApplication.translate("Login_Widget", u"Password:", None))
        self.pushButton.setText(QCoreApplication.translate("Login_Widget", u"Login", None))
    # retranslateUi

