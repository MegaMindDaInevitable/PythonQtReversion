"""
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys 

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Our first MainWindow app!!!")


button = QPushButton()
button.setText("Press Me")

window.setCentralWidget(button)

window.show()
app.exec()

"""
"""
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Holder App")
        button = QPushButton("Press Me!")

        self.setCentralWidget(button)

app = QApplication(sys.argv)

window = ButtonHolder()

window.show()
app.exec()
"""
"""

import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from buttonholderclass import ButtonHolder

app = QApplication(sys.argv)

window = ButtonHolder()

window.show()
app.exec()
"""

#version 3 handling Slider values

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider

def respond_to_slider(data):
    print("Slider Moved to :",data)


app = QApplication()

slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)


slider.valueChanged.connect(respond_to_slider)

slider.show()
app.exec()