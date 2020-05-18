from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore
from profileD import Ui_MainWindow
import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Substring(1);",
    database = "dentistdb"
)

class profile(QMainWindow):
    
    def __init__(self,profileID=0):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.saveBtn.clicked.connect(lambda:self.update(profileID))
        print(profileID)   



    def update(self,pid):
        user_name = self.ui.nameTxt.text()
        user_surname = self.ui.surnameTxt_2.text()
        email = self.ui.emailTxt.text()
        password = self.ui.passwordTxt.text()
        mobile = self.ui.mobileTxt.text()  
          
        con=connection
        Mycursor=con.cursor()

        sql = "UPDATE user_account SET user_name = %s, user_surname = %s, email = %s, password = %s, mobile = %s WHERE id = %s"
        value = [user_name,user_surname,email,password,mobile,pid]
        Mycursor.execute(sql,value)

        try:
            con.commit()
            print(f'{Mycursor.rowcount} Data Updated')
        except mysql.connector.Error as err:
            print ("Error occured" , err)
        finally:
            con.close
        
