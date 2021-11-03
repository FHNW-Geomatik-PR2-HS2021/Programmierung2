from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dialog Beispiele")
        layout = QVBoxLayout()

        button1 = QPushButton("QMessageBox: Information")
        button2 = QPushButton("QMessageBox: About")
        button3 = QPushButton("QMessageBox: Warning")
        button4 = QPushButton("QMessageBox: Critical")
        button5 = QPushButton("QMessageBox: Question")

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
        QMessageBox.warning(self, "Titel", "Disk ist voll, das File konnte nicht geschrieben werden")

    def button4_clicked(self):
        QMessageBox.critical(self, "Stop", "Das Konfigurations-File konnte nicht geladen werden. Das Programm muss beendet werden.")
        self.close()

    def button5_clicked(self):
        antwort = QMessageBox.question(self, "Frage", "Ist Python eine gute Spache?", QMessageBox.Yes, QMessageBox.No)

        if antwort == QMessageBox.Yes:
            QMessageBox.information(self, "Python", "Ja, das ist klar")
        else:
            QMessageBox.critical(self, "Buuuuuuh!!!!", "Ok, das Programm wird beendet")
            self.close()

app = QApplication([])
f = Fenster()
app.exec()