from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *

class Umrechner(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Kapitel_08/gui3.ui", self)

        self.createConnects()
        self.show()

    # -------------------------------------------------------------------------

    def createConnects(self):
        #self.umrechnen.clicked.connect(self.buttonUmrechnen)
        self.euroLineEdit.textChanged.connect(self.euroEdit)

    # -------------------------------------------------------------------------

    def euroEdit(self, text):
        self.buttonUmrechnen()

    def buttonUmrechnen(self):
        euro = self.euroLineEdit.text()
        try:
            wert = float(euro)
            wert_chf = wert * 1.06
            self.frankenLineEdit.setText(str(wert_chf))
        except:
            self.frankenLineEdit.setText("ungültiger Wert")

app = QApplication([])
fenster = Umrechner()
app.exec()