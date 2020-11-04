# This Python file uses the following encoding: utf-8
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QGraphicsDropShadowEffect, QDesktopWidget, QMessageBox
from PyQt5.QtCore import Qt, QFile, QCoreApplication, QTimer, QUrl, QThread, pyqtSignal, QPoint, QVariant
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPainter, QColor, QPixmap, QCursor, QDesktopServices, QBitmap, QPen
from utility import get_font_avenir, load_combobox_options
from basewidget import BaseWidget, BaseFrame
from style import mainpanelstyle, combobox_style_small

STATUS_READY = 0
STATUS_RUNNING = 1
STATUS_ERROR = 2
STATUS_FINISH = 3


class MainPanelWidget(BaseWidget):
    def __init__(self, number, main_widget):
        super(MainPanelWidget, self).__init__('panelwidget.ui', number, main_widget)
        font = get_font_avenir()
        font.setPixelSize(14)
        self.comboBox.setFont(font)
        options = load_combobox_options()
        for option in options:
            self.comboBox.addItem('   ' + option, QVariant(option))
        self.comboBox.setPlaceholderText("   Select a Profile")
        self.comboBox.setCurrentIndex(-1)
        self.comboBox.setMaximumWidth(150)
        self.comboBox.currentIndexChanged.connect(
            lambda: self.change_option(self.comboBox.currentIndex()))

        self.set_font(font)


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

    def create_frame(self, number, main_panel):
        return MainPanelFrame(number, main_panel)

    def set_current_option(self, index):
        self.comboBox.setCurrentIndex(index)

    def get_current_option(self):
        return self.comboBox.currentIndex()

    def change_option(self, index):
        if index > -1:
            self.comboBox.setStyleSheet(combobox_style_small)


class MainPanelFrame(BaseFrame):
    def __init__(self, number, main_panel):
        super(MainPanelFrame, self).__init__('panelwidget.ui', number, main_panel)
        self.setStyleSheet(mainpanelstyle)
        font = get_font_avenir()
        font.setPixelSize(18)
        self.comboBox.setFont(font)
        options = load_combobox_options()
        for option in options:
            self.comboBox.addItem('   ' + option, QVariant(option))
        self.comboBox.setPlaceholderText("   Select a Profile")
        self.comboBox.setMaximumWidth(500)
        self.comboBox.setMinimumHeight(26)
        self.comboBox.currentIndexChanged.connect(
            lambda: self.change_option(self.comboBox.currentIndex()))
        self.comboBox.setCurrentIndex(main_panel.get_current_option())
        self.change_option(main_panel.get_current_option())
        self.set_font(font)
        self.adjust_layout()

    def change_option(self, index):
        if index > -1:
            self.comboBox.setStyleSheet(combobox_style_small)
            self.main_panel.set_current_option(index)

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

    def leaveEvent(self, event):
        if not self.comboBox.view().isVisible():
            super().leaveEvent(event)


if __name__ == "__main__":
    app = QApplication([])
    widget = MainPanelWidget()
    widget.show()
    sys.exit(app.exec_())
