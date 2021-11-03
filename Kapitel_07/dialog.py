from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dialog Beispiele")
        layout = QVBoxLayout()

        button1 = QPushButton("QMessageBox: Information")
        button2 = QPushButton("QMessageBox: About")
        button3 = QPushButton("3")
        button4 = QPushButton("4")
        button5 = QPushButton("5")

        button1.clicked.connect(self.button1_clicked)
        button2.clicked.connect(self.button2_clicked)
        button3.clicked.connect(self.button3_clicked)
        button4.clicked.connect(self.button4_clicked)
        button5.clicked.connect(self.button5_clicked)


        style = """QPushButton { font-size: 48px; background-color: #00AA00; }
                   QPushButton:pressed {font-size: 48px; background-color: #AA0000}"""
        button1.setStyleSheet(style)
        button2.setStyleSheet(style)
        button3.setStyleSheet(style)
        button4.setStyleSheet(style)
        button5.setStyleSheet(style)

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(button5)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()

    def button1_clicked(self):
        QMessageBox.information(self, "Titel", "<h1>Hello World</h1>Python macht Spass<br/>Dies ist eine Zeile")
    
    def button2_clicked(self):
        QMessageBox.about(self, "Titel", "Dieses Programm wurde mit PyQT5 erstellt")

    def button3_clicked(self):
        pass
    def button4_clicked(self):
        pass
    def button5_clicked(self):
        pass

app = QApplication([])
f = Fenster()
app.exec()