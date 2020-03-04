# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\users\jack\desktop\secondWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class SecondWindow(object):

    def collectInput(self):
        print("incomplete")

    def goBack(self):
        print("incomplete")
        #MainWindow.show()
        #SecondWindow.hide()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(534, 281)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Name entry
        self.TaskNameEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.TaskNameEntry.setGeometry(QtCore.QRect(100, 40, 113, 20))
        self.TaskNameEntry.setObjectName("TaskNameEntry")

        #date entry
        self.TaskDateEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.TaskDateEntry.setGeometry(QtCore.QRect(100, 90, 113, 20))
        self.TaskDateEntry.setObjectName("TaskDateEntry")

        #between
        self.betweenTime = QtWidgets.QLineEdit(self.centralwidget)
        self.betweenTime.setEnabled(False)
        self.betweenTime.setGeometry(QtCore.QRect(10, 150, 51, 20))
        self.betweenTime.setObjectName("betweenTime")

        #toTime
        self.toTime = QtWidgets.QLineEdit(self.centralwidget)
        self.toTime.setEnabled(False)
        self.toTime.setGeometry(QtCore.QRect(110, 150, 51, 20))
        self.toTime.setObjectName("toTime")

        #is timed checkbox
        self.Timed = QtWidgets.QCheckBox(self.centralwidget)
        self.Timed.setEnabled(True)
        self.Timed.setGeometry(QtCore.QRect(40, 120, 91, 17))
        self.Timed.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Timed.setObjectName("Timed")

        #labels
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 81, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 81, 20))
        self.label_2.setObjectName("label_2")

        #to menu
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(10, 210, 75, 23))
        self.back.setObjectName("back")
        
        #self.back.clicked.connect(self.goBack)

        #finish buttom
        self.finishEntry = QtWidgets.QPushButton(self.centralwidget)
        self.finishEntry.setGeometry(QtCore.QRect(10, 180, 75, 23))
        self.finishEntry.setObjectName("finishEntry")
        self.finishEntry.clicked.connect(self.collectInput)

        #task names box
        self.TaskNameView = QtWidgets.QListView(self.centralwidget)
        self.TaskNameView.setGeometry(QtCore.QRect(230, 30, 81, 192))
        self.TaskNameView.setObjectName("TaskNameView")

        #task name dates box
        self.TaskDateView = QtWidgets.QListView(self.centralwidget)
        self.TaskDateView.setGeometry(QtCore.QRect(330, 30, 191, 192))
        self.TaskDateView.setObjectName("TaskDateView")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 534, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Task 366 Reminders"))
        self.TaskDateEntry.setText(_translate("MainWindow", "YYYY/MM/DD"))
        self.Timed.setText(_translate("MainWindow", "Between time"))
        self.label.setText(_translate("MainWindow", "New task name :"))
        self.label_2.setText(_translate("MainWindow", "Task date :"))
        self.back.setText(_translate("MainWindow", "Back"))
        self.finishEntry.setText(_translate("MainWindow", "Finish entry"))


