# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profile.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(249, 270)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 120, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.emailTxt = QtWidgets.QLineEdit(self.centralwidget)
        self.emailTxt.setGeometry(QtCore.QRect(130, 60, 113, 20))
        self.emailTxt.setObjectName("emailTxt")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.nameTxt = QtWidgets.QLineEdit(self.centralwidget)
        self.nameTxt.setGeometry(QtCore.QRect(130, 0, 113, 20))
        self.nameTxt.setObjectName("nameTxt")
        self.surnameTxt_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.surnameTxt_2.setGeometry(QtCore.QRect(130, 30, 113, 20))
        self.surnameTxt_2.setObjectName("surnameTxt_2")
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(10, 190, 231, 23))
        self.saveBtn.setObjectName("saveBtn")
        self.passwordTxt = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordTxt.setGeometry(QtCore.QRect(130, 90, 113, 20))
        self.passwordTxt.setObjectName("passwordTxt")
        self.mobileTxt = QtWidgets.QLineEdit(self.centralwidget)
        self.mobileTxt.setGeometry(QtCore.QRect(130, 120, 113, 20))
        self.mobileTxt.setObjectName("mobileTxt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 249, 21))
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
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_6.setText(_translate("MainWindow", "Mobile"))
        self.label_2.setText(_translate("MainWindow", "Surname"))
        self.label_5.setText(_translate("MainWindow", "Password"))
        self.label_3.setText(_translate("MainWindow", "E-Mail"))
        self.saveBtn.setText(_translate("MainWindow", "Update"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
