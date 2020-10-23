# This Python file uses the following encoding: utf-8
import sys
import os
import resource_rc

from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtWidgets import QDesktopWidget

def get_font_avenir():
    return get_font("./fonts/AvenirLTStd-Medium.otf")


def get_font(font_path):
    font = QFont()
    fontId = QFontDatabase.addApplicationFont(font_path)
    fontInfoList = QFontDatabase.applicationFontFamilies(fontId)
    fontFamily = fontInfoList[0]
    font.setFamily(fontFamily)
    return font


FONT_RATIO = 1   # font size ratio

def screen_size():
    screen = QDesktopWidget().screenGeometry()
    print('Screen Resolution:%dx%d' % (screen.width(), screen.height()))
    if screen.width() > 1400:
        global FONT_RATIO
        FONT_RATIO = 1.3
    print('FONT RATIO: ', FONT_RATIO)

