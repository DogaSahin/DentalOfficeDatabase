from PyQt5.QtWidgets import *
from asMainWD import Ui_asMainW
import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Substring(1);",
    database = "dentistdb"
)

class createPatient(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_asMainW()
        self.ui.setupUi(self)
        self.ui.saveBtn.clicked.connect(lambda:self.save())
        
    def save(self):
        s=str(self.ui.calendarWidget.selectedDate())
        s1=s[19:29]
        print(s1)

        user_name = self.ui.nameTxt.text()
        user_surname = self.ui.surnameTxt.text()
        mobile = self.ui.phoneTxt.text()
        tckn=self.ui.tcTxt.text()
        con=connection
        Mycursor=con.cursor()
  
        sql = "INSERT INTO patient (tckn,patientname,patientsurname,dob,phone) VALUES (%s,%s,%s,%s,%s)"
        value = (tckn,user_name,user_surname,s1,mobile)
        Mycursor.execute(sql,value)

        try:
            con.commit()
            print(f'{Mycursor.rowcount} Data Added')
        except mysql.connector.Error as err:
            print ("Error occured" , err)
        finally:
            con.close

