from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QCoreApplication, Qt, QSize, QRegExp, QThread, pyqtSignal
from PyQt5.QtGui import QRegExpValidator, QPainter, QColor, QPixmap, QCursor

from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLineEdit, QMessageBox
from PyQt5.uic import loadUi
import os
import sys
import resource_rc
import subprocess
import json
import redis

class LoginThread(QThread):
    done = pyqtSignal(int)

    def __init__(self, username, password):
        super(LoginThread, self).__init__()
        self.username=username
        self.password=password

    def run(self):
        import time
        ret = 1
        fn = os.path.join(os.environ['ATHENAHOME'], 'anthenacmc')
        if os.path.exists(fn):
            p = subprocess.Popen([fn, '-login', '-username={}'.format(self.username), '-password={}'.format(self.password)], cwd=os.environ['ATHENAHOME'])
            ret = p.wait()
        else:
            ret = 2
        self.done.emit(ret)
        pass


class LoginWidget(QWidget):
    LoginCompleted = pyqtSignal(int)

    def __init__(self):
        super(LoginWidget, self).__init__()
        self.r = redis.Redis()
        self.errorcode = -1
        self.initUi()
        self.setWindowFlags(Qt.FramelessWindowHint)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            # self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def closeEvent(self, event):
        self.r.close()

    def showEvent(self, event):
        pass

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def initUi(self):
        loadUi('login.ui', self)
        self.center()
        self.fullscreen = False
        x = self.r.get('ui.fullscreen')
        if bool(x) and x=='True':
            self.fullscreen = True
        self.pushButton_close.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton_mini.clicked.connect(self.showMinimized)

        # Chris: load version
        fn = os.path.join(os.getenv('ATHENAHOME', os.path.split(__file__)[0]), 'clientstatus.json')
        if os.path.exists(fn):
            with open(fn) as f:
                d = json.load(f)
                try:
                    v = d['sync']['status']['framework']['version']
                    self.label_version.setText(v)
                except:
                    pass

        fontId = QtGui.QFontDatabase.addApplicationFont("./fonts/AvenirLTStd-Medium.otf")
        fontInfoList = QtGui.QFontDatabase.applicationFontFamilies(fontId)
        fontFamily = fontInfoList[0]
        font = QtGui.QFont()
        font.setFamily(fontFamily)

        font.setPixelSize(18)
        self.label_version.setFont(font)

        font.setPixelSize(22)

        self.userLineEdit.setFont(font)

        re = QRegExp('[a-zA-Z0-9_]+')
        re_validato = QRegExpValidator(re, self)
        self.userLineEdit.setValidator(re_validato)
        self.userLineEdit.setStyleSheet("background-color:transparent;\n"
                                   "border:1px solid rgb(180, 180, 180);\n"
                                   "border-radius: 5px;\n"
                                   "border-width:0;border-style:outset;\n"
                                   "color: rgba(253, 253, 253, 0.49);")
        self.userLineEdit.setPlaceholderText("User Name")
        self.userLineEdit.textChanged['QString'].connect(self.changefontcolor)

        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.passwordLineEdit.setFont(font)

        # self.passwordLineEdit.setValidator(re_validato)
        self.passwordLineEdit.setStyleSheet("background-color: transparent;\n"
                                   "border:1px solid rgb(180, 180, 180);\n"
                                   "border-radius: 5px;\n"
                                   "border-width:0;border-style:outset;\n"\
                                   "color: rgba(253, 253, 253, 0.49);")
        self.passwordLineEdit.setPlaceholderText("Password")
        self.passwordLineEdit.textChanged['QString'].connect(self.changefontcolor)


        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                            "background-color: #8f00ff;\n"
                                  "border-radius: 20px;\n"
                                  "border:none;")

        self.loginButton.clicked.connect(self.checkUserPassword)

        self.errLabel.setFont(font)
        self.errLabel.setStyleSheet("color: rgba(236, 121, 127, 1); background-color: transparent;")

        # if remember
        x = self.r.hgetall('cmc.identity')
        if b'username' in x:
            self.reCheckbox.setChecked(True)
            self.userLineEdit.setText(x[b'username'].decode('utf-8'))
            if b'password' in x:
                self.passwordLineEdit.setText(x[b'password'].decode('utf-8'))

    def changefontcolor(self):
        sender = self.sender()
        # print(sender.text())
        text = sender.text()
        if (len(text) > 0):
            sender.setStyleSheet("background-color: transparent;\n"
                                   "border:1px solid rgb(180, 180, 180);\n"
                                   "border-radius: 5px;\n"
                                   "border-width:0;border-style:outset;\n"
                                   "color: rgb(255, 255, 255);")
        else:
            sender.setStyleSheet("background-color: transparent;\n"
                                   "border:1px solid rgb(180, 180, 180);\n"
                                   "border-radius: 5px;\n"
                                   "border-width:0;border-style:outset;\n"
                                   "color: rgba(253, 253, 253, 0.49);")

    def checkUserPassword(self):
        self.errLabel.setText('')
        self.userLineEdit.setEnabled(False)
        self.passwordLineEdit.setEnabled(False)
        self.loginButton.setEnabled(False)
        self.repaint()

        QApplication.setOverrideCursor(Qt.WaitCursor)
        username = self.userLineEdit.text()
        password = self.passwordLineEdit.text()
        t = LoginThread(username,password)
        t.done.connect(self.login_complete)
        t.run()


    def login_complete(self, errorcode):        
        QApplication.restoreOverrideCursor()
        self.errorcode = errorcode
        if errorcode ==0:
            # self.Ui_main = AmainWindow()
            # self.Ui_main.show()
            # remember
            if self.reCheckbox.isChecked():
                # r = redis.Redis()
                # r.set('cmc.username', self.userLineEdit.text())
                # r.set('cmc.password', self.passwordLineEdit.text())
                # r.close()
                self.r.hset('cmc.identity', 'username', self.userLineEdit.text())
                self.r.hset('cmc.identity', 'password', self.passwordLineEdit.text())
                pass
            else:
                # r = redis.Redis()
                # r.delete('cmc.username')
                # r.delete('cmc.password')
                # r.close()
                self.r.delete('cmc.identity')
                pass
            self.LoginCompleted.emit(0)
            self.close()
        else:
            msg = 'Fail to login. Error={}'.format(errorcode)
            # QMessageBox.information(self, 'Error', msg)
            self.errLabel.setText(msg)
        self.userLineEdit.setEnabled(True)
        self.passwordLineEdit.setEnabled(True)
        self.loginButton.setEnabled(True)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        pixmap = QPixmap(":/images/Login_BG.png")
        qp.drawPixmap(self.rect(), pixmap)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = LoginWidget()
    main.show()
    app.exec_()
    sys.exit(main.errorcode)


