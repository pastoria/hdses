# This Python file uses the following encoding: utf-8
import sys
import os


from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QMessageBox
from PyQt5.QtCore import Qt, QFile, QCoreApplication, QTimer, QUrl, QThread, pyqtSignal, QPoint
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPainter, QColor, QPixmap, QCursor, QDesktopServices, QBitmap
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

class PanelWidget(QWidget):
    def __init__(self, number, is_float=False):
        super(PanelWidget, self).__init__()
        loadUi('panelwidget.ui', self)
        self.set_font(get_font_avenir())
        self.number = number
        self.label_number.setText('%02d' % number)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.is_float = is_float
        self.float_panel = None

        if not self.is_float:
            self.float_panel = PanelWidget(self.number, True)

    def set_font(self, font):
        self.label_number.setFont(font)
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
        if self.float_panel:
            print('{}:{} {}'.format(self.number, self.x(), self.y()))
            gpos = self.mapToGlobal(QPoint(0, 0))
            print('{}:{} {}'.format(self.number, gpos.x(), gpos.y()))
            # self.float_panel.setGeometry(gpos.x(), gpos.y(), self.width() * 1.2, self.height() * 1.2)
            self.float_panel.move(gpos.x(), gpos.y())
            # self.float_panel.move(1684, 108)
            # self.float_panel.show()

    def leaveEvent(self, event):
        if self.float_panel:
            self.float_panel.hide()

    def change_style(self):
        self.setStyleSheet(qss_status_ready)


if __name__ == "__main__":
    app = QApplication([])
    widget = PanelWidget()
    widget.show()
    sys.exit(app.exec_())
