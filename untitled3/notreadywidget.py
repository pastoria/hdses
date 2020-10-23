# This Python file uses the following encoding: utf-8
import sys
import os


from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QMessageBox
from PyQt5.QtCore import Qt, QFile, QCoreApplication, QTimer, QUrl, QThread, pyqtSignal, QPoint
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPainter, QColor, QPixmap, QCursor, QDesktopServices


class NotReadyWidget(QWidget):
    def __init__(self):
        super(NotReadyWidget, self).__init__()
        loadUi('NotReadyWidget.ui', self)


if __name__ == "__main__":
    app = QApplication([])
    widget = NotReadyWidget()
    widget.show()
    sys.exit(app.exec_())
