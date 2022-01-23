# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manage2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import re

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

import blackjack


class Ui_Dialog(object):
    def __init__(self, user, avatar):
        self.user = user
        self.avatarUs = avatar

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(869, 430)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(869, 430))
        Dialog.setMaximumSize(QtCore.QSize(869, 430))
        Dialog.setStyleSheet("QWidget{\n"
                             "    background: #6B5596;\n"
                             "}\n"
                             "QLineEdit {\n"
                             "    border: 2px solid gray;\n"
                             "    border-radius: 10px;\n"
                             "    padding: 0 8px;\n"
                             "    background: #CFC1D0;\n"
                             "}\n"
                             "QLabel {\n"
                             "    color: #FEFE58;\n"
                             "}\n"
                             "QPushButton{\n"
                             "    border-style: solid;\n"
                             "    border-color: #050a0e;\n"
                             "    border-width: 1px;\n"
                             "    border-radius: 5px;\n"
                             "    color: #FEFE58;\n"
                             "    padding: 2px;\n"
                             "    background-color: #100E19;\n"
                             "}\n"
                             "QPushButton::default{\n"
                             "    border-style: solid;\n"
                             "    border-color: #050a0e;\n"
                             "    border-width: 1px;\n"
                             "    border-radius: 5px;\n"
                             "    color: #FEFE58;\n"
                             "    padding: 2px;\n"
                             "    background-color: #151a1e;\n"
                             "}\n"
                             "QPushButton:hover{\n"
                             "    border-style: solid;\n"
                             "    border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #C0DB50, stop:0.4 #C0DB50, stop:0.5 #100E19, stop:1 #100E19);\n"
                             "    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #C0DB50, stop:1 #C0DB50);\n"
                             "    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);\n"
                             "    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);\n"
                             "    border-width: 2px;\n"
                             "    border-radius: 1px;\n"
                             "    color: #FEFE58;\n"
                             "    padding: 2px;\n"
                             "}\n"
                             "QPushButton:pressed{\n"
                             "    border-style: solid;\n"
                             "    border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #d33af1, stop:0.4 #d33af1, stop:0.5 #100E19, stop:1 #100E19);\n"
                             "    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #d33af1, stop:1 #d33af1);\n"
                             "    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);\n"
                             "    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);\n"
                             "    border-width: 2px;\n"
                             "    border-radius: 1px;\n"
                             "    color: #FEFE58;\n"
                             "    padding: 2px;\n"
                             "}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.saveAboutButton = QtWidgets.QPushButton(self.page_1)
        self.saveAboutButton.setGeometry(QtCore.QRect(730, 290, 101, 31))
        self.saveAboutButton.setObjectName("saveAboutButton")
        self.changePassButton = QtWidgets.QPushButton(self.page_1)
        self.changePassButton.setGeometry(QtCore.QRect(680, 360, 151, 41))
        self.changePassButton.setObjectName("changePassButton")
        self.avatar = QtWidgets.QLabel(self.page_1)
        self.avatar.setGeometry(QtCore.QRect(80, 60, 251, 251))
        self.avatar.setText("")
        self.avatar.setObjectName("avatar")
        pixmap = QPixmap('images/avatars/' + self.user.avatar).scaled(251, 251)
        self.avatar.setPixmap(pixmap)
        self.changeAvButton = QtWidgets.QPushButton(self.page_1)
        self.changeAvButton.setGeometry(QtCore.QRect(160, 330, 101, 41))
        self.changeAvButton.setObjectName("changeAvButton")
        self.label = QtWidgets.QLabel(self.page_1)
        self.label.setGeometry(QtCore.QRect(370, 10, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.req = QtWidgets.QLabel(self.page_1)
        self.req.setGeometry(QtCore.QRect(600, 20, 200, 41))
        self.req.setText("Min 5 max 200 characters (a-zA-Z0-9 )")
        self.errorLabel = QtWidgets.QLabel(self.page_1)
        self.errorLabel.setGeometry(QtCore.QRect(430, 290, 101, 41))
        self.errorLabel.setText("")
        self.aboutText = QtWidgets.QPlainTextEdit(self.page_1)
        self.aboutText.setGeometry(QtCore.QRect(430, 60, 401, 221))
        self.aboutText.setObjectName("aboutText")
        self.aboutText.setStyleSheet("QPlainTextEdit { font-size: 12px;color: #FEFE58; font-weight: bold;}")
        self.aboutText.setPlainText(str(blackjack.DataBase().getPlayer(self.user.username)["description"]))
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.page_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 831, 351))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.rb_7 = Avatar('anubis.png', self.gridLayoutWidget)
        self.rb_7.setObjectName("rb_7")
        self.gridLayout.addWidget(self.rb_7, 1, 1, 1, 1)
        self.rb_3 = Avatar('chameleon-glyph.png', self.gridLayoutWidget)
        self.rb_3.setObjectName("rb_3")
        self.gridLayout.addWidget(self.rb_3, 0, 2, 1, 1)
        self.rb_2 = Avatar('evil-bat.png', self.gridLayoutWidget)
        self.rb_2.setObjectName("rb_2")
        self.gridLayout.addWidget(self.rb_2, 0, 1, 1, 1)
        self.rb_6 = Avatar('griffin-symbol.png', self.gridLayoutWidget)
        self.rb_6.setObjectName("rb_6")
        self.gridLayout.addWidget(self.rb_6, 1, 0, 1, 1)
        self.rb_1 = Avatar('horned-reptile.png', self.gridLayoutWidget)
        self.rb_1.setObjectName("rb_1")
        self.gridLayout.addWidget(self.rb_1, 0, 0, 1, 1)
        self.rb_4 = Avatar('sasquatch.png', self.gridLayoutWidget)
        self.rb_4.setObjectName("rb_4")
        self.gridLayout.addWidget(self.rb_4, 0, 3, 1, 1)
        self.rb_5 = Avatar('sea-creature.png', self.gridLayoutWidget)
        self.rb_5.setObjectName("rb_5")
        self.gridLayout.addWidget(self.rb_5, 0, 4, 1, 1)
        self.rb_9 = Avatar('sea-dragon.png', self.gridLayoutWidget)
        self.rb_9.setObjectName("rb_9")
        self.gridLayout.addWidget(self.rb_9, 1, 3, 1, 1)
        self.rb_8 = Avatar('unicorn.png', self.gridLayoutWidget)
        self.rb_8.setObjectName("rb_8")
        self.gridLayout.addWidget(self.rb_8, 1, 2, 1, 1)
        self.rb_10 = Avatar('witch-face.png', self.gridLayoutWidget)
        self.rb_10.setObjectName("rb_10")
        self.gridLayout.addWidget(self.rb_10, 1, 4, 1, 1)
        self.saveAvButton = QtWidgets.QPushButton(self.page_2)
        self.saveAvButton.setGeometry(QtCore.QRect(740, 370, 81, 31))
        self.saveAvButton.setObjectName("saveAvButton")
        self.backToManButton1 = QtWidgets.QPushButton(self.page_2)
        self.backToManButton1.setGeometry(QtCore.QRect(14, 370, 81, 31))
        self.backToManButton1.setObjectName("backToManButton1")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_2 = QtWidgets.QLabel(self.page_3)
        self.label_2.setGeometry(QtCore.QRect(310, 30, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(170, 120, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setGeometry(QtCore.QRect(150, 180, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page_3)
        self.label_5.setGeometry(QtCore.QRect(150, 250, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.oldPass = QtWidgets.QLineEdit(self.page_3)
        self.oldPass.setGeometry(QtCore.QRect(380, 120, 301, 31))
        self.oldPass.setObjectName("oldPass")
        self.oldPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPass1 = QtWidgets.QLineEdit(self.page_3)
        self.newPass1.setGeometry(QtCore.QRect(380, 190, 301, 31))
        self.newPass1.setObjectName("newPass1")
        self.newPass1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPass2 = QtWidgets.QLineEdit(self.page_3)
        self.newPass2.setGeometry(QtCore.QRect(380, 260, 301, 31))
        self.newPass2.setObjectName("newPass2")
        self.newPass2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.savePassButton = QtWidgets.QPushButton(self.page_3)
        self.savePassButton.setGeometry(QtCore.QRect(580, 320, 101, 31))
        self.savePassButton.setObjectName("savePassButton")
        self.backToManButton2 = QtWidgets.QPushButton(self.page_3)
        self.backToManButton2.setGeometry(QtCore.QRect(10, 370, 81, 31))
        self.backToManButton2.setObjectName("backToManButton2")
        self.req2 = QtWidgets.QLabel(self.page_3)
        self.req2.setGeometry(QtCore.QRect(320, 60, 201, 51))
        self.req2.setText("Password 5 to 16 characters(a-zA-Z0-9)")
        self.errorLabel2 = QtWidgets.QLabel(self.page_3)
        self.errorLabel2.setGeometry(QtCore.QRect(180, 310, 100, 51))
        self.errorLabel2.setText("")
        self.stackedWidget.addWidget(self.page_3)
        self.horizontalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.avatarGroup = QtWidgets.QButtonGroup()
        self.avatarGroup.addButton(self.rb_1)
        self.avatarGroup.addButton(self.rb_2)
        self.avatarGroup.addButton(self.rb_3)
        self.avatarGroup.addButton(self.rb_4)
        self.avatarGroup.addButton(self.rb_5)
        self.avatarGroup.addButton(self.rb_6)
        self.avatarGroup.addButton(self.rb_7)
        self.avatarGroup.addButton(self.rb_8)
        self.avatarGroup.addButton(self.rb_9)
        self.avatarGroup.addButton(self.rb_10)

        self.backToManButton1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
        self.backToManButton2.clicked.connect(self.goToMain)
        self.changeAvButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.changePassButton.clicked.connect(self.goToChangePassword)

        self.saveAvButton.clicked.connect(self.saveAvButtonFunction)
        self.savePassButton.clicked.connect(self.savePassButtonFunction)
        self.saveAboutButton.clicked.connect(self.saveAboutButtonFunction)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.saveAboutButton.setText(_translate("Dialog", "SAVE"))
        self.changePassButton.setText(_translate("Dialog", "CHANGE PASSWORD"))
        self.changeAvButton.setText(_translate("Dialog", "CHANGE"))
        self.label.setText(_translate("Dialog", "MANAGE"))
        self.rb_7.setText(_translate("Dialog", "RadioButton"))
        self.rb_3.setText(_translate("Dialog", "RadioButton"))
        self.rb_2.setText(_translate("Dialog", "RadioButton"))
        self.rb_6.setText(_translate("Dialog", "RadioButton"))
        self.rb_1.setText(_translate("Dialog", "RadioButton"))
        self.rb_4.setText(_translate("Dialog", "RadioButton"))
        self.rb_5.setText(_translate("Dialog", "RadioButton"))
        self.rb_9.setText(_translate("Dialog", "RadioButton"))
        self.rb_8.setText(_translate("Dialog", "RadioButton"))
        self.rb_10.setText(_translate("Dialog", "RadioButton"))
        self.saveAvButton.setText(_translate("Dialog", "SAVE"))
        self.backToManButton1.setText(_translate("Dialog", "BACK"))
        self.label_2.setText(_translate("Dialog", "PASSWORD CHANGE"))
        self.label_3.setText(_translate("Dialog", "OLD PASSWORD"))
        self.label_4.setText(_translate("Dialog", "NEW PASSWORD 1"))
        self.label_5.setText(_translate("Dialog", "NEW PASSWORD 2"))
        self.savePassButton.setText(_translate("Dialog", "SAVE"))
        self.backToManButton2.setText(_translate("Dialog", "BACK"))

    def goToChangePassword(self):
        self.stackedWidget.setCurrentWidget(self.page_3)
        self.oldPass.setText("")
        self.newPass1.setText("")
        self.newPass2.setText("")
        self.errorLabel2.setText("")
        self.oldPass.setStyleSheet("border-color: grey")
        self.newPass1.setStyleSheet("border-color: grey")
        self.newPass2.setStyleSheet("border-color: grey")

    def goToMain(self):
        self.stackedWidget.setCurrentWidget(self.page_1)
        self.aboutText.setPlainText(str(blackjack.DataBase().getPlayer(self.user.username)["description"]))
        self.errorLabel.setText("")

    def saveAvButtonFunction(self):             # dziala
        rb = self.avatarGroup.checkedButton()
        db = blackjack.DataBase()
        db.updateAvatar(self.user.username, rb.name)
        self.user.avatar = rb.name
        pixmap = QPixmap('images/avatars/' + rb.name).scaled(251, 251)
        self.avatar.setPixmap(pixmap)
        pixmap = QPixmap('images/avatars/' + rb.name).scaled(61, 61)
        self.avatarUs.setPixmap(pixmap)
        print("Updated avatar")
        self.stackedWidget.setCurrentWidget(self.page_1)

    def savePassButtonFunction(self):           # dziala
        db = blackjack.DataBase()
        password = db.getPasswd(self.user.username)
        if password != self.oldPass.text():
            self.oldPass.setStyleSheet("border-color: red")
            self.errorLabel2.setText("ERROR")
            self.errorLabel2.setStyleSheet("color: red")
            oldPassCorrect = False
        else:
            self.oldPass.setStyleSheet("border-color: green")
            oldPassCorrect = True
        if re.match("^[a-z0-9A-Z]{5,16}$", self.newPass1.text()) is None:
            self.newPass1.setStyleSheet("border-color: red")
            self.errorLabel2.setText("ERROR")
            self.errorLabel2.setStyleSheet("color: red")
            newPass1Correct = False
        else:
            self.newPass1.setStyleSheet("border-color: green")
            newPass1Correct = True
        if re.match("^[a-z0-9A-Z]{5,16}$", self.newPass2.text()) is None:
            self.newPass2.setStyleSheet("border-color: red")
            self.errorLabel2.setText("ERROR")
            self.errorLabel2.setStyleSheet("color: red")
            newPass2Correct = False
        else:
            self.newPass2.setStyleSheet("border-color: green")
            newPass2Correct = True
        if self.newPass1.text() != self.newPass2.text():
            self.errorLabel2.setText("ERROR")
            self.errorLabel2.setStyleSheet("color: red")
            passMatch = False
        else:
            passMatch = True
        if oldPassCorrect and newPass1Correct and newPass2Correct and passMatch:
            db.updatePassword(self.user.username, self.newPass1.text())
            self.errorLabel2.setText("Password changed")
            self.errorLabel2.setStyleSheet("color: #b1f900")
            print("Password changed")

    def saveAboutButtonFunction(self):
        if re.match("^[a-z0-9A-Z ]{5,200}$", self.aboutText.toPlainText()) is None:
            self.errorLabel.setStyleSheet("color: red")
            self.errorLabel.setText("ERROR")
            pass
        else:
            db = blackjack.DataBase()
            db.updateDescription(self.user.username, self.aboutText.toPlainText())
            self.errorLabel.setStyleSheet("color: #b1f900")
            self.errorLabel.setText("UPDATED")
            print('Updated about')


class Avatar(QtWidgets.QRadioButton):
    def __init__(self, name, parent=None):
        super(Avatar, self).__init__(parent)
        self.name = name
        # self.setIcon('images/avatars/anubis.png')
        self.setStyleSheet("QRadioButton::indicator {"
                           "width: 160px;"
                           "height: 160px;"
                           "image: url(images/avatars/" + name + ")}"
                                                                 "QRadioButton::indicator::checked {"
                                                                 "width: 150px;"
                                                                 "height: 150px;"
                                                                 "border : 5px solid yellow;"
                                                                 "}")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())