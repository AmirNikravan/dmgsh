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
    QLabel, QMainWindow, QSizePolicy, QSpacerItem,
    QStackedWidget, QToolButton, QVBoxLayout, QWidget)

from AnalogGaugeWidget import AnalogGaugeWidget
import rc_rsc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(782, 506)
        MainWindow.setStyleSheet(u"background-color: rgb(39, 51, 109);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(176, 212, 218);")
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
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(253, 50, 111, 191))
        self.stackedWidget.addWidget(self.page_3)

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
        icon = QIcon()
        icon.addFile(u":/icons/icons/up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_up.setIcon(icon)

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
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_down.setIcon(icon1)

        self.verticalLayout.addWidget(self.toolButton_down)

        self.verticalSpacer = QSpacerItem(20, 189, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.toolButton_down, self.toolButton_up)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


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
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"lop", None))
        self.toolButton_up.setText(QCoreApplication.translate("MainWindow", u"up", None))
        self.toolButton_down.setText(QCoreApplication.translate("MainWindow", u"down", None))
    # retranslateUi

