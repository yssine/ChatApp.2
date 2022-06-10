from PyQt5 import QtCore, QtGui, QtWidgets
from dep.online import Ui_Online
from dep.mine import Ui_Mine
from dep.memg import Ui_Mepic
from dep.their import Ui_Their
import threading
import random
import socket
import pickle
from dep.cls import User, Message
from chatt import Ui_MainWindow as ch





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    d = QtWidgets.QInputDialog()
    d.setWindowIcon(QtGui.QIcon('imgs/Logo.png'))
    temp, done2 = d.getText(None, 'Input Dialog', 'Input a unique username:')
    if not done2:
        sys.exit(app.exec_())
    if not temp:
        sys.exit(app.exec_())
    ui = ch(temp,random.randint(0,12))
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
