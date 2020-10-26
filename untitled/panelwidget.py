# This Python file uses the following encoding: utf-8
import sys
import os


from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QDesktopWidget, QMessageBox
from PyQt5.QtCore import Qt, QFile, QCoreApplication, QTimer, QUrl, QThread, pyqtSignal, QPoint
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPainter, QColor, QPixmap, QCursor, QDesktopServices, QBitmap, QPen
from utility import get_font_avenir

STATUS_READY = 0
STATUS_RUNNING = 1
STATUS_ERROR = 2
STATUS_FINISH = 3


qss_status_ready = """
#PanelWidget {
		background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #f7f7c1, stop:1 #ffff4c);
		border-radius: 5px;
}

QLineEdit {
	background: #ffffbd;
	border: 1px solid white;
}
"""

FLOAT_PANEL_RATIO = 1.5


class MainPanelWidget(QWidget):
    def __init__(self, number, main_widget):
        super(MainPanelWidget, self).__init__()
        loadUi('panelwidget.ui', self)
        self.set_font(get_font_avenir())
        self.number = number
        self.main_widget = main_widget
        self.label_number.setText('%02d' % number)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.float_panel = None

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

    def paintEvent(self, QPaintEvent):
        self.bmp = QBitmap(self.size())
        self.bmp.fill()
        painter = QPainter(self.bmp)
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.black)
        painter.drawRoundedRect(self.bmp.rect(), 5, 5)
        painter.setRenderHint(QPainter.Antialiasing)
        self.setMask(self.bmp)

    def enterEvent(self, event):
        if self.main_widget:
            self.main_widget.close_all_float_panels()

        if not self.float_panel:
            self.float_panel = FloatPanelWidget(self.number, self)
            self.float_panel.setParent(self.parent())
            self.float_panel.setWindowFlags(Qt.WindowStaysOnTopHint)

        if self.float_panel:
            f_w = self.width() * FLOAT_PANEL_RATIO
            f_h = self.height() * FLOAT_PANEL_RATIO
            f_x = max(0, self.x()-(f_w-self.width())/2)
            f_y = max(0, self.y()-(f_h-self.height())/2)

            self.float_panel.setGeometry(f_x, f_y, f_w, f_h)
            self.float_panel.show()

    def close_float_panel(self):
        if self.float_panel:
            self.float_panel.close()
            self.float_panel = None

    def change_style(self):
        self.setStyleSheet(qss_status_ready)


floatpanelstyle = """
    FloatPanelWidget {border:2px solid #35065a;}
    #widget_info {background-color: #f4c64f;}
    #widget_status {background-color: #ffffff;}
"""

class FloatPanelWidget(QFrame):
    def __init__(self, number, main_panel):
        super(FloatPanelWidget, self).__init__()
        loadUi('panelwidget.ui', self)
        self.set_font(get_font_avenir())
        self.number = number
        self.main_panel = main_panel
        self.label_number.setText('%02d' % number)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet(floatpanelstyle)

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

    # def paintEvent(self, QPaintEvent):
    #     self.bmp = QBitmap(self.size())
    #     self.bmp.fill()
    #     painter = QPainter(self.bmp)
    #     painter.setPen(Qt.NoPen)
    #     painter.setBrush(Qt.black)
    #     painter.drawRoundedRect(self.bmp.rect(), 5, 5)
    #     painter.setRenderHint(QPainter.Antialiasing)
    #     self.setMask(self.bmp)

    def leaveEvent(self, event):
        if self.main_panel:
            self.main_panel.close_float_panel()

    def change_style(self):
        self.setStyleSheet(qss_status_ready)


if __name__ == "__main__":
    app = QApplication([])
    widget = MainPanelWidget()
    widget.show()
    sys.exit(app.exec_())
