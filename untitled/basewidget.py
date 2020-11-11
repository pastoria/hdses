# This Python file uses the following encoding: utf-8

from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QGraphicsDropShadowEffect, QDesktopWidget, QMessageBox
from PyQt5.QtCore import Qt, QFile, QCoreApplication, QTimer, QUrl, QThread, pyqtSignal, QPoint
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPainter, QColor, QPixmap, QCursor, QDesktopServices, QBitmap, QPen, QBrush

FLOAT_PANEL_RATIO = 1.5


class BaseWidget(QWidget):
    def __init__(self, ui_file, number, main_widget):
        super(BaseWidget, self).__init__()
        loadUi(ui_file, self)
        self.number = number
        self.main_widget = main_widget
        self.label_number.setText('%2d' % number)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.float_panel = None

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
            self.float_panel = self.create_frame(self.number, self)
            self.float_panel.setParent(self.parent())
            self.float_panel.setWindowFlags(Qt.WindowStaysOnTopHint)

        if self.float_panel:
            f_w = self.width() * FLOAT_PANEL_RATIO
            f_h = self.height() * FLOAT_PANEL_RATIO
            f_x = max(0, self.x() - (f_w - self.width()) / 2)
            f_y = max(0, self.y() - (f_h - self.height()) / 2)

            f_x = min(self.parent().width() - f_w, f_x)
            f_y = min(self.parent().height() - f_h, f_y)

            self.float_panel.setGeometry(f_x, f_y, f_w, f_h)
            self.float_panel.show()

    def close_float_panel(self):
        if self.float_panel:
            self.float_panel.close()
            self.float_panel = None


class BaseFrame(QFrame):
    def __init__(self, ui_file, number, main_panel):
        super(BaseFrame, self).__init__()
        loadUi(ui_file, self)
        self.number = number
        self.main_panel = main_panel
        self.label_number.setText('%2d' % number)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)
        # self.add_shadow_effect()

    def paintEvent(self, QPaintEvent):
        self.bmp = QBitmap(self.size())
        self.bmp.fill()
        painter = QPainter(self.bmp)
        painter.setPen(QColor(53, 6, 90))
        painter.setBrush(QBrush(QColor(53, 6, 90)))
        painter.drawRoundedRect(self.bmp.rect(), 5, 5)
        painter.setRenderHint(QPainter.Antialiasing)
        self.setMask(self.bmp)

    def leaveEvent(self, event):
        if self.main_panel:
            self.main_panel.close_float_panel()

    def add_shadow_effect(self):
        self.shadow_effect = QGraphicsDropShadowEffect(self)
        self.shadow_effect.setOffset(1, 1)
        self.shadow_effect.setBlurRadius(5)
        self.shadow_effect.setColor(QColor(53, 6, 90))
        self.setGraphicsEffect(self.shadow_effect)
