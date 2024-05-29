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
    QLabel, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QToolButton,
    QVBoxLayout, QWidget)

from AnalogGaugeWidget import AnalogGaugeWidget
import rc_rsc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(802, 550)
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
        self.stackedWidget_2 = QStackedWidget(self.gmp)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(-20, 20, 741, 501))
        self.stackedWidget_2.setStyleSheet(u"background-color: rgb(198, 70, 0);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.progressBar = QProgressBar(self.page)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(100, 230, 131, 31))
        self.progressBar.setValue(24)
        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget_2.addWidget(self.page_2)
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
        self.toolButton_up.setText(QCoreApplication.translate("MainWindow", u"up", None))
        self.toolButton_down.setText(QCoreApplication.translate("MainWindow", u"down", None))
    # retranslateUi

