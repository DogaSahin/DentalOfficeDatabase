from PyQt5.QtWidgets import QApplication
from mainW import mainWindow
from createAW import createAccount
from log import logWin

app=QApplication([])
logW=logWin()
logW.show()

app.exec_()