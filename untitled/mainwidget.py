# This Python file uses the following encoding: utf-8
import sys
import os
import random
import resource_rc

from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QMessageBox, QGridLayout
from PyQt5.QtCore import Qt, QFile, QCoreApplication, QVariant, QTimer, QUrl, QThread, pyqtSignal
from PyQt5.uic import loadUi
from basewidget import BaseWidget
from utility import get_font_avenir, load_combobox_options
from panelwidget import MainPanelWidget
from notreadywidget import NotReadyWidget
from style import combobox_style_big

MAX_PANEL = 48


# get row and column value by total number of panels
# max_panel: 16 32 48
def get_max_row_col(max_panel):
    if max_panel == 16:
        max_row = 4
        max_col = 4
    elif max_panel == 32:
        max_row = 4
        max_col = 8
    else:
        max_row = 6
        max_col = 8
    return max_row, max_col


class MainWidget(QWidget):
    def __init__(self, max_panel):
        super(MainWidget, self).__init__()
        loadUi('mainwidget.ui', self)
        self.m_flag = False
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.pushButton_close.setStyleSheet("border:none;")
        self.pushButton_close.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton_allstart.clicked.connect(self.start_all)
        self.pushButton_allcancel.clicked.connect(self.cancel_all)
        font = get_font_avenir()
        self.pushButton_allstart.setFont(font)
        self.pushButton_allcancel.setFont(font)
        self.checkBox.setFont(font)
        self.comboBox.setFont(font)
        options = load_combobox_options()
        for option in options:
            self.comboBox.addItem('   ' + option, QVariant(option))
        self.comboBox.setPlaceholderText("   Select a Profile")
        self.comboBox.view().setSpacing(2)
        self.comboBox.setCurrentIndex(-1)
        self.comboBox.currentIndexChanged.connect(
            lambda: self.change_option(self.comboBox.currentIndex()))

        self.gridLayout = QGridLayout(self.widget_middle)

        max_row, max_col = get_max_row_col(max_panel)
        for i in range(max_row*max_col):
            row = i // max_col
            col = i % max_col
            if random.randint(0, 99) % 2 == 0:
                widget = NotReadyWidget(i+1, self)
            else:
                widget = MainPanelWidget(i+1, self)
            # widget = MainPanelWidget(i + 1, self)
            self.gridLayout.addWidget(widget, row, col)

        self.showMaximized()

    def start_all(self):
        for i in range(self.gridLayout.count()):
            widget = self.gridLayout.itemAt(i).widget()
            if isinstance(widget, MainPanelWidget):
                widget.start()
        pass

    def cancel_all(self):
        for i in range(self.gridLayout.count()):
            widget = self.gridLayout.itemAt(i).widget()
            if isinstance(widget, MainPanelWidget):
                widget.cancel()
        pass

    def change_option(self, index):
        if index > -1:
            self.comboBox.setStyleSheet(combobox_style_big)

        for i in range(self.gridLayout.count()):
            widget = self.gridLayout.itemAt(i).widget()
            if isinstance(widget, MainPanelWidget):
                widget.set_current_option(index)

    def close_all_float_panels(self):
        for i in range(self.gridLayout.count()):
            widget = self.gridLayout.itemAt(i).widget()
            if isinstance(widget, BaseWidget):
                widget.close_float_panel()

    # def mousePressEvent(self, event):
    #     if event.button() == Qt.LeftButton:
    #         self.m_flag = True
    #         self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
    #         event.accept()
    #
    # def mouseMoveEvent(self, QMouseEvent):
    #     if Qt.LeftButton and self.m_flag:
    #         self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
    #         QMouseEvent.accept()
    #
    # def mouseReleaseEvent(self, QMouseEvent):
    #     self.m_flag = False
    #     self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == "__main__":
    app = QApplication([])
    if len(sys.argv) > 1:
        max_panel = int(sys.argv[1])
    else:
        max_panel = MAX_PANEL
    widget = MainWidget(max_panel)
    widget.show()
    sys.exit(app.exec_())
