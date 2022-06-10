from email import message
from select import select
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


class Ui_MainWindow(object):
    def __init__(self,user,pdp):
        self.user=User(user,pdp)
        # self.pdp=pdp
        self.data2p={"user":self.user.usn,"text":"","file":None,"image":None}
        self.lisn=True
        self.buff=[]
        self.Online=[]
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 50, 412, 328))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget_2 = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4.addWidget(self.widget_2)
        self.disco = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.disco.setMinimumSize(QtCore.QSize(64, 64))
        self.disco.setMaximumSize(QtCore.QSize(64, 64))
        self.disco.setStyleSheet("border-radius: 50%;")
        self.disco.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.disco.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/logout.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.disco.setIcon(icon)
        self.disco.setIconSize(QtCore.QSize(60, 60))
        self.disco.setObjectName("disco")
        self.horizontalLayout_4.addWidget(self.disco)
        self.widget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget.setMaximumSize(QtCore.QSize(5, 32))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4.addWidget(self.widget)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 174, 68))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setStyleSheet("background-color: #7f8c8d;")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scrollArea)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(200, 0))
        self.scrollArea_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 200, 68))
        self.scrollAreaWidgetContents_2.setMinimumSize(QtCore.QSize(200, 0))
        self.scrollAreaWidgetContents_2.setMaximumSize(QtCore.QSize(250, 16777215))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.addWidget(self.scrollArea_2)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.TxT = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.TxT.setMinimumSize(QtCore.QSize(200, 100))
        self.TxT.setMaximumSize(QtCore.QSize(16777215, 150))
        self.TxT.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        font = QtGui.QFont()
        font.setFamily("TeX Gyre Pagella Math")
        font.setPointSize(20)
        font.setBold(False)
        self.TxT.setFont(font)
        self.TxT.setObjectName("TxT")
        self.horizontalLayout_2.addWidget(self.TxT)
        self.imp = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.imp.setMinimumSize(QtCore.QSize(70, 70))
        self.imp.setMaximumSize(QtCore.QSize(70, 70))
        self.imp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.imp.setStyleSheet("border-radius: 50%;")
        self.imp.setText("")
        self.imp.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imgs/import.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.imp.setIcon(icon1)
        self.imp.setIconSize(QtCore.QSize(60, 60))
        self.imp.setObjectName("imp")
        self.horizontalLayout_2.addWidget(self.imp)
        self.snd = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.snd.setMinimumSize(QtCore.QSize(70, 70))
        self.snd.setMaximumSize(QtCore.QSize(70, 70))
        self.snd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.snd.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("imgs/snd.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.snd.setIcon(icon2)
        self.snd.setIconSize(QtCore.QSize(60, 60))
        self.snd.setObjectName("snd")
        self.snd.setStyleSheet("border-radius: 50%;")
        self.horizontalLayout_2.addWidget(self.snd)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.timer1=QtCore.QTimer()
        self.timer1.timeout.connect(self.upbuff)
        self.timer1.start()
        # self.timer2=QtCore.QTimer()
        # self.timer2.timeout.connect(self.ado)
        # self.timer2.start()
        self.rcvd = QtCore.pyqtSignal(str,str)
        # self.ado()
        self.snd.clicked.connect(self.offugo)
        self.disco.clicked.connect(self.logout)
        self.imp.clicked.connect(self.openfile)
        # self.rcvd.connect(self.admine)
        self.scrollArea.verticalScrollBar().rangeChanged.connect(lambda: self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum()))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", f"ChatApp: ({self.user.usn})"))
        MainWindow.setWindowIcon(QtGui.QIcon("imgs/Logo.png"))
        self.establish()
        
        self.thread = threading.Thread(target=self.receive)
        self.thread.daemon=True
        self.thread.start()




    def onl(self,usn,pdp,O):
        self.online = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.online.setMinimumSize(QtCore.QSize(0, 50))
        # self.online.setMaximumSize(QtCore.QSize(0, 60))
        self.online.setStyleSheet("background-color: green;")
        self.online.setObjectName("online")
        self.verticalLayout_7.addWidget(self.online)
        self.obj=Ui_Online(usn,pdp,O)
        self.obj.setupUi(self.online)

    def ado(self):
        # print(self.Online)
        for i in self.Online:
            l=i.split(':')
            # print(i[1])
            self.onl(l[0],f'imgs/Avatars/Avatar{l[1]}.png',True)
        # for i in range(10):
        #     self.onl(str(i),f'imgs/Avatars/Avatar{random.randint(0,12)}.png',True)

    def openfile(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(MainWindow, 'Open file')[0]
        f=open(fname,'rb')
        if fname.split('.')[-1] in ['jpg','jpeg ','jfif','pjpeg','pjp','png','svg','ico','webp']:
            self.data2p['image']=f.read()
            self.shmypic(fname,self.user.pdp)
        else:
            self.data2p['file']=f.read()
        self.send(self.data2p)





    def establish(self):
        self.SERVER, done1 = QtWidgets.QInputDialog.getText(None, 'Input Dialog', 'Servers IP address:')
        self.HEADER = 128
        self.FORMAT = 'utf-8'
        self.PORT = 6969
        self.DISCONNECT = "!CACTUS IS LOVE!"
        # self.SERVER = SERVER
        self.ADDR=(self.SERVER, self.PORT)
        self.client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)
        # self.temp, done2 = QtWidgets.QInputDialog.getText(None, 'Input Dialog', 'Input your username:')
        # self.user.usn=self.temp
        self.hello=Message(usr=self.user,typ='Hello')
        self.send(self.hello)

    def send(self,msg):
        message = pickle.dumps(msg)
        msg_l = str(len(message)).encode(self.FORMAT)
        msg_l += b' ' * (self.HEADER - len(msg_l))
        self.client.send(msg_l)
        self.client.send(message)
        # self.data2p={"user":self.user.usn,"text":"","file":None,"image":None}



    def offugo(self):
        mytxt=self.TxT.toPlainText()
        if mytxt or False:
            self.TxT.setPlainText('')
            self.message=Message(self.user,mytxt,'text')
            # self.data2p['text']=mytxt
            self.admine(mytxt,self.user.pdp)
            self.send(self.message)

    def logout(self):
        # self.send(self.DISCONNECT)
        self.message=Message(usr=self.user,typ='disconnect')
        self.send(self.message)
        self.lisn=False
        try:
            self.thread.stop()
        except Exception as e:
            pass
        try:
            MainWindow.close()
        except:
            import sys
            sys.exit()

    def receive(self):
        while self.lisn:
            msg_l=self.client.recv(self.HEADER)
            if msg_l:
                msg_l = int(msg_l)
                message = pickle.loads(self.client.recv(msg_l))
                if message.usr.usn!=self.user.usn and message.typ=='text':
                    self.buff.append((message))
                if message.typ=='Onl':
                    # print(message.msg.split('|')[1:])
                    self.Online=message.msg.split('|')[1:]
                    # self.ado()

    def upbuff(self):
        # print('.')
        if self.buff:
            message=self.buff.pop(0)
            self.adtheir(message.msg,message.usr.pdp)



    def admine(self,msg,pdp):
        self.mine = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.mine.setEnabled(True)
        self.mine.setMouseTracking(True)
        self.mine.setObjectName("mine")
        self.verticalLayout_6.addWidget(self.mine)
        # self.horizontalLayout = QtWidgets.QHBoxLayout(self.mine)
        # self.widget = QtWidgets.QWidget(self.mine)
        # self.horizontalLayout.addWidget(self.widget)
        self.obj=Ui_Mine(msg,pdp)
        self.obj.setupUi(self.mine)
        # self.scrollbot()

    def adtheir(self,msg,pdp):
        self.theirs = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.theirs.setEnabled(True)
        self.theirs.setMouseTracking(True)
        self.theirs.setObjectName("theirs")
        self.verticalLayout_6.addWidget(self.theirs)
        # self.theirs.setStyleSheet("background-color: blue;")
        # self.theirs = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        # self.theirs.setEnabled(True)
        # self.theirs.setMouseTracking(True)
        # self.theirs.setObjectName("mine")
        # self.verticalLayout_6.addWidget(self.theirs)
        # self.horizontalLayout = QtWidgets.QHBoxLayout(self.mine)
        # self.widget = QtWidgets.QWidget(self.mine)
        # self.horizontalLayout.addWidget(self.widget)
        self.obj=Ui_Their(msg,self.user.usn,pdp)
        self.obj.setupUi(self.theirs)
        # self.scrollbot()

    def shmypic(self,img,pdp):
        self.mine = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.mine.setEnabled(True)
        self.mine.setMouseTracking(True)
        self.mine.setObjectName("mine")
        self.verticalLayout_6.addWidget(self.mine)
        # self.horizontalLayout = QtWidgets.QHBoxLayout(self.mine)
        # self.widget = QtWidgets.QWidget(self.mine)
        # self.horizontalLayout.addWidget(self.widget)
        self.obj=Ui_Mepic(img,pdp)
        self.obj.setupUi(self.mine)
        # self.scrollbot()

    def scrollbot(self):
        x=self.scrollArea.verticalScrollBar().maximum()
        y=self.scrollArea.verticalScrollBar().value()
        # self.scrollArea.verticalScrollBar().setSliderPosition(x)
        print(x,y)
        if x==y:
            pass
        # else :
        #     self.timer1.stop()



    def maj(self):
        x=self.scrollArea.verticalScrollBar().maximum()
        self.scrollbot()
        


        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow('',random.randint(0,12))
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
