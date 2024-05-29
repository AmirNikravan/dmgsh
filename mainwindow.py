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
