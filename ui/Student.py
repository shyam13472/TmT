# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file
# 'ui/ui_template/student.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from ui.Menu import Ui_MainWindow
from ui.sql_api import Bd


class student_ui(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(832, 435)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_2.addWidget(self.spinBox)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
            )
        self.horizontalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_11.addItem(spacerItem4)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_11.addWidget(self.lineEdit_6)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        spacerItem5 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_4.addWidget(self.spinBox_2)
        spacerItem6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_4.addItem(spacerItem6)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_4)
        spacerItem7 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
            )
        self.horizontalLayout_12.addItem(spacerItem7)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_12.addWidget(self.label_10)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_12.addWidget(self.lineEdit_7)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        spacerItem8 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding
            )
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_5)
        spacerItem9 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding
            )
        self.horizontalLayout_13.addItem(spacerItem9)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_13.addWidget(self.label_11)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_13.addWidget(self.lineEdit_8)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        spacerItem10 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem10)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_6.addWidget(self.lineEdit_2)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_6)
        spacerItem11 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding
            )
        self.horizontalLayout_14.addItem(spacerItem11)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_14.addWidget(self.label_12)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_14.addWidget(self.lineEdit_9)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        spacerItem12 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem12)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_7.addWidget(self.lineEdit_3)
        spacerItem13 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding
            )
        self.horizontalLayout_7.addItem(spacerItem13)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_7)
        spacerItem14 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding
            )
        self.horizontalLayout_15.addItem(spacerItem14)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_15.addWidget(self.label_13)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_15.addWidget(self.lineEdit_10)
        self.verticalLayout.addLayout(self.horizontalLayout_15)
        spacerItem15 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_9.addWidget(self.lineEdit_4)
        spacerItem16 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding
            )
        self.horizontalLayout_9.addItem(spacerItem16)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_9)
        spacerItem17 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding
            )
        self.horizontalLayout_16.addItem(spacerItem17)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_16.addWidget(self.label_14)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_16.addWidget(self.lineEdit_11)
        self.verticalLayout.addLayout(self.horizontalLayout_16)
        spacerItem18 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem18)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_10.addWidget(self.lineEdit_5)
        spacerItem19 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding
            )
        self.horizontalLayout_10.addItem(spacerItem19)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_10.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_10.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 709, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)
        self.menu.addAction(self.action)
        self.menuBar.addAction(self.menu.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "профиль ученика"))
        self.label_2.setText(_translate("MainWindow", "id"))
        self.label_9.setText(_translate("MainWindow", "Класс"))
        self.label_3.setText(_translate("MainWindow", "ID Группы"))
        self.label_10.setText(_translate("MainWindow", "Email"))
        self.label_4.setText(_translate("MainWindow", "Фио"))
        self.label_11.setText(_translate("MainWindow", "комментарий"))
        self.label_5.setText(_translate("MainWindow", "Номер телефона"))
        self.label_12.setText(_translate("MainWindow", "vk_id"))
        self.label_6.setText(_translate("MainWindow", "СНИЛС"))
        self.label_13.setText(_translate("MainWindow", "Telegram_id"))
        self.label_7.setText(_translate("MainWindow", "Паспорт или свид-во"))
        self.label_14.setText(_translate("MainWindow", "discord_id"))
        self.label_8.setText(_translate("MainWindow", "Школа"))
        self.pushButton_2.setText(_translate("MainWindow", "назад"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.action_2.setText(
            _translate("MainWindow", "Создать новую учебную группу")
        )
        self.action_3.setText(
            _translate("MainWindow", "Создать преподавателя")
        )
        self.action.setText(_translate("MainWindow", "История"))
        self.action_4.setText(_translate("MainWindow", "Список всех групп "))


class Window_student(QtWidgets.QMainWindow, student_ui):
    def __init__(self, id=None, flag=None):
        super(Window_student, self).__init__()
        self.setupUi(self)
        self.bd = Bd()
        self.id = id
        self.flag = flag
        self.InitUI()
        self.pushButton.clicked.connect(self.save)

    def InitUI(self):
        if self.flag:
            try:
                data = self.bd.get_student_by_id(self.id)
                self.spinBox.setValue(int(data[0]))
                self.spinBox.setDisabled(True)
                self.spinBox_2.setValue(int(data[1]))
                self.lineEdit.setText(data[2])
                self.lineEdit_2.setText(data[3])
                self.lineEdit_3.setText(data[4])
                self.lineEdit_4.setText(data[5])
                self.lineEdit_5.setText(data[6])
                self.lineEdit_6.setText(data[7])
                self.lineEdit_7.setText(data[8])
                self.lineEdit_8.setText(data[9])
                self.lineEdit_9.setText(data[10])
                self.lineEdit_10.setText(data[11])
                self.lineEdit_11.setText(data[12])
            except BaseException:
                pass

    def save(self):
        groups = self.spinBox_2.value()
        name = self.lineEdit.text()
        Phone_number = self.lineEdit_2.text()
        Snils = self.lineEdit_3.text()
        Pers_data = self.lineEdit_4.text()
        School = self.lineEdit_5.text()
        Class = self.lineEdit_6.text()
        Email = self.lineEdit_7.text()
        Comment = self.lineEdit_8.text()
        vk_id = self.lineEdit_9.text()
        Telegram_id = self.lineEdit_10.text()
        discord_id = self.lineEdit_11.text()
        if self.flag:
            self.bd.update_student_info(
                groups,
                name,
                Phone_number,
                Snils,
                Pers_data,
                School,
                Class,
                Email,
                Comment,
                vk_id,
                Telegram_id,
                discord_id,
                id=self.id
            )
            QtWidgets.QMessageBox.about(
                self,
                "Успешно", "Данные человека изменены 1"
            )
        else:
            self.bd.add_student(
                groups,
                name,
                Phone_number,
                Snils,
                Pers_data,
                School,
                Class,
                Email,
                Comment,
                vk_id,
                Telegram_id,
                discord_id
            )


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Window_student(id=1, flag=True)
    ex.show()
    sys.exit(app.exec())
