from PyQt5.QtWidgets import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        #self.setMinimumWidth(1280)
        #self.setMinimumHeight(768)
        self.setWindowTitle("Dies ist ein Fenster")
        
        layout = QHBoxLayout()

        button1 = QPushButton("Hello World")
        button2 = QPushButton("Ok")
        button3 = QPushButton("Abbrechen")

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)

        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)
        self.show()


app = QApplication([])
fenster = Fenster()
fenster.raise_()
app.exec()