# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bot.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from ui.sql_api import Bd
import requests
import sys
import random


class Bot_ui(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(709, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "Текст сообщения:"))
        self.pushButton_2.setText(_translate("MainWindow", "назад"))
        self.pushButton_3.setText(_translate("MainWindow", "отправить"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.action_2.setText(_translate(
            "MainWindow",
            "Создать новую учебную группу")
        )
        self.action_3.setText(_translate(
            "MainWindow",
            "Создать преподавателя")
        )
        self.action.setText(_translate("MainWindow", "История"))
        self.action_4.setText(_translate("MainWindow", "Список всех групп "))


class Window_bot(QtWidgets.QMainWindow, Bot_ui):
    def __init__(self, group):
        super(Window_bot, self).__init__()
        self.setupUi(self)
        self.bd = Bd()
        self.pushButton_3.clicked.connect(self.send_msg)
        self.group = group

    def send_msg(self):
        text = self.textEdit.toPlainText()
        user = self.bd.get_net_id_group(self.group)
        n = len(user * 2)
        self.progressBar.setMaximum(n)
        self.progressBar.setValue(0)
        count = 0
        for i in user:
            # Telegram
            telegram_url = 'https://api.telegram.org/'
            t_tocken = 'bot5116492940:AAES0YfQVbVOcaxUdwNSR5ZmZ1YYGIhuptM/'
            t_metod = 'sendMessage'
            t = telegram_url + t_tocken + t_metod
            r = requests.get(t, data={
             "chat_id": str(i[1]),
             "text": {text}
              })
            count += 1
            self.progressBar.setValue(count)
            # VK
            vk_url = 'https://api.vk.com/method/messages.send?'
            vk_token = 'access_token=vk1.a.HI5Te9AEY9jUb3PPIHHbWpRSh6\
                W3UaJhcUvLDU_kkecWhuiEhG1n4DglOnRreAO3MfSscS64FNTtwmq\
                    oxF8iXISKB5LqHF8nr-1bahBY4k2K0Bft2xFV8Y_AAcbiO7SO\
                        WkkSupjxJAbOsxV7ZPAbKE9aiPdeZUGOZyURsyr-sqYtD\
                            5qWsJx0xd2cUlYg2wQUh5I9lpI6HnjL2uZO31W-Lg'
            r = requests.get(
                vk_url + vk_token +
                f'&message={text}&random_id={random.randrange(0, 100000000)}\
                    &user_id={str(i[0])}&v=5.131')
            count += 1
            self.progressBar.setValue(count)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Window_bot()
    ex.show()
    sys.exit(app.exec())
