# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ui.sql_api import Bd


class Admin_ui(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(577, 375)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout_3.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setEnabled(True)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 577, 26))
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
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_4)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.action_2.setText(_translate("MainWindow", "Создать новую учебную группу"))
        self.action_3.setText(_translate("MainWindow", "Создать преподавателя"))
        self.action.setText(_translate("MainWindow", "История"))
        self.action_4.setText(_translate("MainWindow", "Список всех групп "))


class Window_admin(QtWidgets.QMainWindow, Admin_ui):
    def __init__(self):
        super(Window_admin, self).__init__()
        self.setupUi(self)
        self.bd = Bd()
        self.init_ui()

    def init_ui(self):
        res = self.bd.get_all_group()
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['name','num','teacher', 'button'])
        # Заполняем таблицу элементами
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                if elem == row[2]:
                    elem = self.bd.get_teacher_by_id(row[2])
                self.tableWidget.setItem(
                    i, j, QtWidgets.QTableWidgetItem(str(elem)))
            self.tableWidget.setCellWidget(
                    i, 3, QtWidgets.QPushButton('Перейти', self))
            




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Window_admin()
    ex.show()
    sys.exit(app.exec())