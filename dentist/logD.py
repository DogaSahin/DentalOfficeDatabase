# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_logWin(object):
    def setupUi(self, logWin):
        logWin.setObjectName("logWin")
        logWin.resize(302, 182)
        logWin.setToolTip("")
        logWin.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(logWin)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 20, 111, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 91, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 71, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 50, 111, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.loginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loginBtn.setGeometry(QtCore.QRect(10, 90, 75, 23))
        self.loginBtn.setObjectName("loginBtn")
        self.createAc = QtWidgets.QPushButton(self.centralwidget)
        self.createAc.setGeometry(QtCore.QRect(100, 90, 111, 23))
        self.createAc.setObjectName("createAc")
        logWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(logWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 302, 21))
        self.menubar.setObjectName("menubar")
        logWin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(logWin)
        self.statusbar.setObjectName("statusbar")
        logWin.setStatusBar(self.statusbar)

        self.retranslateUi(logWin)
        QtCore.QMetaObject.connectSlotsByName(logWin)

    def retranslateUi(self, logWin):
        _translate = QtCore.QCoreApplication.translate
        logWin.setWindowTitle(_translate("logWin", "Login"))
        self.label.setText(_translate("logWin", "Email"))
        self.label_2.setText(_translate("logWin", "Password"))
        self.loginBtn.setText(_translate("logWin", "Login"))
        self.createAc.setText(_translate("logWin", "Create Account"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    logWin = QtWidgets.QMainWindow()
    ui = Ui_logWin()
    ui.setupUi(logWin)
    logWin.show()
    sys.exit(app.exec_())
