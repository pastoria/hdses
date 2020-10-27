# This Python file uses the following encoding: utf-8
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QGraphicsDropShadowEffect, QDesktopWidget, QMessageBox
from PyQt5.QtCore import Qt, QFile, QCoreApplication, QTimer, QUrl, QThread, pyqtSignal, QPoint
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPainter, QColor, QPixmap, QCursor, QDesktopServices, QBitmap, QPen
from utility import get_font_avenir
from basewidget import BaseWidget, BaseFrame

STATUS_READY = 0
STATUS_RUNNING = 1
STATUS_ERROR = 2
STATUS_FINISH = 3


mainpanelstyle = """
    MainPanelFrame {
        border: 2px solid #35065a;
    }
    #widget_info {background-color: #f4c64f;}
    #widget_status {background-color: #ffffff;}
    #label_1, #label_2, #label_3 {
        color: #809379;
    }

    #label_progress {
        color: #2c56e8;
    }

    QProgressBar {
        background-color: rgba(255, 255, 255, 0);
        border: none;
    }

    QProgressBar::chunk {
        background-color: #2c56e8;
        border-radius: 3px;
    }
"""


class MainPanelWidget(BaseWidget):
    def __init__(self, number, main_widget):
        super(MainPanelWidget, self).__init__('panelwidget.ui', number, main_widget, MainPanelFrameFactory())
        self.set_font(get_font_avenir())

    def set_font(self, font):
        font.setPixelSize(20)
        self.label_number.setFont(font)
        font.setPixelSize(12)
        self.label_sn.setFont(font)
        self.label_model.setFont(font)
        self.label_size.setFont(font)
        self.label_badsectors.setFont(font)
        self.label_status_l.setFont(font)
        self.label_status_r.setFont(font)
        self.label_progress.setFont(font)
        self.label_1.setFont(font)
        self.label_2.setFont(font)
        self.label_3.setFont(font)


class MainPanelFrameFactory:
    def create_frame(self, number, main_panel):
        return MainPanelFrame(number, main_panel)


class MainPanelFrame(BaseFrame):
    def __init__(self, number, main_panel):
        super(MainPanelFrame, self).__init__('panelwidget.ui', number, main_panel)
        self.setStyleSheet(mainpanelstyle)
        self.set_font(get_font_avenir())
        self.adjust_layout()

    def set_font(self, font):
        font.setPixelSize(38)
        self.label_number.setFont(font)
        font.setPixelSize(20)
        self.label_sn.setFont(font)
        self.label_model.setFont(font)
        self.label_size.setFont(font)
        self.label_badsectors.setFont(font)
        self.label_status_l.setFont(font)
        self.label_status_r.setFont(font)
        self.label_progress.setFont(font)
        self.label_1.setFont(font)
        self.label_2.setFont(font)
        self.label_3.setFont(font)

    def adjust_layout(self):
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_3.setSpacing(10)


if __name__ == "__main__":
    app = QApplication([])
    widget = MainPanelWidget()
    widget.show()
    sys.exit(app.exec_())
