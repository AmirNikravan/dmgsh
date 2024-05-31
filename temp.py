import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar, QPushButton

class ProgressBarDemo(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Progress Bar Color Change Demo')
        
        # Create a vertical layout
        layout = QVBoxLayout(self)
        
        # Create a progress bar
        self.progressBar = QProgressBar(self)
        self.progressBar.setValue(50)
        
        # Set initial style for the progress bar
        self.setProgressBarColor('blue')
        
        # Create a button to change the progress bar color
        self.changeColorButton = QPushButton('Change Color to Green', self)
        self.changeColorButton.clicked.connect(self.changeColor)
        
        # Add widgets to the layout
        layout.addWidget(self.progressBar)
        layout.addWidget(self.changeColorButton)
        
        # Set the layout for the main window
        self.setLayout(layout)
    
    def setProgressBarColor(self, color):
        # Set the stylesheet for the progress bar
        self.progressBar.setStyleSheet(f"""
            QProgressBar::chunk {{
                background-color: {color};
            }}
        """)
    
    def changeColor(self):
        # Change the color of the progress bar to green
        self.setProgressBarColor('green')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ProgressBarDemo()
    demo.show()
    sys.exit(app.exec_())
