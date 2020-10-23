# This Python file uses the following encoding: utf-8
import sys
import os


from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QMessageBox
from PyQt5.QtCore import Qt, QFile, QCoreApplication, QTimer, QUrl, QThread, pyqtSignal, QPoint
from PyQt5.uic import loadUi
from PyQt5.QtGui import QBitmap, QPainter, QColor, QPixmap, QCursor, QDesktopServices, QPaintEvent
from utility import get_font_avenir


class NotReadyWidget(QWidget):
    def __init__(self, number):
        super(NotReadyWidget, self).__init__()
        loadUi('notreadywidget.ui', self)
        self.set_font(get_font_avenir())
        self.number = number
        self.label_number.setText(str(number))

    def set_font(self, font):
        self.label_number.setFont(font)
        self.label_title.setFont(font)
        self.label_desc.setFont(font)

    def paintEvent(self, QPaintEvent):
        self.bmp = QBitmap(self.size())
        self.bmp.fill()
        painter = QPainter(self.bmp)
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.black)
        painter.drawRoundedRect(self.bmp.rect(), 5, 5)
        painter.setRenderHint(QPainter.Antialiasing)
        self.setMask(self.bmp)


if __name__ == "__main__":
    app = QApplication([])
    widget = NotReadyWidget()
    widget.show()
    sys.exit(app.exec_())
