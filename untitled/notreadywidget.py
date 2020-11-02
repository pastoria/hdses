# This Python file uses the following encoding: utf-8
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QGraphicsDropShadowEffect, QDesktopWidget, QMessageBox
from PyQt5.QtCore import Qt, QFile, QCoreApplication, QTimer, QUrl, QThread, pyqtSignal, QPoint
from PyQt5.uic import loadUi
from PyQt5.QtGui import QBitmap, QPainter, QColor, QPixmap, QCursor, QDesktopServices, QPaintEvent
from utility import get_font_avenir
from basewidget import BaseWidget, BaseFrame


notreadystyle = """
    NotReadyFrame {
        border: 2px solid #35065a;
    }   
    QLabel {
        Color: #ffffff;
    }
    #widget_up {
        background: #909090;
    }    
    #widget_down {
        background: #ffffff;
    }
"""


class NotReadyWidget(BaseWidget):
    def __init__(self, number, main_widget):
        super(NotReadyWidget, self).__init__('notreadywidget.ui', number, main_widget)
        self.set_font(get_font_avenir())

    def set_font(self, font):
        font.setPixelSize(24)
        self.label_number.setFont(font)
        self.label_title.setFont(font)
        font.setPixelSize(14)
        self.label_desc.setFont(font)

    def create_frame(self, number, main_panel):
        return NotReadyFrame(number, main_panel)


class NotReadyFrame(BaseFrame):
    def __init__(self, number, main_panel):
        super(NotReadyFrame, self).__init__('notreadywidget.ui', number, main_panel)
        self.setStyleSheet(notreadystyle)
        self.set_font(get_font_avenir())

    def set_font(self, font):
        font.setPixelSize(40)
        self.label_number.setFont(font)
        self.label_title.setFont(font)
        font.setPixelSize(24)
        self.label_desc.setFont(font)


if __name__ == "__main__":
    app = QApplication([])
    widget = NotReadyWidget()
    widget.show()
    sys.exit(app.exec_())
