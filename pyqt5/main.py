# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\users\jack\desktop\concept.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import source_rc

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from secondWindow import SecondWindow

class First(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(245, 375)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(12)

        self.label.setFont(font)
        self.label.setObjectName("label")

        #create reminder button
        self.createRem = QtWidgets.QPushButton(self.centralwidget)
        self.createRem.setGeometry(QtCore.QRect(60, 200, 121, 23))
        self.createRem.setObjectName("createRem")

        #run reminder main app
        self.runRem = QtWidgets.QPushButton(self.centralwidget)
        self.runRem.setGeometry(QtCore.QRect(60, 230, 121, 23))
        self.runRem.setObjectName("runRem")

        #delete from json
        self.deleteRem = QtWidgets.QPushButton(self.centralwidget)
        self.deleteRem.setGeometry(QtCore.QRect(60, 260, 121, 23))
        self.deleteRem.setObjectName("deleteRem")

        #exit app
        self.exitRem = QtWidgets.QPushButton(self.centralwidget)
        self.exitRem.setGeometry(QtCore.QRect(90, 300, 61, 23))
        self.exitRem.setObjectName("exitRem")

        #labels
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 60, 131, 131))
        self.label_2.setStyleSheet("image: url(:/newPrefix/titleScreen.jpg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 10, 101, 31))

        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 245, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.createRem.clicked.connect(self.openWindow)
        self.exitRem.clicked.connect(self.windowExit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Task 366"))
        self.label.setText(_translate("MainWindow", "What would you like to do?"))
        self.createRem.setText(_translate("MainWindow", "create reminder"))
        self.runRem.setText(_translate("MainWindow", "run reminders"))
        self.deleteRem.setText(_translate("MainWindow", "delete reminders"))
        self.exitRem.setText(_translate("MainWindow", "exit"))
        self.label_3.setText(_translate("MainWindow", "Task 366"))

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.hide()

    def windowExit(self):
        sys.exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = First()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
