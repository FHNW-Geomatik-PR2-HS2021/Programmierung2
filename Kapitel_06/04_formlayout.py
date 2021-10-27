from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Grid Layout")

        layout = QFormLayout()

        # Widgets erstellen
        name = QLineEdit()
        email = QLineEdit()
        alter = QSpinBox()
        button = QPushButton("Hello World")
        
        # Widgets dem Layout hinzufügen
        layout.addRow("Name:", name)
        layout.addRow("E-Mail:", email)
        layout.addRow("Alter:", alter)
        layout.addRow(button)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)
        self.show()


app = QApplication([])
fenster = Window()
fenster.raise_()
app.exec()