# This Python file uses the following encoding: utf-8
import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
# os.system("pyside6-uic form.ui -o ui_form.py")

from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.toolButton_up.clicked.connect(lambda:self.change_main_page('up'))
        self.ui.toolButton_down.clicked.connect(lambda:self.change_main_page('down'))
        self.ui.toolButton_p1f.clicked.connect(lambda:self.change_bar_page('forward'))
        self.ui.toolButton_p1b.clicked.connect(lambda:self.change_bar_page('before'))
        self.ui.toolButton_p2b.clicked.connect(lambda :self.change_bar_page('before'))
        self.ui.toolButton_p2f.clicked.connect(lambda:self.change_bar_page('forward'))
        self.ui.toolButton_p3b.clicked.connect(lambda:self.change_bar_page('before'))
        self.ui.toolButton_p3f.clicked.connect(lambda:self.change_bar_page('forward'))

    def change_bar_page(self,str):
        max_index = self.ui.stackedWidget_bar.count()-1
        min_index = 0
        current = self.ui.stackedWidget_bar.currentIndex()
        if str == 'forward':
            if current == max_index:
                self.ui.stackedWidget_bar.setCurrentIndex(min_index)
            else:
                self.ui.stackedWidget_bar.setCurrentIndex(current+1)
        elif str == 'before':
            if current == min_index:
                self.ui.stackedWidget_bar.setCurrentIndex(max_index)
            else:
                self.ui.stackedWidget_bar.setCurrentIndex(current -1 )

    def change_main_page(self,str):
        max_index = self.ui.stackedWidget.count()-1
        min_index = 0
        current = self.ui.stackedWidget.currentIndex()
        if str == 'up':
            if current == max_index:
                self.ui.stackedWidget.setCurrentIndex(min_index)
            else:
                self.ui.stackedWidget.setCurrentIndex(current+1)
        elif str == 'down':
            if current == min_index:
                self.ui.stackedWidget.setCurrentIndex(max_index)
            else:
                self.ui.stackedWidget.setCurrentIndex(current-1)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
