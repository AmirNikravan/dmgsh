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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QSizePolicy, QStackedWidget, QToolButton,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(782, 499)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(290, 160, 161, 91))
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(253, 50, 111, 191))
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_4 = QLabel(self.page_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(303, 80, 141, 131))
        self.stackedWidget.addWidget(self.page_4)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 150, 121, 101))
        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(60, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.toolButton_up = QToolButton(self.frame)
        self.toolButton_up.setObjectName(u"toolButton_up")
        self.toolButton_up.setGeometry(QRect(9, 173, 41, 31))
        self.toolButton_down = QToolButton(self.frame)
        self.toolButton_down.setObjectName(u"toolButton_down")
        self.toolButton_down.setGeometry(QRect(11, 210, 41, 31))

        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"fghjfghk678768", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"hjp9p90b", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"455o[6890-84856u", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"adfadsfaf", None))
        self.toolButton_up.setText(QCoreApplication.translate("MainWindow", u"up", None))
        self.toolButton_down.setText(QCoreApplication.translate("MainWindow", u"down", None))
    # retranslateUi

