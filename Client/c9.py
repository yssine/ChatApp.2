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
    ui = ch('Ding',12)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
