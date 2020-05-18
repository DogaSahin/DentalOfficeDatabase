# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asMain.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_asMainW(object):
    def setupUi(self, asMainW):
        asMainW.setObjectName("asMainW")
        asMainW.resize(459, 405)
        self.centralwidget = QtWidgets.QWidget(asMainW)
        self.centralwidget.setObjectName("centralwidget")
        self.nameTxt = QtWidgets.QLineEdit(self.centralwidget)
        self.nameTxt.setGeometry(QtCore.QRect(130, 10, 113, 20))
        self.nameTxt.setObjectName("nameTxt")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.surnameTxt = QtWidgets.QLineEdit(self.centralwidget)
        self.surnameTxt.setGeometry(QtCore.QRect(130, 40, 113, 20))
        self.surnameTxt.setObjectName("surnameTxt")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tcTxt = QtWidgets.QLineEdit(self.centralwidget)
        self.tcTxt.setGeometry(QtCore.QRect(130, 70, 113, 20))
        self.tcTxt.setObjectName("tcTxt")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.phoneTxt = QtWidgets.QLineEdit(self.centralwidget)
        self.phoneTxt.setGeometry(QtCore.QRect(130, 100, 113, 20))
        self.phoneTxt.setObjectName("phoneTxt")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 170, 312, 183))
        self.calendarWidget.setObjectName("calendarWidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 150, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(330, 10, 101, 71))
        self.saveBtn.setObjectName("saveBtn")
        asMainW.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(asMainW)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 459, 21))
        self.menubar.setObjectName("menubar")
        asMainW.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(asMainW)
        self.statusbar.setObjectName("statusbar")
        asMainW.setStatusBar(self.statusbar)

        self.retranslateUi(asMainW)
        QtCore.QMetaObject.connectSlotsByName(asMainW)

    def retranslateUi(self, asMainW):
        _translate = QtCore.QCoreApplication.translate
        asMainW.setWindowTitle(_translate("asMainW", "Secretary"))
        self.label.setText(_translate("asMainW", "Name"))
        self.label_2.setText(_translate("asMainW", "Surname"))
        self.label_3.setText(_translate("asMainW", "TCKN"))
        self.label_4.setText(_translate("asMainW", "Phone"))
        self.label_5.setText(_translate("asMainW", "Birth date"))
        self.saveBtn.setText(_translate("asMainW", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    asMainW = QtWidgets.QMainWindow()
    ui = Ui_asMainW()
    ui.setupUi(asMainW)
    asMainW.show()
    sys.exit(app.exec_())
