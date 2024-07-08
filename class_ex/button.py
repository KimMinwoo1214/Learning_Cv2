from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kairos")
        self.button_state = False
        
        button = QPushButton("Push")
        button.clicked.connect(self.button_is_clicked)
        self.setCentralWidget(button)
        self.show()
    
    def button_is_clicked(self):
        self.button_state = not self.button_state
        self.setStyleSheet("color: green;" 
                           "border-style: solid;"
                           "background-color: #7FFFD4")
        if self.button_state:
            self.setStyleSheet("color: red;"
                            "border-style: solid;"
                             "border-width: 2px;"
                             "border-color: #FA8072;"
                             "border-radius: 3px")
            print("Button is clicked")
            
        
app = QApplication(sys.argv)
win = MainWindow()

app.exec()

