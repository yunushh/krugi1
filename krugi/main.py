import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt6 import QtGui
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtCore import Qt
import random, copy


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.title = "PyQt6 круги"
        self.draw = None
        self.InitWindow()

    def InitWindow(self):
        self.pushButton.clicked.connect(self.run)
        self.show()

    def run(self):
        self.draw = True
        self.update()

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(255, 255, 0))
            rad = random.randrange(100, 255)
            x = random.randrange(455)
            y = random.randrange(455)
            qp.drawEllipse(x, y, rad, rad)
            qp.end()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())


