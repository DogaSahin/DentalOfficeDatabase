from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore
from patientUpdD import Ui_MainWindow
import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Substring(1);",
    database = "dentistdb"
)

class profile(QMainWindow):
    
    def __init__(self,profileID):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.saveBtn.clicked.connect(lambda:self.update(profileID))
        print(profileID)   



    def update(self,tckn):
       con = connection
       myCursor=con.cursor()
       name=self.ui.nameTxt.text()
       phn=self.ui.mobileTxt.text()
       sname=self.ui.surnameTxt_2.text()

       sql= "UPDATE patient SET patientname = %s,patientsurname = %s,phone = %s  WHERE tckn=%s"
       myCursor.execute(sql,[name,sname,phn,str(tckn)])
       con.commit()
       