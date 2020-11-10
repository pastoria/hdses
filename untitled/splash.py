# This Python file uses the following encoding: utf-8
import sys
import os


from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QMessageBox, QGridLayout
from PyQt5.QtCore import Qt, QFile, QCoreApplication, QTimer, QUrl, QThread, pyqtSignal
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPainter, QColor, QPixmap, QCursor, QDesktopServices
from utility import get_font_avenir
from login import LoginWidget


class SplashWidget(QWidget):
    def __init__(self):
        super(SplashWidget, self).__init__()
        loadUi('splash.ui', self)
        self.set_font(get_font_avenir())
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.center()
        self.timer = QTimer()
        self.timer.timeout.connect(self.time)
        self.timer.start(1*1000)
        self.counter = 0

    def time(self):
        msg = [
            'Preparing environment...',
            'Loading third party library...',
            'Ready to go...'
        ]

        if self.counter < len(msg):
            self.label_msg.setText(msg[self.counter])
            self.counter = self.counter + 1
        else:
            self.timer.stop()
            login_widget.show()
            self.close()

    def set_font(self, font):
        font.setPixelSize(18)
        self.label_version.setFont(font)
        self.label_msg.setFont(font)
        font.setPixelSize(14)
        self.label_copyright.setFont(font)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) // 2,
                  (screen.height() - size.height()) // 2)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        pixmap = QPixmap(":/images/Splash_BG_big.png")
        qp.drawPixmap(self.rect(), pixmap)
        qp.end()


if __name__ == "__main__":
    app = QApplication([])
    widget = SplashWidget()
    login_widget = LoginWidget()
    widget.show()
    sys.exit(app.exec_())
