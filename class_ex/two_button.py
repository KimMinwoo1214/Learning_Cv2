from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QWidget
import sys
import random

candidate = {"KMH": 0, "KDH": 0, "CGH": 0, "SSH": 0, "KMW": 0}

class MainWindow(QMainWindow):
    def __init__(self):  
        super().__init__()
        self.button_state = False
        self.setWindowTitle("Kairos")

        container = QWidget()
        self.setCentralWidget(container)

        v_layout = QVBoxLayout()  
        container.setLayout(v_layout)      
        
        button1 = QPushButton("Vote")
        button1.clicked.connect(self.button1_is_clicked)
        button2 = QPushButton("Now Result")
        button2.clicked.connect(self.button2_is_clicked)

        v_layout.addWidget(button1)
        v_layout.addWidget(button2)

        self.show()

    def button1_is_clicked(self):
        result = random.choice(list(candidate.keys()))
        candidate[result] += 1
        print(result)
        
    def button2_is_clicked(self):
        print(f"Now, {candidate}")

app = QApplication(sys.argv)
win = MainWindow() 
app.exec()