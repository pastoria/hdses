# This Python file uses the following encoding: utf-8
import sys
import os


from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QMessageBox, QGridLayout
from PyQt5.QtCore import Qt, QFile, QCoreApplication, QTimer, QUrl, QThread, pyqtSignal
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPainter, QColor, QPixmap, QCursor, QDesktopServices


class SplashWidget(QWidget):
    def __init__(self):
        super(SplashWidget, self).__init__()
        loadUi('splash.ui', self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.center()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

if __name__ == "__main__":
    app = QApplication([])
    widget = SplashWidget()
    widget.show()
    sys.exit(app.exec_())
