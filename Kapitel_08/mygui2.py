from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *

class MeinFenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Kapitel_08/gui.ui", self)

        self.meinSuperButton.clicked.connect(self.button_click)

        self.show()

    def button_click(self):
        print("Hello")

app = QApplication([])
fenster = MeinFenster()
app.exec()