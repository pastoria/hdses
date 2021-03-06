combobox_style_ready = """
QComboBox {  
     background-color: rgba(254, 255, 207, 1);
     border: 0px solid rgba(204, 204, 204, 1);
     border-radius: 3px;
     border-width: 0px; border-style:outset;
     padding-left: 0px;
     outline:0px;
     combobox-popup: 0;
     color: rgba(0, 0, 0, 1);
}
"""

combobox_style_running = """
QComboBox {  
     background-color: rgba(255, 232, 173, 1);
     border: 0px solid rgba(204, 204, 204, 1);
     border-radius: 3px;
     border-width: 0px; border-style:outset;
     padding-left: 0px;
     outline:0px;
     combobox-popup: 0;
     color: rgba(0, 0, 0, 1);
}
"""

combobox_style_bad_sectors = """
QComboBox {  
     background-color: rgba(255, 207, 207, 1);
     border: 0px solid rgba(204, 204, 204, 1);
     border-radius: 3px;
     border-width: 0px; border-style:outset;
     padding-left: 0px;
     outline:0px;
     combobox-popup: 0;
     color: rgba(0, 0, 0, 1);
}

"""
combobox_style_error = """
QComboBox {  
     background-color: rgba(254, 214, 214, 1);
     border: 0px solid rgba(204, 204, 204, 1);
     border-radius: 3px;
     border-width: 0px; border-style:outset;
     padding-left: 0px;
     outline:0px;
     combobox-popup: 0;
     color: rgba(0, 0, 0, 1);
}
"""

combobox_style_success = """
QComboBox {  
     background-color: rgba(218, 251, 206, 1);
     border: 0px solid rgba(204, 204, 204, 1);
     border-radius: 3px;
     border-width: 0px; border-style:outset;
     padding-left: 0px;
     outline:0px;
     combobox-popup: 0;
     color: rgba(0, 0, 0, 1);
}
"""

combobox_style_small = """
QComboBox QAbstractItemView {
    outline: 0px solid red;
    border: 0px solid yellow;
    color: rgba(0, 0, 0, 1);
    padding-left: 0px;
    background-color: rgba(255, 255, 255, 1);
    selection-color: rgba(255, 255, 255, 1);
    selection-background-color: rgba(144, 1, 255, 1);
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 35px;
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

QComboBox::down-arrow:on {
	image: url(:/images/LessButton_Gray.svg);
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
    background: rgba(87, 0, 156, 1);
}

QComboBox QScrollBar::add-line::vertical{
    border:none;
}

QComboBox QScrollBar::sub-line::vertical{
    border:none;
}
"""


combobox_style_big = """
 QComboBox{  background-color: rgba(232, 232, 232, 1);
             border: 1px solid rgba(143, 0, 255, 1);
             border-radius: 5px;
             border-width: 1px; border-style:outset;
             padding-left: 0px;
             font-size: 18px;
             outline:0px;
             combobox-popup: 0;
             color: rgba(0, 0, 0, 1);
}

 QComboBox QAbstractItemView {
    min-height: 40px;
    outline: 0px solid red;
    border: 1px solid rgba(143, 0, 255, 1);
    border-radius: 2px;
    color: rgba(0, 0, 0, 1);
    padding-left: 0px;
    background-color: rgba(255, 255, 255, 1);
    selection-color: rgba(255, 255, 255, 1);
    selection-background-color: rgba(144, 1, 255, 1);
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 35px;
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

QComboBox::down-arrow:on {
	image: url(:/images/LessButton_Purple.svg);
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
    background: rgba(87, 0, 156, 1);
}

QComboBox QScrollBar::add-line::vertical{
    border:none;
}

QComboBox QScrollBar::sub-line::vertical{
    border:none;
}
"""
# MainPanelFrame
# {
#     border: 2px solid #35065a;
# }
mainpanelstyle = """
    MainPanelFrame
    {
        border: 1px solid #35065a;
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
    }transparent
"""

status_style_ready = """
#widget_info {
    background-color: rgba(242, 244, 103, 0.88);
}

#widget_status {
    background-color: #ffffff;
}

#label_1, #label_2, #label_3 {
	color: #809379;
}
"""

status_style_running = """
#widget_info {
    background-color: rgba(244, 198, 79, 1);
}

#widget_status {
    background-color: #ffffff;
}

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
	border-radius: 1px;
}
"""

status_style_bad_sectors = """
#widget_info {
    background-color: rgba(248, 144, 144, 1);
}

#widget_status {
    background-color: #ffffff;
}

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
	border-radius: 1px;
}
"""

status_style_error = """
#widget_info {
    background-color: rgba(255, 62, 62, 1);
}

#widget_status {
    background-color: #ffffff;
}

#label_1, #label_2, #label_3 {
	color: #809379;
}

#label_progress {
	color: rgba(255, 62, 62, 1);
}

QProgressBar {
	background-color: rgba(255, 255, 255, 0);
	border: none;
}

QProgressBar::chunk {
	background-color: rgba(255, 62, 62, 1);
	border-radius: 1px;
}
"""

status_style_success = """
#widget_info {
    background-color: rgba(130, 233, 94, 1);
}

#widget_status {
    background-color: #ffffff;
}

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
	background-color: rgba(130, 233, 94, 1);
	border-radius: 1px;
}
"""

# NotReadyFrame
# {
#     border: 1px solid #35065a;
# }
notreadystyle = """
    NotReadyFrame
    {
        border: 1px solid #35065a;
    }
    QLabel {
        Color: #ffffff;
    }
    #widget_up {
        background: #909090;
    }    
    #widget_down {
        background: #ffffff;
    }
"""
