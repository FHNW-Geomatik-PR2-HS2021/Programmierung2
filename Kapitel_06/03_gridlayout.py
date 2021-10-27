from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Grid Layout")

        layout = QGridLayout()

        nameLabel = QLabel("Name:")
        nameLine = QLineEdit()
        addressLabel = QLabel("Addresse:")
        addressLine = QTextEdit()

        layout.addWidget(nameLabel, 0, 0)
        layout.addWidget(nameLine, 0, 1)
        layout.addWidget(addressLabel, 1, 0, Qt.AlignTop)
        layout.addWidget(addressLine, 1, 1)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)
        self.show()


app = QApplication([])
fenster = Window()
fenster.raise_()
app.exec()