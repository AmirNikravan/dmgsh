# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLCDNumber, QLabel, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QToolButton, QVBoxLayout, QWidget)

from AnalogGaugeWidget import AnalogGaugeWidget
import rc_rsc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(846, 550)
        MainWindow.setStyleSheet(u"background-color: rgb(39, 51, 109);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(39, 51, 109);")
        self.gauges = QWidget()
        self.gauges.setObjectName(u"gauges")
        self.gridLayout = QGridLayout(self.gauges)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.gauges)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = AnalogGaugeWidget(self.frame_2)
        self.widget.setObjectName(u"widget")

        self.verticalLayout_2.addWidget(self.widget)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(15, 0))
        self.label.setMaximumSize(QSize(16777215, 13))

        self.verticalLayout_2.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_2 = AnalogGaugeWidget(self.frame_4)
        self.widget_2.setObjectName(u"widget_2")

        self.verticalLayout_3.addWidget(self.widget_2)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(15, 0))
        self.label_2.setMaximumSize(QSize(16777215, 13))

        self.verticalLayout_3.addWidget(self.label_2)


        self.horizontalLayout_2.addWidget(self.frame_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 9))

        self.verticalLayout_4.addWidget(self.label_4)


        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.gauges)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_3 = AnalogGaugeWidget(self.frame_6)
        self.widget_3.setObjectName(u"widget_3")

        self.verticalLayout_6.addWidget(self.widget_3)

        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(15, 0))
        self.label_5.setMaximumSize(QSize(16777215, 13))

        self.verticalLayout_6.addWidget(self.label_5)


        self.horizontalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_4 = AnalogGaugeWidget(self.frame_7)
        self.widget_4.setObjectName(u"widget_4")

        self.verticalLayout_7.addWidget(self.widget_4)

        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(15, 0))
        self.label_6.setMaximumSize(QSize(16777215, 13))

        self.verticalLayout_7.addWidget(self.label_6)


        self.horizontalLayout_3.addWidget(self.frame_7)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 9))

        self.verticalLayout_5.addWidget(self.label_7)


        self.gridLayout.addWidget(self.frame_5, 0, 1, 1, 1)

        self.frame_8 = QFrame(self.gauges)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.widget_5 = AnalogGaugeWidget(self.frame_9)
        self.widget_5.setObjectName(u"widget_5")

        self.verticalLayout_9.addWidget(self.widget_5)

        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(15, 0))
        self.label_8.setMaximumSize(QSize(16777215, 13))

        self.verticalLayout_9.addWidget(self.label_8)


        self.horizontalLayout_4.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_6 = AnalogGaugeWidget(self.frame_10)
        self.widget_6.setObjectName(u"widget_6")

        self.verticalLayout_10.addWidget(self.widget_6)

        self.label_9 = QLabel(self.frame_10)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(15, 0))
        self.label_9.setMaximumSize(QSize(16777215, 13))

        self.verticalLayout_10.addWidget(self.label_9)


        self.horizontalLayout_4.addWidget(self.frame_10)


        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.label_10 = QLabel(self.frame_8)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 9))

        self.verticalLayout_8.addWidget(self.label_10)


        self.gridLayout.addWidget(self.frame_8, 0, 2, 1, 1)

        self.frame_11 = QFrame(self.gauges)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_11)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_12)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_7 = AnalogGaugeWidget(self.frame_12)
        self.widget_7.setObjectName(u"widget_7")

        self.verticalLayout_12.addWidget(self.widget_7)

        self.label_11 = QLabel(self.frame_12)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(15, 0))
        self.label_11.setMaximumSize(QSize(16777215, 13))

        self.verticalLayout_12.addWidget(self.label_11)


        self.horizontalLayout_5.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_13)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.widget_8 = AnalogGaugeWidget(self.frame_13)
        self.widget_8.setObjectName(u"widget_8")

        self.verticalLayout_13.addWidget(self.widget_8)

        self.label_12 = QLabel(self.frame_13)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(15, 0))
        self.label_12.setMaximumSize(QSize(16777215, 13))

        self.verticalLayout_13.addWidget(self.label_12)


        self.horizontalLayout_5.addWidget(self.frame_13)


        self.verticalLayout_11.addLayout(self.horizontalLayout_5)

        self.label_13 = QLabel(self.frame_11)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 9))

        self.verticalLayout_11.addWidget(self.label_13)


        self.gridLayout.addWidget(self.frame_11, 1, 0, 1, 1)

        self.frame_14 = QFrame(self.gauges)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_14)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_15)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.widget_9 = AnalogGaugeWidget(self.frame_15)
        self.widget_9.setObjectName(u"widget_9")

        self.verticalLayout_15.addWidget(self.widget_9)

        self.label_14 = QLabel(self.frame_15)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(15, 0))
        self.label_14.setMaximumSize(QSize(16777215, 13))

        self.verticalLayout_15.addWidget(self.label_14)


        self.horizontalLayout_6.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_16)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.widget_10 = AnalogGaugeWidget(self.frame_16)
        self.widget_10.setObjectName(u"widget_10")

        self.verticalLayout_16.addWidget(self.widget_10)

        self.label_15 = QLabel(self.frame_16)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(15, 0))
        self.label_15.setMaximumSize(QSize(16777215, 13))

        self.verticalLayout_16.addWidget(self.label_15)


        self.horizontalLayout_6.addWidget(self.frame_16)


        self.verticalLayout_14.addLayout(self.horizontalLayout_6)

        self.label_16 = QLabel(self.frame_14)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(16777215, 9))

        self.verticalLayout_14.addWidget(self.label_16)


        self.gridLayout.addWidget(self.frame_14, 1, 1, 1, 1)

        self.frame_17 = QFrame(self.gauges)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_17)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_18)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.widget_11 = AnalogGaugeWidget(self.frame_18)
        self.widget_11.setObjectName(u"widget_11")

        self.verticalLayout_18.addWidget(self.widget_11)

        self.label_17 = QLabel(self.frame_18)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(15, 0))
        self.label_17.setMaximumSize(QSize(16777215, 13))

        self.verticalLayout_18.addWidget(self.label_17)


        self.horizontalLayout_7.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_17)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_19)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.widget_12 = QWidget(self.frame_19)
        self.widget_12.setObjectName(u"widget_12")

        self.verticalLayout_19.addWidget(self.widget_12)

        self.label_18 = QLabel(self.frame_19)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(15, 0))
        self.label_18.setMaximumSize(QSize(16777215, 13))

        self.verticalLayout_19.addWidget(self.label_18)


        self.horizontalLayout_7.addWidget(self.frame_19)


        self.verticalLayout_17.addLayout(self.horizontalLayout_7)

        self.label_19 = QLabel(self.frame_17)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 9))

        self.verticalLayout_17.addWidget(self.label_19)


        self.gridLayout.addWidget(self.frame_17, 1, 2, 1, 1)

        self.stackedWidget.addWidget(self.gauges)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_3 = QGridLayout(self.page_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_20 = QFrame(self.page_3)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_20)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(112, 490))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_22)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.toolButton_lamptest = QToolButton(self.frame_22)
        self.toolButton_lamptest.setObjectName(u"toolButton_lamptest")
        self.toolButton_lamptest.setStyleSheet(u"            #toolButton_lamptest {\n"
"                background-color: rgb(93, 93, 93);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 40px;\n"
"                border-color: rgb(232, 232, 232);\n"
"            }\n"
"            #toolButton_lamptest:pressed {\n"
"                background-color: red;\n"
"            }")
        icon = QIcon()
        icon.addFile(u":/icons/icons/button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_lamptest.setIcon(icon)
        self.toolButton_lamptest.setIconSize(QSize(512, 512))

        self.verticalLayout_20.addWidget(self.toolButton_lamptest)

        self.label_24 = QLabel(self.frame_22)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(16777215, 14))

        self.verticalLayout_20.addWidget(self.label_24)

        self.toolButton_lop = QToolButton(self.frame_22)
        self.toolButton_lop.setObjectName(u"toolButton_lop")
        self.toolButton_lop.setStyleSheet(u"            #toolButton_lop {\n"
"                background-color: rgb(93, 93, 93);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 40px;\n"
"                border-color: rgb(232, 232, 232);\n"
"            }\n"
"            #toolButton_lop:pressed {\n"
"                background-color: red;\n"
"            }")
        self.toolButton_lop.setIcon(icon)
        self.toolButton_lop.setIconSize(QSize(512, 512))

        self.verticalLayout_20.addWidget(self.toolButton_lop)

        self.label_25 = QLabel(self.frame_22)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(16777215, 14))

        self.verticalLayout_20.addWidget(self.label_25)

        self.toolButton_mcr = QToolButton(self.frame_22)
        self.toolButton_mcr.setObjectName(u"toolButton_mcr")
        self.toolButton_mcr.setStyleSheet(u"            #toolButton_mcr {\n"
"                background-color: rgb(93, 93, 93);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 40px;\n"
"                border-color: rgb(232, 232, 232);\n"
"            }\n"
"            #toolButton_mcr:pressed {\n"
"                background-color: red;\n"
"            }")
        self.toolButton_mcr.setIcon(icon)
        self.toolButton_mcr.setIconSize(QSize(512, 512))

        self.verticalLayout_20.addWidget(self.toolButton_mcr)

        self.label_26 = QLabel(self.frame_22)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(16777215, 14))

        self.verticalLayout_20.addWidget(self.label_26)

        self.toolButton_bridge = QToolButton(self.frame_22)
        self.toolButton_bridge.setObjectName(u"toolButton_bridge")
        self.toolButton_bridge.setStyleSheet(u"            #toolButton_bridge {\n"
"                background-color: rgb(93, 93, 93);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 40px;\n"
"                border-color: rgb(232, 232, 232);\n"
"            }\n"
"            #toolButton_bridge:pressed {\n"
"                background-color: red;\n"
"            }")
        self.toolButton_bridge.setIcon(icon)
        self.toolButton_bridge.setIconSize(QSize(512, 512))

        self.verticalLayout_20.addWidget(self.toolButton_bridge)

        self.label_27 = QLabel(self.frame_22)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(16777215, 14))

        self.verticalLayout_20.addWidget(self.label_27)


        self.gridLayout_2.addWidget(self.frame_22, 0, 0, 1, 1)

        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(112, 490))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_21)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.pushButton_control = QPushButton(self.frame_21)
        self.pushButton_control.setObjectName(u"pushButton_control")
        self.pushButton_control.setMinimumSize(QSize(74, 86))
        self.pushButton_control.setStyleSheet(u"            #pushButton_control {\n"
"                background-color: rgb(93, 93, 93);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 40px;\n"
"                border-color: rgb(232, 232, 232);\n"
"            }\n"
"            #pushButton_control:pressed {\n"
"                background-color: red;\n"
"            }")

        self.verticalLayout_21.addWidget(self.pushButton_control)

        self.label_20 = QLabel(self.frame_21)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(16777215, 14))

        self.verticalLayout_21.addWidget(self.label_20)

        self.pushButton_control_2 = QPushButton(self.frame_21)
        self.pushButton_control_2.setObjectName(u"pushButton_control_2")
        self.pushButton_control_2.setMinimumSize(QSize(74, 86))
        self.pushButton_control_2.setStyleSheet(u"            #pushButton_control_2 {\n"
"                background-color: rgb(93, 93, 93);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 40px;\n"
"                border-color: rgb(232, 232, 232);\n"
"            }\n"
"            #pushButton_control_2:pressed\n"
" {\n"
"                background-color: red;\n"
"            }")

        self.verticalLayout_21.addWidget(self.pushButton_control_2)

        self.label_21 = QLabel(self.frame_21)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 14))

        self.verticalLayout_21.addWidget(self.label_21)

        self.toolButton = QToolButton(self.frame_21)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setStyleSheet(u"            #toolButton {\n"
"                background-color: rgb(93, 93, 93);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 40px;\n"
"                border-color: rgb(232, 232, 232);\n"
"            }\n"
"            #toolButton:pressed {\n"
"                background-color: red;\n"
"            }")
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QSize(512, 512))

        self.verticalLayout_21.addWidget(self.toolButton)

        self.label_22 = QLabel(self.frame_21)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(16777215, 14))

        self.verticalLayout_21.addWidget(self.label_22)

        self.toolButton_2 = QToolButton(self.frame_21)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setStyleSheet(u"            #toolButton_2 {\n"
"                background-color: rgb(93, 93, 93);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 40px;\n"
"                border-color: rgb(232, 232, 232);\n"
"            }\n"
"            #toolButton_2:pressed {\n"
"                background-color: red;\n"
"            }")
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setIconSize(QSize(512, 512))

        self.verticalLayout_21.addWidget(self.toolButton_2)

        self.label_23 = QLabel(self.frame_21)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(16777215, 14))

        self.verticalLayout_21.addWidget(self.label_23)


        self.gridLayout_2.addWidget(self.frame_21, 0, 1, 1, 1)

        self.frame_23 = QFrame(self.frame_20)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(112, 490))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_23)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.toolButton_7 = QToolButton(self.frame_23)
        self.toolButton_7.setObjectName(u"toolButton_7")
        self.toolButton_7.setStyleSheet(u"            #toolButton_3 {\n"
"                background-color: rgb(93, 93, 93);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 40px;\n"
"                border-color: rgb(232, 232, 232);\n"
"            }\n"
"            #toolButton_3:pressed {\n"
"                background-color: red;\n"
"            }")
        self.toolButton_7.setIcon(icon)
        self.toolButton_7.setIconSize(QSize(512, 512))

        self.verticalLayout_22.addWidget(self.toolButton_7)

        self.label_28 = QLabel(self.frame_23)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(16777215, 14))

        self.verticalLayout_22.addWidget(self.label_28)

        self.pushButton_control_3 = QPushButton(self.frame_23)
        self.pushButton_control_3.setObjectName(u"pushButton_control_3")
        self.pushButton_control_3.setMinimumSize(QSize(74, 86))
        self.pushButton_control_3.setStyleSheet(u"            #pushButton_control_2 {\n"
"                background-color: rgb(93, 93, 93);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 40px;\n"
"                border-color: rgb(232, 232, 232);\n"
"            }\n"
"            #pushButton_control_2:pressed {\n"
"                background-color: red;\n"
"            }")

        self.verticalLayout_22.addWidget(self.pushButton_control_3)

        self.label_31 = QLabel(self.frame_23)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(16777215, 14))

        self.verticalLayout_22.addWidget(self.label_31)

        self.toolButton_8 = QToolButton(self.frame_23)
        self.toolButton_8.setObjectName(u"toolButton_8")
        self.toolButton_8.setStyleSheet(u"            #toolButton_3 {\n"
"                background-color: rgb(93, 93, 93);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 40px;\n"
"                border-color: rgb(232, 232, 232);\n"
"            }\n"
"            #toolButton_3:pressed {\n"
"                background-color: red;\n"
"            }")
        self.toolButton_8.setIcon(icon)
        self.toolButton_8.setIconSize(QSize(512, 512))

        self.verticalLayout_22.addWidget(self.toolButton_8)

        self.label_29 = QLabel(self.frame_23)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(16777215, 14))

        self.verticalLayout_22.addWidget(self.label_29)

        self.toolButton_9 = QToolButton(self.frame_23)
        self.toolButton_9.setObjectName(u"toolButton_9")
        self.toolButton_9.setStyleSheet(u"            #toolButton_3 {\n"
"                background-color: rgb(93, 93, 93);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 40px;\n"
"                border-color: rgb(232, 232, 232);\n"
"            }\n"
"            #toolButton_3:pressed {\n"
"                background-color: red;\n"
"            }")
        self.toolButton_9.setIcon(icon)
        self.toolButton_9.setIconSize(QSize(512, 512))

        self.verticalLayout_22.addWidget(self.toolButton_9)

        self.label_30 = QLabel(self.frame_23)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(16777215, 14))

        self.verticalLayout_22.addWidget(self.label_30)


        self.gridLayout_2.addWidget(self.frame_23, 0, 2, 1, 1)

        self.frame_24 = QFrame(self.frame_20)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(112, 490))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_24)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.pushButton_control_4 = QPushButton(self.frame_24)
        self.pushButton_control_4.setObjectName(u"pushButton_control_4")
        self.pushButton_control_4.setMinimumSize(QSize(74, 86))
        self.pushButton_control_4.setStyleSheet(u"            #pushButton_control {\n"
"                background-color: rgb(93, 93, 93);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 40px;\n"
"                border-color: rgb(232, 232, 232);\n"
"            }\n"
"            #pushButton_control:pressed {\n"
"                background-color: red;\n"
"            }")

        self.verticalLayout_23.addWidget(self.pushButton_control_4)

        self.label_32 = QLabel(self.frame_24)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(16777215, 14))

        self.verticalLayout_23.addWidget(self.label_32)

        self.toolButton_10 = QToolButton(self.frame_24)
        self.toolButton_10.setObjectName(u"toolButton_10")
        self.toolButton_10.setStyleSheet(u"            #toolButton {\n"
"                background-color: rgb(93, 93, 93);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 40px;\n"
"                border-color: rgb(232, 232, 232);\n"
"            }\n"
"            #toolButton:pressed {\n"
"                background-color: red;\n"
"            }")
        self.toolButton_10.setIcon(icon)
        self.toolButton_10.setIconSize(QSize(512, 512))

        self.verticalLayout_23.addWidget(self.toolButton_10)

        self.label_34 = QLabel(self.frame_24)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(16777215, 14))

        self.verticalLayout_23.addWidget(self.label_34)

        self.toolButton_12 = QToolButton(self.frame_24)
        self.toolButton_12.setObjectName(u"toolButton_12")
        self.toolButton_12.setStyleSheet(u"            #toolButton {\n"
"                background-color: rgb(93, 93, 93);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 40px;\n"
"                border-color: rgb(232, 232, 232);\n"
"            }\n"
"            #toolButton:pressed {\n"
"                background-color: red;\n"
"            }")
        self.toolButton_12.setIcon(icon)
        self.toolButton_12.setIconSize(QSize(512, 512))

        self.verticalLayout_23.addWidget(self.toolButton_12)

        self.label_36 = QLabel(self.frame_24)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(16777215, 14))

        self.verticalLayout_23.addWidget(self.label_36)

        self.toolButton_14 = QToolButton(self.frame_24)
        self.toolButton_14.setObjectName(u"toolButton_14")
        self.toolButton_14.setStyleSheet(u"            #toolButton {\n"
"                background-color: rgb(93, 93, 93);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 40px;\n"
"                border-color: rgb(232, 232, 232);\n"
"            }\n"
"            #toolButton:pressed {\n"
"                background-color: red;\n"
"            }")
        self.toolButton_14.setIcon(icon)
        self.toolButton_14.setIconSize(QSize(512, 512))

        self.verticalLayout_23.addWidget(self.toolButton_14)

        self.label_38 = QLabel(self.frame_24)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMaximumSize(QSize(16777215, 14))

        self.verticalLayout_23.addWidget(self.label_38)


        self.gridLayout_2.addWidget(self.frame_24, 0, 3, 1, 1)

        self.frame_25 = QFrame(self.frame_20)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMaximumSize(QSize(112, 490))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_25)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.pushButton_control_5 = QPushButton(self.frame_25)
        self.pushButton_control_5.setObjectName(u"pushButton_control_5")
        self.pushButton_control_5.setMinimumSize(QSize(74, 86))
        self.pushButton_control_5.setStyleSheet(u"            #pushButton_control {\n"
"                background-color: rgb(93, 93, 93);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 40px;\n"
"                border-color: rgb(232, 232, 232);\n"
"            }\n"
"            #pushButton_control:pressed {\n"
"                background-color: red;\n"
"            }")

        self.verticalLayout_24.addWidget(self.pushButton_control_5)

        self.label_33 = QLabel(self.frame_25)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(16777215, 14))

        self.verticalLayout_24.addWidget(self.label_33)

        self.toolButton_11 = QToolButton(self.frame_25)
        self.toolButton_11.setObjectName(u"toolButton_11")
        self.toolButton_11.setStyleSheet(u"            #toolButton {\n"
"                background-color: rgb(93, 93, 93);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 40px;\n"
"                border-color: rgb(232, 232, 232);\n"
"            }\n"
"            #toolButton:pressed {\n"
"                background-color: red;\n"
"            }")
        self.toolButton_11.setIcon(icon)
        self.toolButton_11.setIconSize(QSize(512, 512))

        self.verticalLayout_24.addWidget(self.toolButton_11)

        self.label_35 = QLabel(self.frame_25)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(16777215, 14))

        self.verticalLayout_24.addWidget(self.label_35)

        self.toolButton_13 = QToolButton(self.frame_25)
        self.toolButton_13.setObjectName(u"toolButton_13")
        self.toolButton_13.setStyleSheet(u"            #toolButton {\n"
"                background-color: rgb(93, 93, 93);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 40px;\n"
"                border-color: rgb(232, 232, 232);\n"
"            }\n"
"            #toolButton:pressed {\n"
"                background-color: red;\n"
"            }")
        self.toolButton_13.setIcon(icon)
        self.toolButton_13.setIconSize(QSize(512, 512))

        self.verticalLayout_24.addWidget(self.toolButton_13)

        self.label_37 = QLabel(self.frame_25)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(16777215, 14))

        self.verticalLayout_24.addWidget(self.label_37)

        self.toolButton_15 = QToolButton(self.frame_25)
        self.toolButton_15.setObjectName(u"toolButton_15")
        self.toolButton_15.setStyleSheet(u"            #toolButton {\n"
"                background-color: rgb(93, 93, 93);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 40px;\n"
"                border-color: rgb(232, 232, 232);\n"
"            }\n"
"            #toolButton:pressed {\n"
"                background-color: red;\n"
"            }")
        self.toolButton_15.setIcon(icon)
        self.toolButton_15.setIconSize(QSize(512, 512))

        self.verticalLayout_24.addWidget(self.toolButton_15)

        self.label_39 = QLabel(self.frame_25)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(16777215, 14))

        self.verticalLayout_24.addWidget(self.label_39)


        self.gridLayout_2.addWidget(self.frame_25, 0, 4, 1, 1)


        self.gridLayout_3.addWidget(self.frame_20, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.gmp = QWidget()
        self.gmp.setObjectName(u"gmp")
        self.horizontalLayout_9 = QHBoxLayout(self.gmp)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_32 = QFrame(self.gmp)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.stackedWidget_2 = QStackedWidget(self.frame_32)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMaximumSize(QSize(900, 16777215))
        self.stackedWidget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_8 = QHBoxLayout(self.page)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_26 = QFrame(self.page)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.lcdNumber = QLCDNumber(self.frame_26)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setEnabled(False)
        self.lcdNumber.setGeometry(QRect(50, 430, 54, 23))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        self.lcdNumber.setMaximumSize(QSize(54, 16777215))
        self.lcdNumber.setLayoutDirection(Qt.LeftToRight)
        self.line = QFrame(self.frame_26)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(47, 107, 3, 312))
        self.line.setMinimumSize(QSize(0, 0))
        self.line.setMaximumSize(QSize(5, 16777215))
        self.line.setStyleSheet(u"background-color: rgb(38, 162, 105);")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.progressBar = QProgressBar(self.frame_26)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 40, 61, 381))
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setMaximum(2200)
        self.progressBar.setValue(2100)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(Qt.Vertical)
        self.line_2 = QFrame(self.frame_26)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(45, 40, 2, 380))
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_3 = QLabel(self.frame_26)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(15, 391, 28, 16))
        self.label_40 = QLabel(self.frame_26)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(15, 375, 28, 16))
        self.label_41 = QLabel(self.frame_26)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(15, 358, 28, 16))
        self.label_42 = QLabel(self.frame_26)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(15, 340, 28, 16))
        self.label_43 = QLabel(self.frame_26)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(15, 323, 28, 16))
        self.label_44 = QLabel(self.frame_26)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(15, 306, 28, 16))
        self.label_45 = QLabel(self.frame_26)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(15, 287, 28, 16))
        self.label_46 = QLabel(self.frame_26)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(15, 270, 28, 16))
        self.label_47 = QLabel(self.frame_26)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(15, 254, 28, 16))
        self.label_48 = QLabel(self.frame_26)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(8, 236, 37, 16))
        self.label_49 = QLabel(self.frame_26)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(8, 219, 37, 16))
        self.label_50 = QLabel(self.frame_26)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(8, 202, 37, 16))
        self.label_52 = QLabel(self.frame_26)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(8, 184, 37, 16))
        self.label_53 = QLabel(self.frame_26)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(8, 167, 37, 16))
        self.label_54 = QLabel(self.frame_26)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(8, 149, 37, 16))
        self.label_55 = QLabel(self.frame_26)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(8, 132, 37, 16))
        self.label_56 = QLabel(self.frame_26)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(8, 114, 37, 16))
        self.label_57 = QLabel(self.frame_26)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(8, 98, 37, 16))
        self.label_58 = QLabel(self.frame_26)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(8, 80, 37, 16))
        self.label_59 = QLabel(self.frame_26)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(8, 63, 37, 16))
        self.label_60 = QLabel(self.frame_26)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(8, 47, 37, 16))
        self.label_61 = QLabel(self.frame_26)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(8, 33, 37, 16))
        self.line_3 = QFrame(self.frame_26)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(47, 81, 3, 26))
        self.line_3.setMinimumSize(QSize(0, 0))
        self.line_3.setMaximumSize(QSize(5, 16777215))
        self.line_3.setStyleSheet(u"background-color: rgb(248, 228, 92);")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_4 = QFrame(self.frame_26)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(47, 40, 3, 43))
        self.line_4.setMinimumSize(QSize(0, 0))
        self.line_4.setMaximumSize(QSize(5, 16777215))
        self.line_4.setStyleSheet(u"background-color: rgb(224, 27, 36);")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_51 = QLabel(self.frame_26)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(60, 10, 17, 17))

        self.horizontalLayout_8.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.page)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.lcdNumber_2 = QLCDNumber(self.frame_27)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setEnabled(False)
        self.lcdNumber_2.setGeometry(QRect(50, 430, 54, 23))
        sizePolicy.setHeightForWidth(self.lcdNumber_2.sizePolicy().hasHeightForWidth())
        self.lcdNumber_2.setSizePolicy(sizePolicy)
        self.lcdNumber_2.setMaximumSize(QSize(54, 16777215))
        self.lcdNumber_2.setLayoutDirection(Qt.LeftToRight)
        self.line_5 = QFrame(self.frame_27)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(47, 164, 3, 223))
        self.line_5.setMinimumSize(QSize(0, 0))
        self.line_5.setMaximumSize(QSize(5, 16777215))
        self.line_5.setStyleSheet(u"background-color: rgb(38, 162, 105);")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)
        self.progressBar_2 = QProgressBar(self.frame_27)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setGeometry(QRect(50, 40, 61, 381))
        self.progressBar_2.setStyleSheet(u"")
        self.progressBar_2.setMaximum(1200)
        self.progressBar_2.setValue(1100)
        self.progressBar_2.setTextVisible(False)
        self.progressBar_2.setOrientation(Qt.Vertical)
        self.line_6 = QFrame(self.frame_27)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(45, 41, 2, 380))
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_62 = QLabel(self.frame_27)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(15, 378, 28, 16))
        self.label_63 = QLabel(self.frame_27)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(15, 346, 28, 16))
        self.label_64 = QLabel(self.frame_27)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(15, 315, 28, 16))
        self.label_65 = QLabel(self.frame_27)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(15, 281, 28, 16))
        self.label_66 = QLabel(self.frame_27)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(15, 251, 28, 16))
        self.label_67 = QLabel(self.frame_27)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(15, 220, 28, 16))
        self.label_68 = QLabel(self.frame_27)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(15, 188, 28, 16))
        self.label_69 = QLabel(self.frame_27)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(15, 156, 28, 16))
        self.label_70 = QLabel(self.frame_27)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(15, 124, 28, 16))
        self.label_71 = QLabel(self.frame_27)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(8, 93, 37, 16))
        self.label_72 = QLabel(self.frame_27)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(8, 61, 37, 16))
        self.label_73 = QLabel(self.frame_27)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(8, 33, 37, 16))
        self.line_7 = QFrame(self.frame_27)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(47, 133, 3, 33))
        self.line_7.setMinimumSize(QSize(0, 0))
        self.line_7.setMaximumSize(QSize(5, 16777215))
        self.line_7.setStyleSheet(u"background-color: rgb(248, 228, 92);")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_8 = QFrame(self.frame_27)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(47, 40, 3, 93))
        self.line_8.setMinimumSize(QSize(0, 0))
        self.line_8.setMaximumSize(QSize(5, 16777215))
        self.line_8.setStyleSheet(u"background-color: rgb(224, 27, 36);")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_84 = QLabel(self.frame_27)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setGeometry(QRect(60, 10, 14, 17))
        self.line_9 = QFrame(self.frame_27)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(47, 387, 3, 32))
        self.line_9.setMinimumSize(QSize(0, 0))
        self.line_9.setMaximumSize(QSize(5, 16777215))
        self.line_9.setStyleSheet(u"background-color: rgb(248, 228, 92);")
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_8.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.page)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.lcdNumber_3 = QLCDNumber(self.frame_28)
        self.lcdNumber_3.setObjectName(u"lcdNumber_3")
        self.lcdNumber_3.setEnabled(False)
        self.lcdNumber_3.setGeometry(QRect(50, 430, 54, 23))
        sizePolicy.setHeightForWidth(self.lcdNumber_3.sizePolicy().hasHeightForWidth())
        self.lcdNumber_3.setSizePolicy(sizePolicy)
        self.lcdNumber_3.setMaximumSize(QSize(54, 16777215))
        self.lcdNumber_3.setLayoutDirection(Qt.LeftToRight)
        self.line_10 = QFrame(self.frame_28)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setGeometry(QRect(47, 164, 3, 223))
        self.line_10.setMinimumSize(QSize(0, 0))
        self.line_10.setMaximumSize(QSize(5, 16777215))
        self.line_10.setStyleSheet(u"background-color: rgb(38, 162, 105);")
        self.line_10.setFrameShape(QFrame.Shape.VLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)
        self.progressBar_3 = QProgressBar(self.frame_28)
        self.progressBar_3.setObjectName(u"progressBar_3")
        self.progressBar_3.setGeometry(QRect(50, 40, 61, 381))
        self.progressBar_3.setStyleSheet(u"")
        self.progressBar_3.setMaximum(1200)
        self.progressBar_3.setValue(1100)
        self.progressBar_3.setTextVisible(False)
        self.progressBar_3.setOrientation(Qt.Vertical)
        self.line_11 = QFrame(self.frame_28)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setGeometry(QRect(45, 41, 2, 380))
        self.line_11.setFrameShape(QFrame.Shape.VLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_74 = QLabel(self.frame_28)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(15, 378, 28, 16))
        self.label_75 = QLabel(self.frame_28)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(15, 346, 28, 16))
        self.label_76 = QLabel(self.frame_28)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(15, 315, 28, 16))
        self.label_77 = QLabel(self.frame_28)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setGeometry(QRect(15, 281, 28, 16))
        self.label_78 = QLabel(self.frame_28)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setGeometry(QRect(15, 251, 28, 16))
        self.label_79 = QLabel(self.frame_28)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(15, 220, 28, 16))
        self.label_80 = QLabel(self.frame_28)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setGeometry(QRect(15, 188, 28, 16))
        self.label_81 = QLabel(self.frame_28)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setGeometry(QRect(15, 156, 28, 16))
        self.label_82 = QLabel(self.frame_28)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setGeometry(QRect(15, 124, 28, 16))
        self.label_83 = QLabel(self.frame_28)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setGeometry(QRect(8, 93, 37, 16))
        self.label_85 = QLabel(self.frame_28)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setGeometry(QRect(8, 61, 37, 16))
        self.label_86 = QLabel(self.frame_28)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setGeometry(QRect(8, 33, 37, 16))
        self.line_12 = QFrame(self.frame_28)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setGeometry(QRect(47, 133, 3, 33))
        self.line_12.setMinimumSize(QSize(0, 0))
        self.line_12.setMaximumSize(QSize(5, 16777215))
        self.line_12.setStyleSheet(u"background-color: rgb(248, 228, 92);")
        self.line_12.setFrameShape(QFrame.Shape.VLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_21 = QFrame(self.frame_28)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setGeometry(QRect(47, 40, 3, 93))
        self.line_21.setMinimumSize(QSize(0, 0))
        self.line_21.setMaximumSize(QSize(5, 16777215))
        self.line_21.setStyleSheet(u"background-color: rgb(224, 27, 36);")
        self.line_21.setFrameShape(QFrame.Shape.VLine)
        self.line_21.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_87 = QLabel(self.frame_28)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setGeometry(QRect(60, 10, 14, 17))
        self.line_22 = QFrame(self.frame_28)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setGeometry(QRect(47, 387, 3, 32))
        self.line_22.setMinimumSize(QSize(0, 0))
        self.line_22.setMaximumSize(QSize(5, 16777215))
        self.line_22.setStyleSheet(u"background-color: rgb(248, 228, 92);")
        self.line_22.setFrameShape(QFrame.Shape.VLine)
        self.line_22.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_8.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.page)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.lcdNumber_4 = QLCDNumber(self.frame_29)
        self.lcdNumber_4.setObjectName(u"lcdNumber_4")
        self.lcdNumber_4.setEnabled(False)
        self.lcdNumber_4.setGeometry(QRect(50, 430, 54, 23))
        sizePolicy.setHeightForWidth(self.lcdNumber_4.sizePolicy().hasHeightForWidth())
        self.lcdNumber_4.setSizePolicy(sizePolicy)
        self.lcdNumber_4.setMaximumSize(QSize(54, 16777215))
        self.lcdNumber_4.setLayoutDirection(Qt.LeftToRight)
        self.line_13 = QFrame(self.frame_29)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setGeometry(QRect(47, 213, 3, 206))
        self.line_13.setMinimumSize(QSize(0, 0))
        self.line_13.setMaximumSize(QSize(5, 16777215))
        self.line_13.setStyleSheet(u"background-color: rgb(38, 162, 105);")
        self.line_13.setFrameShape(QFrame.Shape.VLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)
        self.progressBar_4 = QProgressBar(self.frame_29)
        self.progressBar_4.setObjectName(u"progressBar_4")
        self.progressBar_4.setGeometry(QRect(50, 40, 61, 381))
        self.progressBar_4.setStyleSheet(u"")
        self.progressBar_4.setMaximum(120)
        self.progressBar_4.setValue(110)
        self.progressBar_4.setTextVisible(False)
        self.progressBar_4.setOrientation(Qt.Vertical)
        self.line_14 = QFrame(self.frame_29)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setGeometry(QRect(45, 40, 2, 380))
        self.line_14.setFrameShape(QFrame.Shape.VLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_108 = QLabel(self.frame_29)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setGeometry(QRect(21, 378, 24, 16))
        self.line_15 = QFrame(self.frame_29)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setGeometry(QRect(47, 197, 3, 16))
        self.line_15.setMinimumSize(QSize(0, 0))
        self.line_15.setMaximumSize(QSize(5, 16777215))
        self.line_15.setStyleSheet(u"background-color: rgb(248, 228, 92);")
        self.line_15.setFrameShape(QFrame.Shape.VLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_16 = QFrame(self.frame_29)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setGeometry(QRect(47, 40, 3, 159))
        self.line_16.setMinimumSize(QSize(0, 0))
        self.line_16.setMaximumSize(QSize(5, 16777215))
        self.line_16.setStyleSheet(u"background-color: rgb(224, 27, 36);")
        self.line_16.setFrameShape(QFrame.Shape.VLine)
        self.line_16.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_130 = QLabel(self.frame_29)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setGeometry(QRect(60, 10, 17, 17))
        self.label_109 = QLabel(self.frame_29)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setGeometry(QRect(21, 346, 24, 16))
        self.label_110 = QLabel(self.frame_29)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setGeometry(QRect(21, 314, 24, 16))
        self.label_111 = QLabel(self.frame_29)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setGeometry(QRect(21, 282, 24, 16))
        self.label_112 = QLabel(self.frame_29)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setGeometry(QRect(21, 251, 24, 16))
        self.label_113 = QLabel(self.frame_29)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setGeometry(QRect(21, 220, 24, 16))
        self.label_114 = QLabel(self.frame_29)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setGeometry(QRect(21, 188, 24, 16))
        self.label_115 = QLabel(self.frame_29)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setGeometry(QRect(21, 155, 24, 16))
        self.label_116 = QLabel(self.frame_29)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setGeometry(QRect(21, 124, 24, 16))
        self.label_117 = QLabel(self.frame_29)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setGeometry(QRect(14, 90, 31, 20))
        self.label_118 = QLabel(self.frame_29)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setGeometry(QRect(14, 60, 31, 20))
        self.label_119 = QLabel(self.frame_29)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setGeometry(QRect(14, 31, 31, 20))

        self.horizontalLayout_8.addWidget(self.frame_29)

        self.frame_31 = QFrame(self.page)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.lcdNumber_5 = QLCDNumber(self.frame_31)
        self.lcdNumber_5.setObjectName(u"lcdNumber_5")
        self.lcdNumber_5.setEnabled(False)
        self.lcdNumber_5.setGeometry(QRect(50, 430, 54, 23))
        sizePolicy.setHeightForWidth(self.lcdNumber_5.sizePolicy().hasHeightForWidth())
        self.lcdNumber_5.setSizePolicy(sizePolicy)
        self.lcdNumber_5.setMaximumSize(QSize(54, 16777215))
        self.lcdNumber_5.setLayoutDirection(Qt.LeftToRight)
        self.line_17 = QFrame(self.frame_31)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setGeometry(QRect(47, 213, 3, 206))
        self.line_17.setMinimumSize(QSize(0, 0))
        self.line_17.setMaximumSize(QSize(5, 16777215))
        self.line_17.setStyleSheet(u"background-color: rgb(38, 162, 105);")
        self.line_17.setFrameShape(QFrame.Shape.VLine)
        self.line_17.setFrameShadow(QFrame.Shadow.Sunken)
        self.progressBar_5 = QProgressBar(self.frame_31)
        self.progressBar_5.setObjectName(u"progressBar_5")
        self.progressBar_5.setGeometry(QRect(50, 40, 61, 381))
        self.progressBar_5.setStyleSheet(u"")
        self.progressBar_5.setMaximum(120)
        self.progressBar_5.setValue(110)
        self.progressBar_5.setTextVisible(False)
        self.progressBar_5.setOrientation(Qt.Vertical)
        self.line_18 = QFrame(self.frame_31)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setGeometry(QRect(45, 40, 2, 380))
        self.line_18.setFrameShape(QFrame.Shape.VLine)
        self.line_18.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_120 = QLabel(self.frame_31)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setGeometry(QRect(21, 378, 24, 16))
        self.line_19 = QFrame(self.frame_31)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setGeometry(QRect(47, 197, 3, 16))
        self.line_19.setMinimumSize(QSize(0, 0))
        self.line_19.setMaximumSize(QSize(5, 16777215))
        self.line_19.setStyleSheet(u"background-color: rgb(248, 228, 92);")
        self.line_19.setFrameShape(QFrame.Shape.VLine)
        self.line_19.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_20 = QFrame(self.frame_31)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setGeometry(QRect(47, 40, 3, 159))
        self.line_20.setMinimumSize(QSize(0, 0))
        self.line_20.setMaximumSize(QSize(5, 16777215))
        self.line_20.setStyleSheet(u"background-color: rgb(224, 27, 36);")
        self.line_20.setFrameShape(QFrame.Shape.VLine)
        self.line_20.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_131 = QLabel(self.frame_31)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setGeometry(QRect(60, 10, 17, 17))
        self.label_121 = QLabel(self.frame_31)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setGeometry(QRect(21, 346, 24, 16))
        self.label_122 = QLabel(self.frame_31)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setGeometry(QRect(21, 314, 24, 16))
        self.label_123 = QLabel(self.frame_31)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setGeometry(QRect(21, 282, 24, 16))
        self.label_124 = QLabel(self.frame_31)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setGeometry(QRect(21, 251, 24, 16))
        self.label_125 = QLabel(self.frame_31)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setGeometry(QRect(21, 220, 24, 16))
        self.label_126 = QLabel(self.frame_31)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setGeometry(QRect(21, 188, 24, 16))
        self.label_127 = QLabel(self.frame_31)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setGeometry(QRect(21, 155, 24, 16))
        self.label_128 = QLabel(self.frame_31)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setGeometry(QRect(21, 124, 24, 16))
        self.label_129 = QLabel(self.frame_31)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setGeometry(QRect(14, 90, 31, 20))
        self.label_132 = QLabel(self.frame_31)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setGeometry(QRect(14, 60, 31, 20))
        self.label_133 = QLabel(self.frame_31)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setGeometry(QRect(14, 31, 31, 20))

        self.horizontalLayout_8.addWidget(self.frame_31)

        self.frame_30 = QFrame(self.page)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_30)

        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_11 = QHBoxLayout(self.page_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_35 = QFrame(self.page_2)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.lcdNumber_8 = QLCDNumber(self.frame_35)
        self.lcdNumber_8.setObjectName(u"lcdNumber_8")
        self.lcdNumber_8.setEnabled(False)
        self.lcdNumber_8.setGeometry(QRect(50, 430, 54, 23))
        sizePolicy.setHeightForWidth(self.lcdNumber_8.sizePolicy().hasHeightForWidth())
        self.lcdNumber_8.setSizePolicy(sizePolicy)
        self.lcdNumber_8.setMaximumSize(QSize(54, 16777215))
        self.lcdNumber_8.setLayoutDirection(Qt.LeftToRight)
        self.line_31 = QFrame(self.frame_35)
        self.line_31.setObjectName(u"line_31")
        self.line_31.setGeometry(QRect(47, 291, 3, 96))
        self.line_31.setMinimumSize(QSize(0, 0))
        self.line_31.setMaximumSize(QSize(5, 16777215))
        self.line_31.setStyleSheet(u"background-color: rgb(38, 162, 105);")
        self.line_31.setFrameShape(QFrame.Shape.VLine)
        self.line_31.setFrameShadow(QFrame.Shadow.Sunken)
        self.progressBar_8 = QProgressBar(self.frame_35)
        self.progressBar_8.setObjectName(u"progressBar_8")
        self.progressBar_8.setGeometry(QRect(50, 40, 61, 381))
        self.progressBar_8.setStyleSheet(u"")
        self.progressBar_8.setMaximum(120)
        self.progressBar_8.setValue(110)
        self.progressBar_8.setTextVisible(False)
        self.progressBar_8.setOrientation(Qt.Vertical)
        self.line_32 = QFrame(self.frame_35)
        self.line_32.setObjectName(u"line_32")
        self.line_32.setGeometry(QRect(45, 40, 2, 380))
        self.line_32.setFrameShape(QFrame.Shape.VLine)
        self.line_32.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_160 = QLabel(self.frame_35)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setGeometry(QRect(21, 378, 24, 16))
        self.line_33 = QFrame(self.frame_35)
        self.line_33.setObjectName(u"line_33")
        self.line_33.setGeometry(QRect(47, 261, 3, 33))
        self.line_33.setMinimumSize(QSize(0, 0))
        self.line_33.setMaximumSize(QSize(5, 16777215))
        self.line_33.setStyleSheet(u"background-color: rgb(248, 228, 92);")
        self.line_33.setFrameShape(QFrame.Shape.VLine)
        self.line_33.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_34 = QFrame(self.frame_35)
        self.line_34.setObjectName(u"line_34")
        self.line_34.setGeometry(QRect(47, 40, 3, 222))
        self.line_34.setMinimumSize(QSize(0, 0))
        self.line_34.setMaximumSize(QSize(5, 16777215))
        self.line_34.setStyleSheet(u"background-color: rgb(224, 27, 36);")
        self.line_34.setFrameShape(QFrame.Shape.VLine)
        self.line_34.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_161 = QLabel(self.frame_35)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setGeometry(QRect(60, 10, 17, 17))
        self.label_162 = QLabel(self.frame_35)
        self.label_162.setObjectName(u"label_162")
        self.label_162.setGeometry(QRect(21, 346, 24, 16))
        self.label_163 = QLabel(self.frame_35)
        self.label_163.setObjectName(u"label_163")
        self.label_163.setGeometry(QRect(21, 314, 24, 16))
        self.label_164 = QLabel(self.frame_35)
        self.label_164.setObjectName(u"label_164")
        self.label_164.setGeometry(QRect(21, 282, 24, 16))
        self.label_165 = QLabel(self.frame_35)
        self.label_165.setObjectName(u"label_165")
        self.label_165.setGeometry(QRect(21, 251, 24, 16))
        self.label_166 = QLabel(self.frame_35)
        self.label_166.setObjectName(u"label_166")
        self.label_166.setGeometry(QRect(21, 220, 24, 16))
        self.label_167 = QLabel(self.frame_35)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setGeometry(QRect(21, 188, 24, 16))
        self.label_168 = QLabel(self.frame_35)
        self.label_168.setObjectName(u"label_168")
        self.label_168.setGeometry(QRect(21, 155, 24, 16))
        self.label_169 = QLabel(self.frame_35)
        self.label_169.setObjectName(u"label_169")
        self.label_169.setGeometry(QRect(21, 124, 24, 16))
        self.label_170 = QLabel(self.frame_35)
        self.label_170.setObjectName(u"label_170")
        self.label_170.setGeometry(QRect(14, 90, 31, 20))
        self.label_171 = QLabel(self.frame_35)
        self.label_171.setObjectName(u"label_171")
        self.label_171.setGeometry(QRect(14, 60, 31, 20))
        self.label_172 = QLabel(self.frame_35)
        self.label_172.setObjectName(u"label_172")
        self.label_172.setGeometry(QRect(14, 31, 31, 20))
        self.line_39 = QFrame(self.frame_35)
        self.line_39.setObjectName(u"line_39")
        self.line_39.setGeometry(QRect(47, 402, 3, 17))
        self.line_39.setMinimumSize(QSize(0, 0))
        self.line_39.setMaximumSize(QSize(5, 16777215))
        self.line_39.setStyleSheet(u"background-color: rgb(224, 27, 36);")
        self.line_39.setFrameShape(QFrame.Shape.VLine)
        self.line_39.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_41 = QFrame(self.frame_35)
        self.line_41.setObjectName(u"line_41")
        self.line_41.setGeometry(QRect(47, 386, 3, 17))
        self.line_41.setMinimumSize(QSize(0, 0))
        self.line_41.setMaximumSize(QSize(5, 16777215))
        self.line_41.setStyleSheet(u"background-color: rgb(246, 211, 45);")
        self.line_41.setFrameShape(QFrame.Shape.VLine)
        self.line_41.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_11.addWidget(self.frame_35)

        self.frame_33 = QFrame(self.page_2)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.lcdNumber_6 = QLCDNumber(self.frame_33)
        self.lcdNumber_6.setObjectName(u"lcdNumber_6")
        self.lcdNumber_6.setEnabled(False)
        self.lcdNumber_6.setGeometry(QRect(50, 430, 54, 23))
        sizePolicy.setHeightForWidth(self.lcdNumber_6.sizePolicy().hasHeightForWidth())
        self.lcdNumber_6.setSizePolicy(sizePolicy)
        self.lcdNumber_6.setMaximumSize(QSize(54, 16777215))
        self.lcdNumber_6.setLayoutDirection(Qt.LeftToRight)
        self.line_23 = QFrame(self.frame_33)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setGeometry(QRect(47, 117, 3, 272))
        self.line_23.setMinimumSize(QSize(0, 0))
        self.line_23.setMaximumSize(QSize(5, 16777215))
        self.line_23.setStyleSheet(u"background-color: rgb(38, 162, 105);")
        self.line_23.setFrameShape(QFrame.Shape.VLine)
        self.line_23.setFrameShadow(QFrame.Shadow.Sunken)
        self.progressBar_6 = QProgressBar(self.frame_33)
        self.progressBar_6.setObjectName(u"progressBar_6")
        self.progressBar_6.setGeometry(QRect(50, 40, 61, 381))
        self.progressBar_6.setStyleSheet(u"")
        self.progressBar_6.setMaximum(120)
        self.progressBar_6.setValue(110)
        self.progressBar_6.setTextVisible(False)
        self.progressBar_6.setOrientation(Qt.Vertical)
        self.line_24 = QFrame(self.frame_33)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setGeometry(QRect(45, 40, 2, 380))
        self.line_24.setFrameShape(QFrame.Shape.VLine)
        self.line_24.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_134 = QLabel(self.frame_33)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setGeometry(QRect(21, 378, 24, 16))
        self.line_25 = QFrame(self.frame_33)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setGeometry(QRect(47, 87, 3, 31))
        self.line_25.setMinimumSize(QSize(0, 0))
        self.line_25.setMaximumSize(QSize(5, 16777215))
        self.line_25.setStyleSheet(u"background-color: rgb(248, 228, 92);")
        self.line_25.setFrameShape(QFrame.Shape.VLine)
        self.line_25.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_26 = QFrame(self.frame_33)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setGeometry(QRect(47, 40, 3, 47))
        self.line_26.setMinimumSize(QSize(0, 0))
        self.line_26.setMaximumSize(QSize(5, 16777215))
        self.line_26.setStyleSheet(u"background-color: rgb(224, 27, 36);")
        self.line_26.setFrameShape(QFrame.Shape.VLine)
        self.line_26.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_135 = QLabel(self.frame_33)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setGeometry(QRect(60, 10, 17, 17))
        self.label_136 = QLabel(self.frame_33)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setGeometry(QRect(21, 346, 24, 16))
        self.label_137 = QLabel(self.frame_33)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setGeometry(QRect(21, 314, 24, 16))
        self.label_138 = QLabel(self.frame_33)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setGeometry(QRect(21, 282, 24, 16))
        self.label_139 = QLabel(self.frame_33)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setGeometry(QRect(21, 251, 24, 16))
        self.label_140 = QLabel(self.frame_33)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setGeometry(QRect(21, 220, 24, 16))
        self.label_141 = QLabel(self.frame_33)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setGeometry(QRect(21, 188, 24, 16))
        self.label_142 = QLabel(self.frame_33)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setGeometry(QRect(21, 155, 24, 16))
        self.label_143 = QLabel(self.frame_33)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setGeometry(QRect(21, 124, 24, 16))
        self.label_144 = QLabel(self.frame_33)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setGeometry(QRect(14, 90, 31, 20))
        self.label_145 = QLabel(self.frame_33)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setGeometry(QRect(14, 60, 31, 20))
        self.label_146 = QLabel(self.frame_33)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setGeometry(QRect(14, 31, 31, 20))
        self.line_42 = QFrame(self.frame_33)
        self.line_42.setObjectName(u"line_42")
        self.line_42.setGeometry(QRect(47, 387, 3, 17))
        self.line_42.setMinimumSize(QSize(0, 0))
        self.line_42.setMaximumSize(QSize(5, 16777215))
        self.line_42.setStyleSheet(u"background-color: rgb(246, 211, 45);")
        self.line_42.setFrameShape(QFrame.Shape.VLine)
        self.line_42.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_43 = QFrame(self.frame_33)
        self.line_43.setObjectName(u"line_43")
        self.line_43.setGeometry(QRect(47, 404, 3, 16))
        self.line_43.setMinimumSize(QSize(0, 0))
        self.line_43.setMaximumSize(QSize(5, 16777215))
        self.line_43.setStyleSheet(u"background-color: rgb(224, 27, 36);")
        self.line_43.setFrameShape(QFrame.Shape.VLine)
        self.line_43.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_11.addWidget(self.frame_33)

        self.frame_36 = QFrame(self.page_2)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.lcdNumber_9 = QLCDNumber(self.frame_36)
        self.lcdNumber_9.setObjectName(u"lcdNumber_9")
        self.lcdNumber_9.setEnabled(False)
        self.lcdNumber_9.setGeometry(QRect(50, 430, 54, 23))
        sizePolicy.setHeightForWidth(self.lcdNumber_9.sizePolicy().hasHeightForWidth())
        self.lcdNumber_9.setSizePolicy(sizePolicy)
        self.lcdNumber_9.setMaximumSize(QSize(54, 16777215))
        self.lcdNumber_9.setLayoutDirection(Qt.LeftToRight)
        self.line_35 = QFrame(self.frame_36)
        self.line_35.setObjectName(u"line_35")
        self.line_35.setGeometry(QRect(47, 199, 3, 188))
        self.line_35.setMinimumSize(QSize(0, 0))
        self.line_35.setMaximumSize(QSize(5, 16777215))
        self.line_35.setStyleSheet(u"background-color: rgb(38, 162, 105);")
        self.line_35.setFrameShape(QFrame.Shape.VLine)
        self.line_35.setFrameShadow(QFrame.Shadow.Sunken)
        self.progressBar_9 = QProgressBar(self.frame_36)
        self.progressBar_9.setObjectName(u"progressBar_9")
        self.progressBar_9.setGeometry(QRect(50, 40, 61, 381))
        self.progressBar_9.setStyleSheet(u"")
        self.progressBar_9.setMaximum(120)
        self.progressBar_9.setValue(110)
        self.progressBar_9.setTextVisible(False)
        self.progressBar_9.setOrientation(Qt.Vertical)
        self.line_36 = QFrame(self.frame_36)
        self.line_36.setObjectName(u"line_36")
        self.line_36.setGeometry(QRect(45, 40, 2, 380))
        self.line_36.setFrameShape(QFrame.Shape.VLine)
        self.line_36.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_173 = QLabel(self.frame_36)
        self.label_173.setObjectName(u"label_173")
        self.label_173.setGeometry(QRect(21, 378, 24, 16))
        self.line_37 = QFrame(self.frame_36)
        self.line_37.setObjectName(u"line_37")
        self.line_37.setGeometry(QRect(47, 162, 3, 35))
        self.line_37.setMinimumSize(QSize(0, 0))
        self.line_37.setMaximumSize(QSize(5, 16777215))
        self.line_37.setStyleSheet(u"background-color: rgb(248, 228, 92);")
        self.line_37.setFrameShape(QFrame.Shape.VLine)
        self.line_37.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_38 = QFrame(self.frame_36)
        self.line_38.setObjectName(u"line_38")
        self.line_38.setGeometry(QRect(47, 40, 3, 124))
        self.line_38.setMinimumSize(QSize(0, 0))
        self.line_38.setMaximumSize(QSize(5, 16777215))
        self.line_38.setStyleSheet(u"background-color: rgb(224, 27, 36);")
        self.line_38.setFrameShape(QFrame.Shape.VLine)
        self.line_38.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_174 = QLabel(self.frame_36)
        self.label_174.setObjectName(u"label_174")
        self.label_174.setGeometry(QRect(60, 10, 17, 17))
        self.label_175 = QLabel(self.frame_36)
        self.label_175.setObjectName(u"label_175")
        self.label_175.setGeometry(QRect(21, 346, 24, 16))
        self.label_176 = QLabel(self.frame_36)
        self.label_176.setObjectName(u"label_176")
        self.label_176.setGeometry(QRect(21, 314, 24, 16))
        self.label_177 = QLabel(self.frame_36)
        self.label_177.setObjectName(u"label_177")
        self.label_177.setGeometry(QRect(21, 282, 24, 16))
        self.label_178 = QLabel(self.frame_36)
        self.label_178.setObjectName(u"label_178")
        self.label_178.setGeometry(QRect(21, 251, 24, 16))
        self.label_179 = QLabel(self.frame_36)
        self.label_179.setObjectName(u"label_179")
        self.label_179.setGeometry(QRect(21, 220, 24, 16))
        self.label_180 = QLabel(self.frame_36)
        self.label_180.setObjectName(u"label_180")
        self.label_180.setGeometry(QRect(21, 188, 24, 16))
        self.label_181 = QLabel(self.frame_36)
        self.label_181.setObjectName(u"label_181")
        self.label_181.setGeometry(QRect(21, 155, 24, 16))
        self.label_182 = QLabel(self.frame_36)
        self.label_182.setObjectName(u"label_182")
        self.label_182.setGeometry(QRect(21, 124, 24, 16))
        self.label_183 = QLabel(self.frame_36)
        self.label_183.setObjectName(u"label_183")
        self.label_183.setGeometry(QRect(14, 90, 31, 20))
        self.label_184 = QLabel(self.frame_36)
        self.label_184.setObjectName(u"label_184")
        self.label_184.setGeometry(QRect(14, 60, 31, 20))
        self.label_185 = QLabel(self.frame_36)
        self.label_185.setObjectName(u"label_185")
        self.label_185.setGeometry(QRect(14, 31, 31, 20))
        self.line_44 = QFrame(self.frame_36)
        self.line_44.setObjectName(u"line_44")
        self.line_44.setGeometry(QRect(47, 404, 3, 16))
        self.line_44.setMinimumSize(QSize(0, 0))
        self.line_44.setMaximumSize(QSize(5, 16777215))
        self.line_44.setStyleSheet(u"background-color: rgb(224, 27, 36);")
        self.line_44.setFrameShape(QFrame.Shape.VLine)
        self.line_44.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_45 = QFrame(self.frame_36)
        self.line_45.setObjectName(u"line_45")
        self.line_45.setGeometry(QRect(47, 387, 3, 17))
        self.line_45.setMinimumSize(QSize(0, 0))
        self.line_45.setMaximumSize(QSize(5, 16777215))
        self.line_45.setStyleSheet(u"background-color: rgb(246, 211, 45);")
        self.line_45.setFrameShape(QFrame.Shape.VLine)
        self.line_45.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_11.addWidget(self.frame_36)

        self.frame_39 = QFrame(self.page_2)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.lcdNumber_11 = QLCDNumber(self.frame_39)
        self.lcdNumber_11.setObjectName(u"lcdNumber_11")
        self.lcdNumber_11.setEnabled(False)
        self.lcdNumber_11.setGeometry(QRect(50, 430, 54, 23))
        sizePolicy.setHeightForWidth(self.lcdNumber_11.sizePolicy().hasHeightForWidth())
        self.lcdNumber_11.setSizePolicy(sizePolicy)
        self.lcdNumber_11.setMaximumSize(QSize(54, 16777215))
        self.lcdNumber_11.setLayoutDirection(Qt.LeftToRight)
        self.line_49 = QFrame(self.frame_39)
        self.line_49.setObjectName(u"line_49")
        self.line_49.setGeometry(QRect(47, 199, 3, 188))
        self.line_49.setMinimumSize(QSize(0, 0))
        self.line_49.setMaximumSize(QSize(5, 16777215))
        self.line_49.setStyleSheet(u"background-color: rgb(38, 162, 105);")
        self.line_49.setFrameShape(QFrame.Shape.VLine)
        self.line_49.setFrameShadow(QFrame.Shadow.Sunken)
        self.progressBar_11 = QProgressBar(self.frame_39)
        self.progressBar_11.setObjectName(u"progressBar_11")
        self.progressBar_11.setGeometry(QRect(50, 40, 61, 381))
        self.progressBar_11.setStyleSheet(u"")
        self.progressBar_11.setMaximum(120)
        self.progressBar_11.setValue(110)
        self.progressBar_11.setTextVisible(False)
        self.progressBar_11.setOrientation(Qt.Vertical)
        self.line_50 = QFrame(self.frame_39)
        self.line_50.setObjectName(u"line_50")
        self.line_50.setGeometry(QRect(45, 40, 2, 380))
        self.line_50.setFrameShape(QFrame.Shape.VLine)
        self.line_50.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_199 = QLabel(self.frame_39)
        self.label_199.setObjectName(u"label_199")
        self.label_199.setGeometry(QRect(21, 378, 24, 16))
        self.line_51 = QFrame(self.frame_39)
        self.line_51.setObjectName(u"line_51")
        self.line_51.setGeometry(QRect(47, 162, 3, 35))
        self.line_51.setMinimumSize(QSize(0, 0))
        self.line_51.setMaximumSize(QSize(5, 16777215))
        self.line_51.setStyleSheet(u"background-color: rgb(248, 228, 92);")
        self.line_51.setFrameShape(QFrame.Shape.VLine)
        self.line_51.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_52 = QFrame(self.frame_39)
        self.line_52.setObjectName(u"line_52")
        self.line_52.setGeometry(QRect(47, 40, 3, 124))
        self.line_52.setMinimumSize(QSize(0, 0))
        self.line_52.setMaximumSize(QSize(5, 16777215))
        self.line_52.setStyleSheet(u"background-color: rgb(224, 27, 36);")
        self.line_52.setFrameShape(QFrame.Shape.VLine)
        self.line_52.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_200 = QLabel(self.frame_39)
        self.label_200.setObjectName(u"label_200")
        self.label_200.setGeometry(QRect(60, 10, 17, 17))
        self.label_201 = QLabel(self.frame_39)
        self.label_201.setObjectName(u"label_201")
        self.label_201.setGeometry(QRect(21, 346, 24, 16))
        self.label_202 = QLabel(self.frame_39)
        self.label_202.setObjectName(u"label_202")
        self.label_202.setGeometry(QRect(21, 314, 24, 16))
        self.label_203 = QLabel(self.frame_39)
        self.label_203.setObjectName(u"label_203")
        self.label_203.setGeometry(QRect(21, 282, 24, 16))
        self.label_204 = QLabel(self.frame_39)
        self.label_204.setObjectName(u"label_204")
        self.label_204.setGeometry(QRect(21, 251, 24, 16))
        self.label_205 = QLabel(self.frame_39)
        self.label_205.setObjectName(u"label_205")
        self.label_205.setGeometry(QRect(21, 220, 24, 16))
        self.label_206 = QLabel(self.frame_39)
        self.label_206.setObjectName(u"label_206")
        self.label_206.setGeometry(QRect(21, 188, 24, 16))
        self.label_207 = QLabel(self.frame_39)
        self.label_207.setObjectName(u"label_207")
        self.label_207.setGeometry(QRect(21, 155, 24, 16))
        self.label_208 = QLabel(self.frame_39)
        self.label_208.setObjectName(u"label_208")
        self.label_208.setGeometry(QRect(21, 124, 24, 16))
        self.label_209 = QLabel(self.frame_39)
        self.label_209.setObjectName(u"label_209")
        self.label_209.setGeometry(QRect(14, 90, 31, 20))
        self.label_210 = QLabel(self.frame_39)
        self.label_210.setObjectName(u"label_210")
        self.label_210.setGeometry(QRect(14, 60, 31, 20))
        self.label_211 = QLabel(self.frame_39)
        self.label_211.setObjectName(u"label_211")
        self.label_211.setGeometry(QRect(14, 31, 31, 20))
        self.line_53 = QFrame(self.frame_39)
        self.line_53.setObjectName(u"line_53")
        self.line_53.setGeometry(QRect(47, 404, 3, 16))
        self.line_53.setMinimumSize(QSize(0, 0))
        self.line_53.setMaximumSize(QSize(5, 16777215))
        self.line_53.setStyleSheet(u"background-color: rgb(224, 27, 36);")
        self.line_53.setFrameShape(QFrame.Shape.VLine)
        self.line_53.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_54 = QFrame(self.frame_39)
        self.line_54.setObjectName(u"line_54")
        self.line_54.setGeometry(QRect(47, 387, 3, 17))
        self.line_54.setMinimumSize(QSize(0, 0))
        self.line_54.setMaximumSize(QSize(5, 16777215))
        self.line_54.setStyleSheet(u"background-color: rgb(246, 211, 45);")
        self.line_54.setFrameShape(QFrame.Shape.VLine)
        self.line_54.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_11.addWidget(self.frame_39)

        self.frame_37 = QFrame(self.page_2)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.lcdNumber_10 = QLCDNumber(self.frame_37)
        self.lcdNumber_10.setObjectName(u"lcdNumber_10")
        self.lcdNumber_10.setEnabled(False)
        self.lcdNumber_10.setGeometry(QRect(50, 430, 54, 23))
        sizePolicy.setHeightForWidth(self.lcdNumber_10.sizePolicy().hasHeightForWidth())
        self.lcdNumber_10.setSizePolicy(sizePolicy)
        self.lcdNumber_10.setMaximumSize(QSize(54, 16777215))
        self.lcdNumber_10.setLayoutDirection(Qt.LeftToRight)
        self.progressBar_10 = QProgressBar(self.frame_37)
        self.progressBar_10.setObjectName(u"progressBar_10")
        self.progressBar_10.setGeometry(QRect(50, 40, 61, 381))
        self.progressBar_10.setStyleSheet(u"")
        self.progressBar_10.setMaximum(100)
        self.progressBar_10.setValue(90)
        self.progressBar_10.setTextVisible(False)
        self.progressBar_10.setOrientation(Qt.Vertical)
        self.line_40 = QFrame(self.frame_37)
        self.line_40.setObjectName(u"line_40")
        self.line_40.setGeometry(QRect(45, 40, 2, 380))
        self.line_40.setFrameShape(QFrame.Shape.VLine)
        self.line_40.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_186 = QLabel(self.frame_37)
        self.label_186.setObjectName(u"label_186")
        self.label_186.setGeometry(QRect(21, 370, 24, 16))
        self.label_187 = QLabel(self.frame_37)
        self.label_187.setObjectName(u"label_187")
        self.label_187.setGeometry(QRect(60, 10, 17, 17))
        self.label_188 = QLabel(self.frame_37)
        self.label_188.setObjectName(u"label_188")
        self.label_188.setGeometry(QRect(21, 333, 24, 16))
        self.label_189 = QLabel(self.frame_37)
        self.label_189.setObjectName(u"label_189")
        self.label_189.setGeometry(QRect(21, 295, 24, 16))
        self.label_190 = QLabel(self.frame_37)
        self.label_190.setObjectName(u"label_190")
        self.label_190.setGeometry(QRect(21, 257, 24, 16))
        self.label_191 = QLabel(self.frame_37)
        self.label_191.setObjectName(u"label_191")
        self.label_191.setGeometry(QRect(21, 218, 24, 16))
        self.label_192 = QLabel(self.frame_37)
        self.label_192.setObjectName(u"label_192")
        self.label_192.setGeometry(QRect(21, 179, 24, 16))
        self.label_193 = QLabel(self.frame_37)
        self.label_193.setObjectName(u"label_193")
        self.label_193.setGeometry(QRect(21, 142, 24, 16))
        self.label_194 = QLabel(self.frame_37)
        self.label_194.setObjectName(u"label_194")
        self.label_194.setGeometry(QRect(21, 105, 24, 16))
        self.label_195 = QLabel(self.frame_37)
        self.label_195.setObjectName(u"label_195")
        self.label_195.setGeometry(QRect(21, 68, 24, 16))
        self.label_196 = QLabel(self.frame_37)
        self.label_196.setObjectName(u"label_196")
        self.label_196.setGeometry(QRect(14, 31, 31, 20))

        self.horizontalLayout_11.addWidget(self.frame_37)

        self.frame_38 = QFrame(self.page_2)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.frame_38)

        self.stackedWidget_2.addWidget(self.page_2)

        self.horizontalLayout_10.addWidget(self.stackedWidget_2)


        self.horizontalLayout_9.addWidget(self.frame_32)

        self.stackedWidget.addWidget(self.gmp)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(41, 488))
        self.frame.setMaximumSize(QSize(60, 481624))
        self.frame.setStyleSheet(u"background-color: rgb(156, 156, 156);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 189, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.toolButton_up = QToolButton(self.frame)
        self.toolButton_up.setObjectName(u"toolButton_up")
        self.toolButton_up.setStyleSheet(u"            QToolButton {\n"
"                background-color: #3498db;\n"
"                border: 2px solid #2980b9;\n"
"                border-radius: 10px;\n"
"                padding: 5px;\n"
"                color: white;\n"
"                font-size: 16px;\n"
"            }\n"
"            QToolButton:hover {\n"
"                background-color: #2980b9;\n"
"            }\n"
"            QToolButton:pressed {\n"
"                background-color: #1abc9c;\n"
"            }")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_up.setIcon(icon1)

        self.verticalLayout.addWidget(self.toolButton_up)

        self.toolButton_down = QToolButton(self.frame)
        self.toolButton_down.setObjectName(u"toolButton_down")
        self.toolButton_down.setStyleSheet(u"            QToolButton {\n"
"                background-color: #3498db;\n"
"                border: 2px solid #2980b9;\n"
"                border-radius: 10px;\n"
"                padding: 5px;\n"
"                color: white;\n"
"                font-size: 16px;\n"
"            }\n"
"            QToolButton:hover {\n"
"                background-color: #2980b9;\n"
"            }\n"
"            QToolButton:pressed {\n"
"                background-color: #1abc9c;\n"
"            }")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_down.setIcon(icon2)

        self.verticalLayout.addWidget(self.toolButton_down)

        self.verticalSpacer = QSpacerItem(20, 189, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.toolButton_down, self.toolButton_up)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Bank A", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Bank B", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Exhuast", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Bank A", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Bank B", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Air Coolder", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Befor Thermo", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"After Thermo", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Fresh Water", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.toolButton_lamptest.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Lamp Test", None))
        self.toolButton_lop.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"LOP", None))
        self.toolButton_mcr.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"MCR", None))
        self.toolButton_bridge.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Bridge", None))
        self.pushButton_control.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_control_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.toolButton_7.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_control_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.toolButton_8.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.toolButton_9.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_control_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.toolButton_10.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.toolButton_12.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.toolButton_14.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_control_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.toolButton_11.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.toolButton_13.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.toolButton_15.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"100 -", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"200 -", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"300 -", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"400 -", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"500 -", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"600 -", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"700 -", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"800 -", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"900 -", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"1000 -", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"1100 -", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"1200 -", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"1300 -", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"1400 -", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"1500 -", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"1600 -", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"1700 -", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"1800 -", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"1900 -", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"2000 -", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"2100 -", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"2200 -", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"100 -", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"200 -", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"300 -", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"400 -", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"500 -", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"600 -", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"700 -", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"800 -", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"900 -", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"1000 -", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"1100 -", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"1200 -", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"100 -", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"200 -", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"300 -", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"400 -", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"500 -", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"600 -", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"700 -", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"800 -", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"900 -", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"1000 -", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"1100 -", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"1200 -", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"10 -", None))
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"20 -", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"30 -", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"40 -", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"50 -", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"60 -", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"70 -", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"80 -", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"90 -", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"100 -", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"110 -", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"120 -", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"10 -", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"20 -", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"30 -", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"40 -", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"50 -", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"60 -", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"70 -", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"80 -", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"90 -", None))
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"100 -", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"110 -", None))
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"120 -", None))
        self.label_160.setText(QCoreApplication.translate("MainWindow", u"10 -", None))
        self.label_161.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_162.setText(QCoreApplication.translate("MainWindow", u"20 -", None))
        self.label_163.setText(QCoreApplication.translate("MainWindow", u"30 -", None))
        self.label_164.setText(QCoreApplication.translate("MainWindow", u"40 -", None))
        self.label_165.setText(QCoreApplication.translate("MainWindow", u"50 -", None))
        self.label_166.setText(QCoreApplication.translate("MainWindow", u"60 -", None))
        self.label_167.setText(QCoreApplication.translate("MainWindow", u"70 -", None))
        self.label_168.setText(QCoreApplication.translate("MainWindow", u"80 -", None))
        self.label_169.setText(QCoreApplication.translate("MainWindow", u"90 -", None))
        self.label_170.setText(QCoreApplication.translate("MainWindow", u"100 -", None))
        self.label_171.setText(QCoreApplication.translate("MainWindow", u"110 -", None))
        self.label_172.setText(QCoreApplication.translate("MainWindow", u"120 -", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"10 -", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"20 -", None))
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"30 -", None))
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"40 -", None))
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"50 -", None))
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"60 -", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"70 -", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"80 -", None))
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"90 -", None))
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"100 -", None))
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"110 -", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"120 -", None))
        self.label_173.setText(QCoreApplication.translate("MainWindow", u"10 -", None))
        self.label_174.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_175.setText(QCoreApplication.translate("MainWindow", u"20 -", None))
        self.label_176.setText(QCoreApplication.translate("MainWindow", u"30 -", None))
        self.label_177.setText(QCoreApplication.translate("MainWindow", u"40 -", None))
        self.label_178.setText(QCoreApplication.translate("MainWindow", u"50 -", None))
        self.label_179.setText(QCoreApplication.translate("MainWindow", u"60 -", None))
        self.label_180.setText(QCoreApplication.translate("MainWindow", u"70 -", None))
        self.label_181.setText(QCoreApplication.translate("MainWindow", u"80 -", None))
        self.label_182.setText(QCoreApplication.translate("MainWindow", u"90 -", None))
        self.label_183.setText(QCoreApplication.translate("MainWindow", u"100 -", None))
        self.label_184.setText(QCoreApplication.translate("MainWindow", u"110 -", None))
        self.label_185.setText(QCoreApplication.translate("MainWindow", u"120 -", None))
        self.label_199.setText(QCoreApplication.translate("MainWindow", u"10 -", None))
        self.label_200.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_201.setText(QCoreApplication.translate("MainWindow", u"20 -", None))
        self.label_202.setText(QCoreApplication.translate("MainWindow", u"30 -", None))
        self.label_203.setText(QCoreApplication.translate("MainWindow", u"40 -", None))
        self.label_204.setText(QCoreApplication.translate("MainWindow", u"50 -", None))
        self.label_205.setText(QCoreApplication.translate("MainWindow", u"60 -", None))
        self.label_206.setText(QCoreApplication.translate("MainWindow", u"70 -", None))
        self.label_207.setText(QCoreApplication.translate("MainWindow", u"80 -", None))
        self.label_208.setText(QCoreApplication.translate("MainWindow", u"90 -", None))
        self.label_209.setText(QCoreApplication.translate("MainWindow", u"100 -", None))
        self.label_210.setText(QCoreApplication.translate("MainWindow", u"110 -", None))
        self.label_211.setText(QCoreApplication.translate("MainWindow", u"120 -", None))
        self.label_186.setText(QCoreApplication.translate("MainWindow", u"10 -", None))
        self.label_187.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_188.setText(QCoreApplication.translate("MainWindow", u"20 -", None))
        self.label_189.setText(QCoreApplication.translate("MainWindow", u"30 -", None))
        self.label_190.setText(QCoreApplication.translate("MainWindow", u"40 -", None))
        self.label_191.setText(QCoreApplication.translate("MainWindow", u"50 -", None))
        self.label_192.setText(QCoreApplication.translate("MainWindow", u"60 -", None))
        self.label_193.setText(QCoreApplication.translate("MainWindow", u"70 -", None))
        self.label_194.setText(QCoreApplication.translate("MainWindow", u"80 -", None))
        self.label_195.setText(QCoreApplication.translate("MainWindow", u"90 -", None))
        self.label_196.setText(QCoreApplication.translate("MainWindow", u"100 -", None))
        self.toolButton_up.setText(QCoreApplication.translate("MainWindow", u"up", None))
        self.toolButton_down.setText(QCoreApplication.translate("MainWindow", u"down", None))
    # retranslateUi

