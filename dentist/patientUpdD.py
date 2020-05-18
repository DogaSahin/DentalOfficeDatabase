# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'patientUpd.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(264, 180)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mobileTxt = QtWidgets.QLineEdit(self.centralwidget)
        self.mobileTxt.setGeometry(QtCore.QRect(130, 70, 113, 20))
        self.mobileTxt.setObjectName("mobileTxt")
        self.nameTxt = QtWidgets.QLineEdit(self.centralwidget)
        self.nameTxt.setGeometry(QtCore.QRect(130, 0, 113, 20))
        self.nameTxt.setObjectName("nameTxt")
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(10, 110, 231, 23))
        self.saveBtn.setObjectName("saveBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 70, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.surnameTxt_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.surnameTxt_2.setGeometry(QtCore.QRect(130, 30, 113, 20))
        self.surnameTxt_2.setObjectName("surnameTxt_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 264, 21))
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
        self.saveBtn.setText(_translate("MainWindow", "Update"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_6.setText(_translate("MainWindow", "Mobile"))
        self.label_2.setText(_translate("MainWindow", "Surname"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
