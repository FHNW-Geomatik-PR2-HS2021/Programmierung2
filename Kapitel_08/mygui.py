from PyQt5.QtWidgets import *
from PyQt5.uic import *


def hello():
    print("Button wurde geklicked!")
    fenster.lineEdit.setText("Ok!!!")

app = QApplication([])

fenster = loadUi("Kapitel_08/gui.ui")
fenster.show()


fenster.meinSuperButton.clicked.connect(hello)

app.exec()