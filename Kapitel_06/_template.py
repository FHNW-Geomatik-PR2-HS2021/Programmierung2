from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Grid Layout")

        # layout = QGridLayout()

        # Widgets erstellen

        # Widgets dem Layout hinzufügen

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)
        self.show()


app = QApplication([])
fenster = Window()
fenster.raise_()
app.exec()