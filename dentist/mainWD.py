# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainW.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(539, 427)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 60, 491, 201))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.openBtn = QtWidgets.QPushButton(self.centralwidget)
        self.openBtn.setGeometry(QtCore.QRect(20, 290, 75, 23))
        self.openBtn.setObjectName("openBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.searchTxt = QtWidgets.QLineEdit(self.centralwidget)
        self.searchTxt.setGeometry(QtCore.QRect(90, 30, 113, 20))
        self.searchTxt.setObjectName("searchTxt")
        self.profileBtn = QtWidgets.QPushButton(self.centralwidget)
        self.profileBtn.setGeometry(QtCore.QRect(410, 0, 75, 23))
        self.profileBtn.setObjectName("profileBtn")
        self.welcomeLbl = QtWidgets.QLabel(self.centralwidget)
        self.welcomeLbl.setGeometry(QtCore.QRect(30, 370, 231, 16))
        self.welcomeLbl.setObjectName("welcomeLbl")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 539, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openBtn.setText(_translate("MainWindow", "Open"))
        self.label.setText(_translate("MainWindow", "Search"))
        self.profileBtn.setText(_translate("MainWindow", "Profile"))
        self.welcomeLbl.setText(_translate("MainWindow", "Welcome"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
