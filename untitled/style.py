combobox_style_small = """
 QComboBox{  background-color: rgba(255, 255, 255, 1);
             border: 1px solid rgba(204, 204, 204, 1);
             border-radius: 3px;
             border-width: 1px; border-style:outset;
             padding-left: 0px;
             font-size: 14px;
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
    selection-background-color: rgba(204, 204, 204, 1);
}

QComboBox::drop-down {
subcontrol-origin: padding;
subcontrol-position: top right;
width: 30px;
border-left-width: 0px;
border-left-color: gray;
border-left-style: solid;
border-top-right-radius: 3px;
border-bottom-right-radius: 3px;
background:transparent;
}

QComboBox::down-arrow {
	image: url(:/images/MoreButton_Gray.svg);
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

combobox_style_big = """
 QComboBox{  background-color: rgba(255, 255, 255, 1);
             border: 1px solid rgba(143, 0, 255, 1);
             border-radius: 3px;
             border-width: 1px; border-style:outset;
             padding-left: 0px;
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
    selection-background-color: rgba(204, 204, 204, 1);
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

mainpanelstyle = """
    MainPanelFrame {
        border: 2px solid #35065a;
    }
    #widget_info {background-color: #f4c64f;}
    #widget_status {background-color: #ffffff;}
    #label_1, #label_2, #label_3 {
        color: #809379;
    }

    #label_progress {
        color: #2c56e8;
    }

    QProgressBar {
        background-color: rgba(255, 255, 255, 0);
        border: none;
    }

    QProgressBar::chunk {
        background-color: #2c56e8;
        border-radius: 3px;
    }
"""