import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton

class VerticalLineDemo(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Vertical Line with Different Background Colors')
        
        # Create a vertical layout
        layout = QVBoxLayout()
        
        # Create a horizontal layout for line and widgets
        h_layout = QHBoxLayout()
        
        # Create a left and a right line
        self.leftLine = QLabel(self)
        self.leftLine.setStyleSheet("border-left: 2px solid lightgray;")

        self.rightLine = QLabel(self)
        self.rightLine.setStyleSheet("border-left: 2px solid blue;")

        # Add the left and right lines to the horizontal layout
        h_layout.addWidget(self.leftLine)
        h_layout.addWidget(self.rightLine)
        
        # Add the horizontal layout to the main layout
        layout.addLayout(h_layout)
        
        # Create a button to change the background color of the right side
        self.changeColorButton = QPushButton('Change Right Side Color', self)
        self.changeColorButton.clicked.connect(self.changeRightColor)
        layout.addWidget(self.changeColorButton)
        
        # Set the layout for the main window
        self.setLayout(layout)
    
    def changeRightColor(self):
        # Change the background color of the right side line
        self.rightLine.setStyleSheet("border-left: 2px solid green;")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VerticalLineDemo()
    ex.show()
    sys.exit(app.exec_())
