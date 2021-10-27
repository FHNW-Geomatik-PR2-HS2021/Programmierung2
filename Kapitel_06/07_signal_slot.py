from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Grid Layout")

        layout = QVBoxLayout()

        # Widgets erstellen

        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        checkbox = QCheckBox("Hello World")
        self.name = QLineEdit()


        # Widgets dem Layout hinzufügen

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(checkbox)
        layout.addWidget(self.name)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)
        self.show()

        ########

        button1.clicked.connect(self.Knopf1)
        button2.clicked.connect(self.Knopf2)
        checkbox.stateChanged.connect(self.MyCheckBox)

    def MyCheckBox(self, state):
        if state == Qt.CheckState.Checked:
            print("Checkbox ist gewählt!")
        elif state == Qt.CheckState.Unchecked:
            print("Checkbox ist nicht gewählt") 

    def Knopf1(self):
        print("Line Edit hat den Wert: " + self.name.text())

    def Knopf2(self):
        self.name.setText("Hello World")


app = QApplication([])
fenster = Window()
fenster.raise_()
app.exec()