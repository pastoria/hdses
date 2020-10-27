# This Python file uses the following encoding: utf-8
import sys
import os
import random
import resource_rc

from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QMessageBox, QGridLayout
from PyQt5.QtCore import Qt, QFile, QCoreApplication, QTimer, QUrl, QThread, pyqtSignal
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPainter, QColor, QPixmap, QCursor, QDesktopServices
from basewidget import BaseWidget
from panelwidget import MainPanelWidget
from notreadywidget import NotReadyWidget

MAX_ROW = 6
MAX_COL = 8


class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        loadUi('mainwidget.ui', self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.pushButton_close.setStyleSheet("border:none;")
        self.pushButton_close.clicked.connect(QCoreApplication.instance().quit)
        self.gridLayout = QGridLayout(self.widget_middle)

        for i in range(MAX_ROW*MAX_COL):
            row = i // MAX_COL
            col = i % MAX_COL
            if random.randint(0, 99) % 2 == 0:
                widget = NotReadyWidget(i+1, self)
            else:
                widget = MainPanelWidget(i+1, self)
            self.gridLayout.addWidget(widget, row, col)

        self.showMaximized()

    def close_all_float_panels(self):
        for i in range(self.gridLayout.count()):
            widget = self.gridLayout.itemAt(i).widget()
            if isinstance(widget, BaseWidget):
                widget.close_float_panel()

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


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWidget()
    widget.show()
    sys.exit(app.exec_())
