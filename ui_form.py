# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QProgressBar, QPushButton,
    QSizePolicy, QWidget)

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(664, 384)
        widget.setStyleSheet(u"background-color: black;")
        self.formLayout_3 = QFormLayout(widget)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.groupBox_2 = QGroupBox(widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"color: white;")
        self.formLayout_2 = QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.button_download_comments = QPushButton(self.groupBox_2)
        self.button_download_comments.setObjectName(u"button_download_comments")
        self.button_download_comments.setStyleSheet(u"QPushButton {\n"
"    background-color: #5468ff;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    color: #fff;QPushButton {\n"
"    background-color: #5468ff;\n"
"	margin-bottom: 8px;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    color: #fff;\n"
"    font-family: \"JetBrains Mono\", monospace;\n"
"    font-size: 15px;\n"
"    padding: 0px 16px 0px 16px;\n"
"    height: 24px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3c4fe0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c4fe0;\n"
"}\n"
"\n"
"    font-family: \"JetBrains Mono\", monospace;\n"
"    font-size: 15px;\n"
"    padding: 0px 18px 0px 17px;\n"
"    height: 24px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3c4fe0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c4fe0;\n"
"}")

        self.horizontalLayout_5.addWidget(self.button_download_comments)

        self.progressbar_comments = QProgressBar(self.groupBox_2)
        self.progressbar_comments.setObjectName(u"progressbar_comments")
        self.progressbar_comments.setValue(0)

        self.horizontalLayout_5.addWidget(self.progressbar_comments)


        self.formLayout_2.setLayout(1, QFormLayout.SpanningRole, self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.button_photos = QPushButton(self.groupBox_2)
        self.button_photos.setObjectName(u"button_photos")
        self.button_photos.setLayoutDirection(Qt.LeftToRight)
        self.button_photos.setAutoFillBackground(False)
        self.button_photos.setStyleSheet(u"QPushButton {\n"
"    background-color: #5468ff;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    color: #fff;QPushButton {\n"
"    background-color: #5468ff;\n"
"	margin-bottom: 8px;\n"
"	margin-right: 20px;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    color: #fff;\n"
"	text-align: center;\n"
"    font-family: \"JetBrains Mono\", monospace;\n"
"    font-size: 15px;\n"
"    padding: 20px 20px 20px 20px;\n"
"    height: 24px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3c4fe0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c4fe0;\n"
"}\n"
"\n"
"    font-family: \"JetBrains Mono\", monospace;\n"
"    font-size: 15px;\n"
"    padding: 0px 18px 0px 17px;\n"
"    height: 24px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3c4fe0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c4fe0;\n"
"}")

        self.horizontalLayout_4.addWidget(self.button_photos)

        self.progressbar_photos = QProgressBar(self.groupBox_2)
        self.progressbar_photos.setObjectName(u"progressbar_photos")
        self.progressbar_photos.setStyleSheet(u"\n"
"text-align: center;")
        self.progressbar_photos.setValue(0)

        self.horizontalLayout_4.addWidget(self.progressbar_photos)


        self.formLayout_2.setLayout(2, QFormLayout.SpanningRole, self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.button_profile_pic = QPushButton(self.groupBox_2)
        self.button_profile_pic.setObjectName(u"button_profile_pic")
        self.button_profile_pic.setStyleSheet(u"QPushButton {\n"
"    background-color: #5468ff;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    color: #fff;QPushButton {\n"
"    background-color: #5468ff;\n"
"	margin-bottom: 8px;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    color: #fff;\n"
"    font-family: \"JetBrains Mono\", monospace;\n"
"    font-size: 15px;\n"
"    padding: 0px 16px 0px 16px;\n"
"    height: 24px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3c4fe0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c4fe0;\n"
"}\n"
"\n"
"    font-family: \"JetBrains Mono\", monospace;\n"
"    font-size: 15px;\n"
"    padding: 0px 18px 0px 17px;\n"
"    height: 24px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3c4fe0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c4fe0;\n"
"}")

        self.horizontalLayout_6.addWidget(self.button_profile_pic)

        self.progressbar_profile_pic = QProgressBar(self.groupBox_2)
        self.progressbar_profile_pic.setObjectName(u"progressbar_profile_pic")
        self.progressbar_profile_pic.setStyleSheet(u"margin-left: 3px;\n"
"text-align: center;")
        self.progressbar_profile_pic.setValue(0)

        self.horizontalLayout_6.addWidget(self.progressbar_profile_pic)


        self.formLayout_2.setLayout(3, QFormLayout.SpanningRole, self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_status = QLabel(self.groupBox_2)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setStyleSheet(u"color: white")

        self.horizontalLayout_7.addWidget(self.label_status)

        self.lineedit_status = QLineEdit(self.groupBox_2)
        self.lineedit_status.setObjectName(u"lineedit_status")
        self.lineedit_status.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #757575;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    background: rgb(94, 92, 100);  /* setzt den Hintergrund auf Schwarz */\n"
"    color: #FFFFFF;  /* setzt die Textfarbe auf Wei\u00df */\n"
"    font-size: 16px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #4a90d9;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background: #444444;  /* setzt den Hintergrund auf ein dunkles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    color: #aaaaaa;  /* setzt die Textfarbe auf ein helles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    border-color: #aaaaaa;\n"
"}")

        self.horizontalLayout_7.addWidget(self.lineedit_status)


        self.formLayout_2.setLayout(4, QFormLayout.SpanningRole, self.horizontalLayout_7)

        self.button_locations = QPushButton(self.groupBox_2)
        self.button_locations.setObjectName(u"button_locations")
        self.button_locations.setStyleSheet(u"QPushButton {\n"
"    background-color: #5468ff;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    color: #fff;QPushButton {\n"
"    background-color: #5468ff;\n"
"	margin-bottom: 8px;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    color: #fff;\n"
"    font-family: \"JetBrains Mono\", monospace;\n"
"    font-size: 15px;\n"
"    padding: 0px 16px 0px 16px;\n"
"    height: 24px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3c4fe0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c4fe0;\n"
"}\n"
"\n"
"    font-family: \"JetBrains Mono\", monospace;\n"
"    font-size: 15px;\n"
"    padding: 0px 18px 0px 17px;\n"
"    height: 24px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3c4fe0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c4fe0;\n"
"}")

        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.button_locations)


        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.groupBox_2)

        self.groupbox_login = QGroupBox(widget)
        self.groupbox_login.setObjectName(u"groupbox_login")
        self.formLayout = QFormLayout(self.groupbox_login)
        self.formLayout.setObjectName(u"formLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_email = QLabel(self.groupbox_login)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setStyleSheet(u"color: white;")

        self.horizontalLayout.addWidget(self.label_email)

        self.lineedit_email = QLineEdit(self.groupbox_login)
        self.lineedit_email.setObjectName(u"lineedit_email")
        self.lineedit_email.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #757575;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    background: rgb(94, 92, 100);  /* setzt den Hintergrund auf Schwarz */\n"
"    color: #FFFFFF;  /* setzt die Textfarbe auf Wei\u00df */\n"
"    font-size: 16px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #4a90d9;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background: #444444;  /* setzt den Hintergrund auf ein dunkles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    color: #aaaaaa;  /* setzt die Textfarbe auf ein helles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    border-color: #aaaaaa;\n"
"}")

        self.horizontalLayout.addWidget(self.lineedit_email)


        self.formLayout.setLayout(0, QFormLayout.SpanningRole, self.horizontalLayout)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_target = QLabel(self.groupbox_login)
        self.label_target.setObjectName(u"label_target")
        self.label_target.setStyleSheet(u"color: white")

        self.horizontalLayout_8.addWidget(self.label_target)

        self.lineedit_target = QLineEdit(self.groupbox_login)
        self.lineedit_target.setObjectName(u"lineedit_target")
        self.lineedit_target.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #757575;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    background: rgb(94, 92, 100);  /* setzt den Hintergrund auf Schwarz */\n"
"    color: #FFFFFF;  /* setzt die Textfarbe auf Wei\u00df */\n"
"    font-size: 16px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #4a90d9;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background: #444444;  /* setzt den Hintergrund auf ein dunkles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    color: #aaaaaa;  /* setzt die Textfarbe auf ein helles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    border-color: #aaaaaa;\n"
"}")

        self.horizontalLayout_8.addWidget(self.lineedit_target)


        self.formLayout.setLayout(3, QFormLayout.SpanningRole, self.horizontalLayout_8)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_password = QLabel(self.groupbox_login)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setStyleSheet(u"color: white")

        self.horizontalLayout_2.addWidget(self.label_password)

        self.lineedit_password = QLineEdit(self.groupbox_login)
        self.lineedit_password.setObjectName(u"lineedit_password")
        self.lineedit_password.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #757575;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    background: rgb(94, 92, 100);  /* setzt den Hintergrund auf Schwarz */\n"
"    color: #FFFFFF;  /* setzt die Textfarbe auf Wei\u00df */\n"
"    font-size: 16px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #4a90d9;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background: #444444;  /* setzt den Hintergrund auf ein dunkles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    color: #aaaaaa;  /* setzt die Textfarbe auf ein helles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    border-color: #aaaaaa;\n"
"}")
        self.lineedit_password.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.lineedit_password)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.button_login = QPushButton(self.groupbox_login)
        self.button_login.setObjectName(u"button_login")
        self.button_login.setStyleSheet(u"QPushButton {\n"
"    background-color: #5468ff;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    color: #fff;QPushButton {\n"
"    background-color: #5468ff;\n"
"	margin-bottom: 8px;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    color: #fff;\n"
"    font-family: \"JetBrains Mono\", monospace;\n"
"    font-size: 15px;\n"
"    padding: 0px 16px 0px 16px;\n"
"    height: 24px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3c4fe0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c4fe0;\n"
"}\n"
"\n"
"    font-family: \"JetBrains Mono\", monospace;\n"
"    font-size: 15px;\n"
"    padding: 0px 18px 0px 17px;\n"
"    height: 24px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3c4fe0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c4fe0;\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.button_login)


        self.formLayout.setLayout(1, QFormLayout.SpanningRole, self.horizontalLayout_3)

        self.progressbar_login = QProgressBar(self.groupbox_login)
        self.progressbar_login.setObjectName(u"progressbar_login")
        self.progressbar_login.setStyleSheet(u"color: white;")
        self.progressbar_login.setValue(0)

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.progressbar_login)


        self.formLayout_3.setWidget(0, QFormLayout.SpanningRole, self.groupbox_login)


        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"Osintgram 2.0  CC  1.0  /Version : 1", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("widget", u"Media", None))
        self.button_download_comments.setText(QCoreApplication.translate("widget", u"Download comments", None))
        self.button_photos.setText(QCoreApplication.translate("widget", u"Download photos       ", None))
        self.button_profile_pic.setText(QCoreApplication.translate("widget", u"Download profile pic ", None))
        self.label_status.setText(QCoreApplication.translate("widget", u"Status:", None))
        self.button_locations.setText(QCoreApplication.translate("widget", u"Export Locations", None))
        self.groupbox_login.setTitle("")
        self.label_email.setText(QCoreApplication.translate("widget", u"E-Mail", None))
        self.label_target.setText(QCoreApplication.translate("widget", u"Target:", None))
        self.label_password.setText(QCoreApplication.translate("widget", u"Password", None))
        self.button_login.setText(QCoreApplication.translate("widget", u"Login", None))
    # retranslateUi

