from PyQt5.QtWidgets import *
from logD import Ui_logWin
from mainW import mainWindow
from createAW import createAccount
from asMainW import createPatient
import mysql.connector
import time

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Substring(1);",
    database = "dentistdb"
)

class logWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_logWin()
        self.ui.setupUi(self)
        self.kayitpecere=createAccount()
        self.ui.loginBtn.clicked.connect(lambda:self.login())
        self.ui.createAc.clicked.connect(lambda:self.create())
        
    def login(self):
        con = connection
        cursor=con.cursor()

        email = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        find_user = ("SELECT * FROM user_account WHERE email = %s AND password = %s") 
        cursor.execute(find_user,[(email),(password)])
        results = cursor.fetchall()
        con.close()
        print(results[0][0])
        if results:
            if results[0][7] == "dentist":
                self.anapencere= mainWindow(int(results[0][0]))
                self.anapencere.show()
            elif results[0][7] == "secretary":
                self.sec=createPatient()
                self.sec.show()

            else:
                print ("Invalid Email or Password")
                time.sleep(2)
        
    def create(self):
        self.kayitpecere.show()    
    
