# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'patient.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_patientW(object):
    def setupUi(self, patientW):
        patientW.setObjectName("patientW")
        patientW.resize(513, 491)
        self.centralwidget = QtWidgets.QWidget(patientW)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 50, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 90, 191, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(260, 90, 221, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 70, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 150, 461, 251))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 410, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.deleteBtn = QtWidgets.QPushButton(self.centralwidget)
        self.deleteBtn.setGeometry(QtCore.QRect(330, 410, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.deleteBtn.setFont(font)
        self.deleteBtn.setObjectName("deleteBtn")
        patientW.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(patientW)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 513, 21))
        self.menubar.setObjectName("menubar")
        patientW.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(patientW)
        self.statusbar.setObjectName("statusbar")
        patientW.setStatusBar(self.statusbar)

        self.retranslateUi(patientW)
        QtCore.QMetaObject.connectSlotsByName(patientW)

    def retranslateUi(self, patientW):
        _translate = QtCore.QCoreApplication.translate
        patientW.setWindowTitle(_translate("patientW", "Patient Info"))
        self.pushButton.setText(_translate("patientW", "Save"))
        self.label.setText(_translate("patientW", "Name"))
        self.label_2.setText(_translate("patientW", "Dissease"))
        self.label_3.setText(_translate("patientW", "Medicine"))
        self.pushButton_2.setText(_translate("patientW", "Update"))
        self.deleteBtn.setText(_translate("patientW", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    patientW = QtWidgets.QMainWindow()
    ui = Ui_patientW()
    ui.setupUi(patientW)
    patientW.show()
    sys.exit(app.exec_())
