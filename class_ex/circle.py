import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QDial, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 슬라이더와 다이얼 설정
        self.red_slider = QSlider(Qt.Horizontal, self)
        self.red_slider.move(30, 30)
        self.red_slider.setRange(0, 255)

        self.green_slider = QSlider(Qt.Horizontal, self)
        self.green_slider.move(30, 70)
        self.green_slider.setRange(0, 255)

        self.blue_slider = QSlider(Qt.Horizontal, self)
        self.blue_slider.move(30, 110)
        self.blue_slider.setRange(0, 255)

        self.dial = QDial(self)
        self.dial.move(250, 30)
        self.dial.setRange(0, 255)
        self.dial.setNotchesVisible(True)

        # 버튼 설정
        btn = QPushButton('Default', self)
        btn.move(150, 160)

        # 라벨 설정
        self.label = QLabel('R: 0, G: 0, B: 0', self)
        self.label.move(30, 150)
        self.label.resize(200, 20)

        # 슬라이더와 다이얼 값 변경 시 연결
        self.red_slider.valueChanged.connect(self.update_color)
        self.green_slider.valueChanged.connect(self.update_color)
        self.blue_slider.valueChanged.connect(self.update_color)
        self.dial.valueChanged.connect(self.update_dial_color)

        # 버튼 클릭 시 초기화
        btn.clicked.connect(self.reset_values)

        self.setWindowTitle('Color Adjuster')
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def update_color(self):
        red = self.red_slider.value()
        green = self.green_slider.value()
        blue = self.blue_slider.value()

        color = QColor(red, green, blue)
        self.setStyleSheet(f'QWidget {{ background-color: {color.name()} }}')
        self.label.setText(f'R: {red}, G: {green}, B: {blue}')

    def update_dial_color(self):
        value = self.dial.value()
        self.red_slider.setValue(value)
        self.green_slider.setValue(value)
        self.blue_slider.setValue(value)
        self.update_color()

    def reset_values(self):
        self.red_slider.setValue(0)
        self.green_slider.setValue(0)
        self.blue_slider.setValue(0)
        self.dial.setValue(0)
        self.setStyleSheet('QWidget { background-color: white }')
        self.label.setText('R: 0, G: 0, B: 0')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
