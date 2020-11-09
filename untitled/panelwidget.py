# This Python file uses the following encoding: utf-8
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QGraphicsDropShadowEffect, QDesktopWidget, QMessageBox
from PyQt5.QtCore import Qt, QFile, QCoreApplication, QTimer, QUrl, QThread, pyqtSignal, QPoint, QVariant, QSize
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPainter, QColor, QPixmap, QCursor, QDesktopServices, QBitmap, QPen, QIcon
from utility import get_font_avenir, load_combobox_options
from basewidget import BaseWidget, BaseFrame
from style import mainpanelstyle, combobox_style_small, combobox_style_ready, combobox_style_running, combobox_style_bad_sectors, \
    combobox_style_error, combobox_style_success, \
    status_style_ready, status_style_running, status_style_bad_sectors, status_style_error, status_style_success

STATUS_READY = 0
STATUS_RUNNING = 1
STATUS_BAD_SECTORS = 2
STATUS_ERROR = 3
STATUS_SUCCESS = 4


class MainPanelWidget(BaseWidget):
    def __init__(self, number, main_widget):
        super(MainPanelWidget, self).__init__('panelwidget.ui', number, main_widget)
        font = get_font_avenir()
        font.setPixelSize(12)
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

        self.info = {
            'sn': 'Z1P4HZ0S',
            'model': 'ST2000NM0011',
            'size': '2.00TB',
            'bad_sectors': 5,
            'start_time': '01:48',
            'end_time': '05:02',
            'speed': '110 MB / S',
            'progress': 45,
            'error': 33
        }

        import random
        self.status = random.randint(0, 4)
        # r = random.choice([1, 1])
        self.change_status()
        self.update_info()

    def set_progress(self, value):
        self.label_progress.setText(str(value)+'%')
        self.progressBar.setValue(value)

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
        pass
        # if index > -1:
        #     self.comboBox.setStyleSheet('color:(144, 144, 144)')
        #     # self.comboBox.setStyleSheet(combobox_style_small)

    def start(self):
        if self.status == STATUS_READY:
            self.status = STATUS_RUNNING
            self.change_status()

    def cancel(self):
        if self.status == STATUS_RUNNING or self.status == STATUS_BAD_SECTORS:
            self.status = STATUS_ERROR
            self.change_status()

    def change_status(self):
        status_dict = {
            STATUS_READY: self.change_status_ready,
            STATUS_RUNNING: self.change_status_running,
            STATUS_BAD_SECTORS: self.change_status_bad_sectors,
            STATUS_ERROR: self.change_status_error,
            STATUS_SUCCESS: self.change_status_success
        }

        func = status_dict.get(self.status, None)
        if func:
            func()

    def update_info(self):
        self.label_sn.setText(self.info.get('sn', ''))
        self.label_model.setText(self.info.get('model', ''))
        self.label_size.setText(self.info.get('size', ''))
        self.label_badsectors.setText('BadSectors ({0})'.format(self.info.get('bad_sectors', 0)))
        self.label_status_l.setText(self.info.get('start_time', ''))
        if self.status == STATUS_ERROR:
            self.label_status_r.setText('Error code: {0}'.format(self.info.get('error')))
        else:
            self.label_status_r.setText(self.info.get('speed'))

        if self.status == STATUS_SUCCESS:
            self.set_progress(100)
        else:
            self.set_progress(self.info.get('progress'))

    def change_status_ready(self):
        style = combobox_style_ready+combobox_style_small+status_style_ready
        self.setStyleSheet(style)
        self.label_icon_r.setPixmap(QPixmap(':/images/Speed.svg'))
        self.pushButton.setIcon(QIcon(':/images/StartTask_Gray.svg'))
        self.label_progress.hide()
        self.progressBar.hide()

    def change_status_running(self):
        style = combobox_style_running+combobox_style_small+status_style_running
        self.setStyleSheet(style)
        self.label_icon_r.setPixmap(QPixmap(':/images/Speed.svg'))
        self.pushButton.setIcon(QIcon(':/images/StopTask_White.svg'))
        self.label_progress.show()
        self.progressBar.show()

    def change_status_bad_sectors(self):
        style = combobox_style_bad_sectors+combobox_style_small+status_style_bad_sectors
        self.setStyleSheet(style)
        self.label_icon_r.setPixmap(QPixmap(':/images/Speed.svg'))
        self.pushButton.setIcon(QIcon(':/images/StopTask_White.svg'))
        self.label_progress.show()
        self.progressBar.show()

    def change_status_error(self):
        style = combobox_style_error+combobox_style_small+status_style_error
        self.setStyleSheet(style)
        self.label_icon_r.setPixmap(QPixmap(':/images/Error.svg'))
        self.label_status_r.setText('Error code: {0}'.format(self.info.get('error')))
        self.pushButton.setIcon(QIcon(''))
        self.label_progress.show()
        self.progressBar.show()

    def change_status_success(self):
        style = combobox_style_success+combobox_style_small+status_style_success
        self.setStyleSheet(style)
        self.label_icon_r.setPixmap(QPixmap(':/images/Speed.svg'))
        self.pushButton.setIcon(QIcon(''))
        self.label_progress.hide()
        self.progressBar.show()


class MainPanelFrame(BaseFrame):
    def __init__(self, number, main_panel):
        super(MainPanelFrame, self).__init__('panelwidget.ui', number, main_panel)
        self.setStyleSheet(mainpanelstyle)
        self.pushButton.setIconSize(QSize(22, 22))
        self.pushButton.clicked.connect(self.start_cancel)
        # self.label_icon_l.setSize(QSize(20, 20))
        # self.label_icon_r.setPixmapSize(QSize(20, 20))
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
        self.update_info(main_panel.info, main_panel.status)
        self.set_font(font)
        self.adjust_layout()

        self.change_status(self.main_panel.status)

    def start_cancel(self):
        if self.main_panel.status == STATUS_SUCCESS or self.main_panel.status == STATUS_ERROR:
            return

        if self.main_panel.status == STATUS_READY:
            self.main_panel.status = STATUS_RUNNING
            self.main_panel.change_status()
            self.change_status(STATUS_RUNNING)
        else:
            self.main_panel.status = STATUS_ERROR
            self.main_panel.change_status()
            self.change_status(STATUS_ERROR)


    def change_option(self, index):
        if index > -1:
            # self.comboBox.setStyleSheet(combobox_style_small)
            self.main_panel.set_current_option(index)

    def update_info(self, info, status):
        self.label_sn.setText(info.get('sn', ''))
        self.label_model.setText(info.get('model', ''))
        self.label_size.setText(info.get('size', ''))
        self.label_badsectors.setText('BadSectors ({0})'.format(info.get('bad_sectors', 0)))
        self.label_status_l.setText(info.get('start_time', ''))
        if status == STATUS_ERROR:
            self.label_status_r.setText('Error code: {0}'.format(info.get('error')))
        else:
            self.label_status_r.setText(info.get('speed'))

        if status == STATUS_SUCCESS:
            self.set_progress(100)
        else:
            self.set_progress(info.get('progress'))

    def change_status(self, status):
        status_dict = {
            STATUS_READY: self.change_status_ready,
            STATUS_RUNNING: self.change_status_running,
            STATUS_BAD_SECTORS: self.change_status_bad_sectors,
            STATUS_ERROR: self.change_status_error,
            STATUS_SUCCESS: self.change_status_success
        }

        func = status_dict.get(status, None)
        if func:
            func()

    def change_status_ready(self):
        style = combobox_style_ready+combobox_style_small+status_style_ready
        self.setStyleSheet(style)
        self.label_icon_r.setPixmap(QPixmap(':/images/Speed.svg'))
        self.pushButton.setIcon(QIcon(':/images/StartTask_Gray.svg'))
        self.label_progress.hide()
        self.progressBar.hide()

    def change_status_running(self):
        style = combobox_style_running+combobox_style_small+status_style_running
        self.setStyleSheet(style)
        self.label_icon_r.setPixmap(QPixmap(':/images/Speed.svg'))
        self.pushButton.setIcon(QIcon(':/images/StopTask_White.svg'))
        self.label_progress.show()
        self.progressBar.show()

    def change_status_bad_sectors(self):
        style = combobox_style_bad_sectors+combobox_style_small+status_style_bad_sectors
        self.setStyleSheet(style)
        self.label_icon_r.setPixmap(QPixmap(':/images/Speed.svg'))
        self.pushButton.setIcon(QIcon(':/images/StopTask_White.svg'))
        self.label_progress.show()
        self.progressBar.show()

    def change_status_error(self):
        style = combobox_style_error+combobox_style_small+status_style_error
        self.setStyleSheet(style)
        self.label_icon_r.setPixmap(QPixmap(':/images/Error.svg'))
        self.pushButton.setIcon(QIcon(''))
        self.label_progress.show()
        self.progressBar.show()

    def change_status_success(self):
        style = combobox_style_success+combobox_style_small+status_style_success
        self.setStyleSheet(style)
        self.label_icon_r.setPixmap(QPixmap(':/images/Speed.svg'))
        self.pushButton.setIcon(QIcon(''))
        self.label_progress.hide()
        self.progressBar.show()

    def set_progress(self, value):
        self.label_progress.setText(str(value)+'%')
        self.progressBar.setValue(value)

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
