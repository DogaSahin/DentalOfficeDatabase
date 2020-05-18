from PyQt5.QtWidgets import *
from createAWD import Ui_MainWindow
import mysql.connector
from mysql.connector import errorcode

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Substring(1);",
    database = "dentistdb"
)

class createAccount(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.statusBox.addItem("Y")
        self.ui.statusBox.addItem("N")
        self.ui.saveBtn.clicked.connect(lambda:self.saveF())

    def saveF(self):
        user_name = self.ui.nameTxt.text()
        user_surname = self.ui.surnameTxt_2.text()
        email = self.ui.emailTxt.text()
        password = self.ui.passwordTxt.text()
        mobile = self.ui.mobileTxt.text()
        is_active = self.ui.statusBox.currentText()
        role = self.ui.roleTxt.text()
        
        con=connection
        Mycursor=con.cursor()

        sql = "INSERT INTO user_account (user_name,user_surname,email,password,mobile,is_active,role) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        value = (user_name,user_surname,email,password,mobile,is_active,role)
        Mycursor.execute(sql,value)

        try:
            con.commit()
            print(f'{Mycursor.rowcount} Data Added')
        except mysql.connector.Error as err:
            print ("Error occured" , err)
        finally:
            con.close


