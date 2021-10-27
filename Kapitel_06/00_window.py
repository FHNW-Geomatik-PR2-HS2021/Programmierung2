from PyQt5.QtWidgets import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(20,120,640,480)
        #self.setMinimumWidth(1280)
        #self.setMinimumHeight(768)
        self.setWindowTitle("Dies ist ein Fenster")
        self.show()


app = QApplication([])
fenster = Fenster()
fenster.raise_()
app.exec()