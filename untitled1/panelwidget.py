# This Python file uses the following encoding: utf-8
import sys
import os


from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QMessageBox
from PyQt5.QtCore import Qt, QFile, QCoreApplication, QTimer, QUrl, QThread, pyqtSignal
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPainter, QColor, QPixmap, QCursor, QDesktopServices

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
    def __init__(self):
        super(PanelWidget, self).__init__()
        loadUi('panelwidget.ui', self)
#        self.setWindowFlags(Qt.FramelessWindowHint)
#        self.setAttribute(Qt.WA_TranslucentBackground)
        self.change_style()

    def change_style(self):
        self.setStyleSheet(qss_status_ready)


if __name__ == "__main__":
    app = QApplication([])
    widget = PanelWidget()
    widget.show()
    sys.exit(app.exec_())
