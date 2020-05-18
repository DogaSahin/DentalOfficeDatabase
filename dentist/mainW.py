from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore
from mainWD import Ui_MainWindow
from patientW import patientWin
from profileW import profile
import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Substring(1);",
    database = "dentistdb"
)

class mainWindow(QMainWindow):

    def loadData(self):
        con=connection
        myCursor=con.cursor()

        sql = "SELECT * FROM patient"
        myCursor.execute(sql)
        result=myCursor.fetchall()
        self.ui.tableWidget.setColumnCount(5)
        for row_n, coloumn in enumerate(result):
            self.ui.tableWidget.setRowCount(row_n+1)
            for coloumn_n, data in enumerate(coloumn):
                self.ui.tableWidget.setItem(row_n,coloumn_n,QtWidgets.QTableWidgetItem(str(data)))
        con.close()    
        
    def __init__(self,pid=0):
        super().__init__()
        
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.loadData()
        self.ui.openBtn.clicked.connect(lambda:self.bagla())
        self.ui.searchTxt.textChanged.connect(lambda : self.search())
        self.ui.profileBtn.clicked.connect(lambda:self.profileShow(pid))
        #self.ui.setupUi(self)

    def bagla(self):
        r=self.ui.tableWidget.currentRow()
        c=self.ui.tableWidget.currentColumn()
        self.patientWindow=patientWin()
        self.patientWindow.ui.label.setText(str(self.ui.tableWidget.item(r,0).text()))

        self.patientWindow.show()

    def search(self):
        tckn = self.ui.searchTxt.text()
        con = connection
        con._open_connection()
        myCursor=con.cursor()

        sql = "SELECT * FROM patient_history WHERE tckn LIKE %s"
        myCursor.execute(sql,[("%"+tckn+"%")])
        result = myCursor.fetchall()
        self.ui.tableWidget.setColumnCount(5)
        for row_n, coloumn in enumerate(result):
            self.ui.tableWidget.setRowCount(row_n+1)
            for coloumn_n, data in enumerate(coloumn):
                self.ui.tableWidget.setItem(row_n,coloumn_n,QtWidgets.QTableWidgetItem(str(data)))
        con.close()
    
    def profileShow(self,pid):
        self.pr=profile(pid)
        self.pr.show()
        


        
