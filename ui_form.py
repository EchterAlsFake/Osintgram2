# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QProgressBar, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Inst_downloader_widget(object):
    def setupUi(self, Inst_downloader_widget):
        if not Inst_downloader_widget.objectName():
            Inst_downloader_widget.setObjectName(u"Inst_downloader_widget")
        Inst_downloader_widget.resize(693, 430)
        self.widget = QWidget(Inst_downloader_widget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-1, 9, 194, 31))
        self.email_horizontal_layout = QHBoxLayout(self.widget)
        self.email_horizontal_layout.setObjectName(u"email_horizontal_layout")
        self.email_horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.email_horizontal_layout.addWidget(self.label_2)

        self.line_edit_email = QLineEdit(self.widget)
        self.line_edit_email.setObjectName(u"line_edit_email")

        self.email_horizontal_layout.addWidget(self.line_edit_email)

        self.widget1 = QWidget(Inst_downloader_widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(200, 10, 307, 29))
        self.password_login_layout = QHBoxLayout(self.widget1)
        self.password_login_layout.setObjectName(u"password_login_layout")
        self.password_login_layout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")

        self.password_login_layout.addWidget(self.label_3)

        self.line_edit_password = QLineEdit(self.widget1)
        self.line_edit_password.setObjectName(u"line_edit_password")
        self.line_edit_password.setEchoMode(QLineEdit.Password)

        self.password_login_layout.addWidget(self.line_edit_password)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.password_login_layout.addLayout(self.horizontalLayout_2)

        self.push_button_login = QPushButton(self.widget1)
        self.push_button_login.setObjectName(u"push_button_login")

        self.password_login_layout.addWidget(self.push_button_login)

        self.widget2 = QWidget(Inst_downloader_widget)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(-1, 101, 284, 27))
        self.target_horizontal_layout = QHBoxLayout(self.widget2)
        self.target_horizontal_layout.setObjectName(u"target_horizontal_layout")
        self.target_horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.target_label = QLabel(self.widget2)
        self.target_label.setObjectName(u"target_label")

        self.target_horizontal_layout.addWidget(self.target_label)

        self.line_edit_target = QLineEdit(self.widget2)
        self.line_edit_target.setObjectName(u"line_edit_target")

        self.target_horizontal_layout.addWidget(self.line_edit_target)

        self.push_button_submit = QPushButton(self.widget2)
        self.push_button_submit.setObjectName(u"push_button_submit")

        self.target_horizontal_layout.addWidget(self.push_button_submit)

        self.widget3 = QWidget(Inst_downloader_widget)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(0, 360, 691, 65))
        self.verticalLayout_2 = QVBoxLayout(self.widget3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_information = QLabel(self.widget3)
        self.label_information.setObjectName(u"label_information")

        self.verticalLayout_2.addWidget(self.label_information)

        self.two_fa_information_label = QLabel(self.widget3)
        self.two_fa_information_label.setObjectName(u"two_fa_information_label")

        self.verticalLayout_2.addWidget(self.two_fa_information_label)

        self.developer_info_label = QLabel(self.widget3)
        self.developer_info_label.setObjectName(u"developer_info_label")

        self.verticalLayout_2.addWidget(self.developer_info_label)

        self.widget4 = QWidget(Inst_downloader_widget)
        self.widget4.setObjectName(u"widget4")
        self.widget4.setGeometry(QRect(0, 40, 479, 50))
        self.verticalLayout = QVBoxLayout(self.widget4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.program_stuck_label = QLabel(self.widget4)
        self.program_stuck_label.setObjectName(u"program_stuck_label")

        self.verticalLayout.addWidget(self.program_stuck_label)

        self.prgressbar_login = QProgressBar(self.widget4)
        self.prgressbar_login.setObjectName(u"prgressbar_login")
        self.prgressbar_login.setValue(0)

        self.verticalLayout.addWidget(self.prgressbar_login)

        self.meta_information_label = QLabel(Inst_downloader_widget)
        self.meta_information_label.setObjectName(u"meta_information_label")
        self.meta_information_label.setGeometry(QRect(0, 130, 115, 17))
        self.widget5 = QWidget(Inst_downloader_widget)
        self.widget5.setObjectName(u"widget5")
        self.widget5.setGeometry(QRect(0, 150, 351, 21))
        self.horizontalLayout = QHBoxLayout(self.widget5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.id_label = QLabel(self.widget5)
        self.id_label.setObjectName(u"id_label")

        self.horizontalLayout.addWidget(self.id_label)

        self.line_edit_id = QLineEdit(self.widget5)
        self.line_edit_id.setObjectName(u"line_edit_id")

        self.horizontalLayout.addWidget(self.line_edit_id)

        self.widget6 = QWidget(Inst_downloader_widget)
        self.widget6.setObjectName(u"widget6")
        self.widget6.setGeometry(QRect(0, 170, 351, 21))
        self.horizontalLayout_3 = QHBoxLayout(self.widget6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.full_name_label = QLabel(self.widget6)
        self.full_name_label.setObjectName(u"full_name_label")

        self.horizontalLayout_3.addWidget(self.full_name_label)

        self.line_edit_full_name = QLineEdit(self.widget6)
        self.line_edit_full_name.setObjectName(u"line_edit_full_name")

        self.horizontalLayout_3.addWidget(self.line_edit_full_name)

        self.widget7 = QWidget(Inst_downloader_widget)
        self.widget7.setObjectName(u"widget7")
        self.widget7.setGeometry(QRect(0, 190, 351, 21))
        self.horizontalLayout_5 = QHBoxLayout(self.widget7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.total_images_label = QLabel(self.widget7)
        self.total_images_label.setObjectName(u"total_images_label")

        self.horizontalLayout_5.addWidget(self.total_images_label)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.line_edit_total_images = QLineEdit(self.widget7)
        self.line_edit_total_images.setObjectName(u"line_edit_total_images")

        self.horizontalLayout_4.addWidget(self.line_edit_total_images)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.widget8 = QWidget(Inst_downloader_widget)
        self.widget8.setObjectName(u"widget8")
        self.widget8.setGeometry(QRect(0, 210, 351, 27))
        self.horizontalLayout_6 = QHBoxLayout(self.widget8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.follower_count_label = QLabel(self.widget8)
        self.follower_count_label.setObjectName(u"follower_count_label")

        self.horizontalLayout_6.addWidget(self.follower_count_label)

        self.line_edit_follower_count = QLineEdit(self.widget8)
        self.line_edit_follower_count.setObjectName(u"line_edit_follower_count")

        self.horizontalLayout_6.addWidget(self.line_edit_follower_count)

        self.widget9 = QWidget(Inst_downloader_widget)
        self.widget9.setObjectName(u"widget9")
        self.widget9.setGeometry(QRect(0, 240, 351, 27))
        self.horizontalLayout_7 = QHBoxLayout(self.widget9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.following_label = QLabel(self.widget9)
        self.following_label.setObjectName(u"following_label")

        self.horizontalLayout_7.addWidget(self.following_label)

        self.line_edit_following_count = QLineEdit(self.widget9)
        self.line_edit_following_count.setObjectName(u"line_edit_following_count")

        self.horizontalLayout_7.addWidget(self.line_edit_following_count)

        self.widget10 = QWidget(Inst_downloader_widget)
        self.widget10.setObjectName(u"widget10")
        self.widget10.setGeometry(QRect(0, 270, 351, 27))
        self.horizontalLayout_8 = QHBoxLayout(self.widget10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verified_label = QLabel(self.widget10)
        self.verified_label.setObjectName(u"verified_label")

        self.horizontalLayout_8.addWidget(self.verified_label)

        self.line_edit_verified = QLineEdit(self.widget10)
        self.line_edit_verified.setObjectName(u"line_edit_verified")

        self.horizontalLayout_8.addWidget(self.line_edit_verified)

        self.widget11 = QWidget(Inst_downloader_widget)
        self.widget11.setObjectName(u"widget11")
        self.widget11.setGeometry(QRect(0, 300, 691, 27))
        self.horizontalLayout_9 = QHBoxLayout(self.widget11)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.push_buton_download_photos = QPushButton(self.widget11)
        self.push_buton_download_photos.setObjectName(u"push_buton_download_photos")

        self.horizontalLayout_9.addWidget(self.push_buton_download_photos)

        self.push_button_download_propic = QPushButton(self.widget11)
        self.push_button_download_propic.setObjectName(u"push_button_download_propic")

        self.horizontalLayout_9.addWidget(self.push_button_download_propic)

        self.widget12 = QWidget(Inst_downloader_widget)
        self.widget12.setObjectName(u"widget12")
        self.widget12.setGeometry(QRect(0, 330, 691, 27))
        self.horizontalLayout_10 = QHBoxLayout(self.widget12)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.progressbar_photos = QProgressBar(self.widget12)
        self.progressbar_photos.setObjectName(u"progressbar_photos")
        self.progressbar_photos.setValue(0)

        self.horizontalLayout_10.addWidget(self.progressbar_photos)

        self.progressbar_propic = QProgressBar(self.widget12)
        self.progressbar_propic.setObjectName(u"progressbar_propic")
        self.progressbar_propic.setValue(0)

        self.horizontalLayout_10.addWidget(self.progressbar_propic)
        self.line_edit_id.setDisabled(True)
        self.line_edit_total_images.setDisabled(True)
        self.line_edit_full_name.setDisabled(True)
        self.line_edit_follower_count.setDisabled(True)
        self.line_edit_following_count.setDisabled(True)
        self.line_edit_verified.setDisabled(True)
        self.line_edit_target.setDisabled(True)
        self.line_edit_target.setText("Login first!")


        self.retranslateUi(Inst_downloader_widget)

        QMetaObject.connectSlotsByName(Inst_downloader_widget)
    # setupUi

    def retranslateUi(self, Inst_downloader_widget):
        Inst_downloader_widget.setWindowTitle(QCoreApplication.translate("Inst_downloader_widget", u"Widget", None))
        self.label_2.setText(QCoreApplication.translate("Inst_downloader_widget", u"Email: ", None))
        self.label_3.setText(QCoreApplication.translate("Inst_downloader_widget", u"Password:", None))
        self.push_button_login.setText(QCoreApplication.translate("Inst_downloader_widget", u"Login", None))
        self.target_label.setText(QCoreApplication.translate("Inst_downloader_widget", u"Target:", None))
        self.push_button_submit.setText(QCoreApplication.translate("Inst_downloader_widget", u"Submit", None))
        self.label_information.setText(QCoreApplication.translate("Inst_downloader_widget", u"Information: ", None))
        self.two_fa_information_label.setText(QCoreApplication.translate("Inst_downloader_widget", u"2FA Information:  2FA is not working. I am  trying to fix that, but I probably won't get it to work sorry :(", None))
        self.developer_info_label.setText(QCoreApplication.translate("Inst_downloader_widget", u"Made by EchterAlsFake - https://github.com/EchterAlsFake/Instagram_Downloader    License: GNU3", None))
        self.program_stuck_label.setText(QCoreApplication.translate("Inst_downloader_widget", u"Note:  If the program gets stuck:  Just wait!   It's running in background.", None))
        self.meta_information_label.setText(QCoreApplication.translate("Inst_downloader_widget", u"Metainformation", None))
        self.id_label.setText(QCoreApplication.translate("Inst_downloader_widget", u"ID: ", None))
        self.full_name_label.setText(QCoreApplication.translate("Inst_downloader_widget", u"Full Name:", None))
        self.total_images_label.setText(QCoreApplication.translate("Inst_downloader_widget", u"Total images:", None))
        self.follower_count_label.setText(QCoreApplication.translate("Inst_downloader_widget", u"Follower count:", None))
        self.following_label.setText(QCoreApplication.translate("Inst_downloader_widget", u"Following count:", None))
        self.verified_label.setText(QCoreApplication.translate("Inst_downloader_widget", u"Verified: ", None))
        self.push_buton_download_photos.setText(QCoreApplication.translate("Inst_downloader_widget", u"Download Photos", None))
        self.push_button_download_propic.setText(QCoreApplication.translate("Inst_downloader_widget", u"Download Profile Picture URL (HD)", None))
    # retranslateUi

