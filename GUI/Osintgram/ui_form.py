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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QProgressBar, QPushButton,
    QSizePolicy, QWidget)

class Ui_Osintgram(object):
    def setupUi(self, Osintgram):
        if not Osintgram.objectName():
            Osintgram.setObjectName(u"Osintgram")
        Osintgram.resize(1049, 371)
        Osintgram.setStyleSheet(u"color: white;\n"
"background-color: rgb(56, 56, 56)")
        self.gridLayout_6 = QGridLayout(Osintgram)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.groupBox = QGroupBox(Osintgram)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineedit_password = QLineEdit(self.groupBox)
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

        self.horizontalLayout_2.addWidget(self.lineedit_password)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineedit_username = QLineEdit(self.groupBox)
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

        self.button_login = QPushButton(self.groupBox)
        self.button_login.setObjectName(u"button_login")
        self.button_login.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.button_login, 2, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox, 0, 0, 1, 2)

        self.groupBox_3 = QGroupBox(Osintgram)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineedit_hashtag = QLineEdit(self.groupBox_3)
        self.lineedit_hashtag.setObjectName(u"lineedit_hashtag")
        self.lineedit_hashtag.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_4.addWidget(self.lineedit_hashtag)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineedit_target = QLineEdit(self.groupBox_3)
        self.lineedit_target.setObjectName(u"lineedit_target")
        self.lineedit_target.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_3.addWidget(self.lineedit_target)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_3, 0, 2, 1, 1)

        self.groupBox_2 = QGroupBox(Osintgram)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.button_igtv = QPushButton(self.groupBox_2)
        self.button_igtv.setObjectName(u"button_igtv")
        self.button_igtv.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_3.addWidget(self.button_igtv, 1, 0, 1, 1)

        self.button_photos = QPushButton(self.groupBox_2)
        self.button_photos.setObjectName(u"button_photos")
        self.button_photos.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_3.addWidget(self.button_photos, 0, 0, 1, 1)

        self.button_album = QPushButton(self.groupBox_2)
        self.button_album.setObjectName(u"button_album")
        self.button_album.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_3.addWidget(self.button_album, 3, 0, 1, 1)

        self.button_stories = QPushButton(self.groupBox_2)
        self.button_stories.setObjectName(u"button_stories")
        self.button_stories.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_3.addWidget(self.button_stories, 2, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.groupBox_4 = QGroupBox(Osintgram)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.lineedit_album = QLineEdit(self.groupBox_4)
        self.lineedit_album.setObjectName(u"lineedit_album")
        self.lineedit_album.setStyleSheet(u"QLineEdit {\n"
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
        self.lineedit_album.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.lineedit_album)


        self.gridLayout_4.addLayout(self.horizontalLayout_8, 3, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lineedit_current_message = QLineEdit(self.groupBox_4)
        self.lineedit_current_message.setObjectName(u"lineedit_current_message")
        self.lineedit_current_message.setStyleSheet(u"QLineEdit {\n"
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
        self.lineedit_current_message.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.lineedit_current_message)


        self.gridLayout_4.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.lineedit_igtv = QLineEdit(self.groupBox_4)
        self.lineedit_igtv.setObjectName(u"lineedit_igtv")
        self.lineedit_igtv.setStyleSheet(u"QLineEdit {\n"
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
        self.lineedit_igtv.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.lineedit_igtv)


        self.gridLayout_4.addLayout(self.horizontalLayout_9, 2, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.lineedit_media = QLineEdit(self.groupBox_4)
        self.lineedit_media.setObjectName(u"lineedit_media")
        self.lineedit_media.setStyleSheet(u"QLineEdit {\n"
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
        self.lineedit_media.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.lineedit_media)


        self.gridLayout_4.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.groupBox_4)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10)

        self.lineedit_total_stories = QLineEdit(self.groupBox_4)
        self.lineedit_total_stories.setObjectName(u"lineedit_total_stories")
        self.lineedit_total_stories.setStyleSheet(u"QLineEdit {\n"
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
        self.lineedit_total_stories.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.lineedit_total_stories)


        self.gridLayout_4.addLayout(self.horizontalLayout_10, 0, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.lineedit_total_photos = QLineEdit(self.groupBox_4)
        self.lineedit_total_photos.setObjectName(u"lineedit_total_photos")
        self.lineedit_total_photos.setStyleSheet(u"QLineEdit {\n"
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
        self.lineedit_total_photos.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.lineedit_total_photos)


        self.gridLayout_4.addLayout(self.horizontalLayout_7, 1, 1, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_4, 1, 1, 1, 2)

        self.groupBox_5 = QGroupBox(Osintgram)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_5 = QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.progressBar = QProgressBar(self.groupBox_5)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    background-color: #F0F0F0; /* Hellgrauer Hintergrund */\n"
"	text-align: center;\n"
"	color: rgb(230, 97, 0);\n"
"	border: color grey;\n"
"	border-width: 6;\n"
"	border-radius: 12px;\n"
"	color: black;\n"
"	\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(26, 95, 180); /* Gr\u00fcn als Vordergrundfarbe */\n"
"	border-radius: 12px;\n"
"}\n"
"")
        self.progressBar.setValue(0)

        self.gridLayout_5.addWidget(self.progressBar, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_5, 2, 0, 1, 3)


        self.retranslateUi(Osintgram)

        QMetaObject.connectSlotsByName(Osintgram)
    # setupUi

    def retranslateUi(self, Osintgram):
        Osintgram.setWindowTitle(QCoreApplication.translate("Osintgram", u"Osintgram 1.2 by EchterAlsFake", None))
        self.groupBox.setTitle(QCoreApplication.translate("Osintgram", u"Login (for Private accounts)", None))
        self.label_2.setText(QCoreApplication.translate("Osintgram", u"Password: ", None))
        self.lineedit_password.setText("")
        self.label.setText(QCoreApplication.translate("Osintgram", u"Username: ", None))
        self.button_login.setText(QCoreApplication.translate("Osintgram", u"Login", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Osintgram", u"User Input", None))
        self.label_4.setText(QCoreApplication.translate("Osintgram", u"Hashtag: ", None))
        self.label_3.setText(QCoreApplication.translate("Osintgram", u"Target:    ", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Osintgram", u"Target Media section: ", None))
        self.button_igtv.setText(QCoreApplication.translate("Osintgram", u"Get IGTV", None))
        self.button_photos.setText(QCoreApplication.translate("Osintgram", u"Get photos", None))
        self.button_album.setText(QCoreApplication.translate("Osintgram", u"Get Albums", None))
        self.button_stories.setText(QCoreApplication.translate("Osintgram", u"Get stories", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Osintgram", u"Status reports:", None))
        self.label_8.setText(QCoreApplication.translate("Osintgram", u"Target's total albums: ", None))
        self.label_5.setText(QCoreApplication.translate("Osintgram", u"Current message: ", None))
        self.label_9.setText(QCoreApplication.translate("Osintgram", u"Target's total IGTV: ", None))
        self.label_6.setText(QCoreApplication.translate("Osintgram", u"Target's total media: ", None))
        self.label_10.setText(QCoreApplication.translate("Osintgram", u"Target's total stories: ", None))
        self.label_7.setText(QCoreApplication.translate("Osintgram", u"Target's total photos: ", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Osintgram", u"Progressbar:", None))
    # retranslateUi

