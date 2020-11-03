# This Python file uses the following encoding: utf-8
import sys
import os
import random
import resource_rc

from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QMessageBox, QGridLayout
from PyQt5.QtCore import Qt, QFile, QCoreApplication, QVariant, QTimer, QUrl, QThread, pyqtSignal
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPainter, QColor, QPixmap, QCursor, QDesktopServices
from basewidget import BaseWidget
from utility import get_font_avenir
from panelwidget import MainPanelWidget
from notreadywidget import NotReadyWidget

MAX_PANEL = 35


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


combobox_style_one = """
     QComboBox{  background-color: rgba(255, 255, 255, 1);
                 border: 1px solid rgba(143, 0, 255, 1);
                 border-radius: 3px;
                 border-width: 1px; border-style:outset;
                 padding-left: 5px;
                 font-size: 18px;
                 outline:0px;
                 combobox-popup: 0;
                 color: rgba(144, 144, 144, 1);
    }

 QComboBox QAbstractItemView {
    outline: 0px solid red;
    border: 0px solid yellow;
    color: rgba(0, 0, 0, 1);
    padding-left: 0px;
    background-color: rgba(255, 255, 255, 1);
    selection-color: rgba(0, 0, 0, 1);
    selection-background-color: rgba(144, 144, 144, 1);
}

QComboBox::drop-down {
subcontrol-origin: padding;
subcontrol-position: top right;
width: 65px;
border-left-width: 0px;
border-left-color: gray;
border-left-style: solid;
border-top-right-radius: 3px;
border-bottom-right-radius: 3px;
background:transparent;
}

QComboBox::down-arrow {
	image: url(:/images/MoreButton_Purple.svg);
	background: transparent;
}

QComboBox QScrollBar::vertical{
    width:10px;
    background: rgba(255, 255, 255, 1);
    border:none;
    border-radius:1px;
}

QComboBox QScrollBar::handle::vertical{
    border-radius:1px;
    width: 10px;
    background: rgba(204, 204, 204, 1);
}

QComboBox QScrollBar::add-line::vertical{
    border:none;
}
QComboBox QScrollBar::sub-line::vertical{
    border:none;
}
"""

combobox_style_two = """
     QComboBox{  background-color: rgba(255, 255, 255, 1);
                 border: 1px solid rgba(143, 0, 255, 1);
                 border-radius: 3px;
                 border-width: 1px; border-style:outset;
                 padding-left: 5px;
                 font-size: 18px;
                 outline:0px;
                 combobox-popup: 0;
                 color: rgba(0, 0, 0, 1);
    }

 QComboBox QAbstractItemView {
    outline: 0px solid red;
    border: 0px solid yellow;
    color: rgba(0, 0, 0, 1);
    padding-left: 0px;
    background-color: rgba(255, 255, 255, 1);
    selection-color: rgba(0, 0, 0, 1);
    selection-background-color: rgba(144, 144, 144, 1);
}

QComboBox::drop-down {
subcontrol-origin: padding;
subcontrol-position: top right;
width: 65px;
border-left-width: 0px;
border-left-color: gray;
border-left-style: solid;
border-top-right-radius: 3px;
border-bottom-right-radius: 3px;
background:transparent;
}

QComboBox::down-arrow {
	image: url(:/images/MoreButton_Purple.svg);
	background: transparent;
}

QComboBox QScrollBar::vertical{
    width:10px;
    background: rgba(255, 255, 255, 1);
    border:none;
    border-radius:1px;
}

QComboBox QScrollBar::handle::vertical{
    border-radius:1px;
    width: 10px;
    background: rgba(204, 204, 204, 1);
}

QComboBox QScrollBar::add-line::vertical{
    border:none;
}
QComboBox QScrollBar::sub-line::vertical{
    border:none;
}
"""

class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        loadUi('mainwidget.ui', self)
        self.m_flag = False
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.pushButton_close.setStyleSheet("border:none;")
        self.pushButton_close.clicked.connect(QCoreApplication.instance().quit)
        font = get_font_avenir()
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(combobox_style_one)
        options = ['Cisco Secure Erase Standard', 'DoD(3)', 'DoD7(7)', 'DoE(3)', 'NSA(3)',
                                'USAirForce(3)', 'USArmy(3)', 'USNavy(3)', 'CAN_RCMP(7)', 'CAN_CSEC(3)',
                                'Russian(2)', 'British(1)', 'UK(3)', 'German(7)', 'Australia(1)',
                                'Australia_15(3)', 'NewZealand(1)', 'BSchneier(7)', 'PGutmann(35)',
                                'Pfitzner(33)', 'OneTime_0(1)', 'OneTime_1(1)']
        for option in options:
            self.comboBox.addItem('   ' + option, QVariant(option))
        self.comboBox.setPlaceholderText("   Select a Profile")
        self.comboBox.setCurrentIndex(-1)
        self.comboBox.currentIndexChanged.connect(
            lambda: self.change_option(self.comboBox.currentIndex()))

        self.gridLayout = QGridLayout(self.widget_middle)

        max_row, max_col = get_max_row_col(MAX_PANEL)
        for i in range(max_row*max_col):
            row = i // max_col
            col = i % max_col
            # if random.randint(0, 99) % 2 == 0:
            #     widget = NotReadyWidget(i+1, self)
            # else:
            #     widget = MainPanelWidget(i+1, self)
            widget = MainPanelWidget(i + 1, self)
            self.gridLayout.addWidget(widget, row, col)

        self.showMaximized()

    def change_option(self, index):
        if index > -1:
            self.comboBox.setStyleSheet(combobox_style_two)
        else:
            self.comboBox.setStyleSheet(combobox_style_one)

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
