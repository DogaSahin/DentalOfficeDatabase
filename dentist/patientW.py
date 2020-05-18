from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore
from patientD import Ui_patientW
from patientUpdW import profile
import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Substring(1);",
    database = "dentistdb"
)

class patientWin(QMainWindow):

    def __init__(self):
       super().__init__()
       self.ui=Ui_patientW()
       self.ui.setupUi(self)
       self.con = connection
       self.myCursor=self.con.cursor()
       self.sql= "SELECT * FROM treatment WHERE patient_tckn=%s"
       self.myCursor.execute(self.sql,[self.ui.label.text()])
       
       self.result=self.myCursor.fetchall()
       #hasta geçmişi gösteren tabloyu dolduruyoruz
       for row_n, coloumn in enumerate(self.result):
            self.ui.tableWidget.setRowCount(row_n+1)
            for coloumn_n, data in enumerate(coloumn):
                self.ui.tableWidget.setItem(row_n,coloumn_n,QtWidgets.QTableWidgetItem(str(data)))
        #hastalıklar vew tadavilerden aldıklarımızı dolduruyoruz
       self.sql= "SELECT * FROM problem_catalog"
       self.myCursor.execute(self.sql)
       self.pid=[]
       self.result1=self.myCursor.fetchall()
       for dis in (self.result1):
            self.ui.comboBox.addItem(str(dis[1]))
            self.pid.append(dis[0])
       
       self.sql= "SELECT * FROM medication_catalog"
       self.myCursor.execute(self.sql)
       self.mid=[]
       self.result2=self.myCursor.fetchall()
       for med in (self.result2):
            self.ui.comboBox_2.addItem(str(med[1]))
            self.mid.append(med[0])

       self.ui.pushButton.clicked.connect(lambda:self.save())
       self.ui.pushButton_2.clicked.connect(lambda:self.update())
       self.ui.deleteBtn.clicked.connect(lambda:self.delete())
       self.con.close()


    def save(self):
        self.con = connection
        self.con._open_connection()
        self.myCursor=self.con.cursor()
        print([self.ui.label.text(),self.mid[self.ui.comboBox.currentIndex()],self.pid[self.ui.comboBox_2.currentIndex()]])
        #buraya SQl kayıt okları gelecek hastalık dis tedavi med değişkeninde
        sql="INSERT INTO treatment (patient_tckn,problem_id,medication_id) VALUES (%s,%s,%s)"
        self.myCursor.execute(sql,[self.ui.label.text(),self.mid[self.ui.comboBox.currentIndex()],self.pid[self.ui.comboBox_2.currentIndex()]])
        self.con.commit()
        self.con.close()

    def update(self):
        prolileWin=profile(self.ui.label.text())
        prolileWin.show()

    def delete(self):
        self.con = connection
        self.con._open_connection()
        self.myCursor=self.con.cursor()
        sql="DELETE FROM patient WHERE tckn=%s"
        self.myCursor.execute(sql,[self.ui.label.text()])
        self.con.commit()
        self.con.close()
        self.ui.label.setText("hasta silindi")

       