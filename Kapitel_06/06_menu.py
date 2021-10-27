from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menu")

        menubar = self.menuBar()

        filemenu = menubar.addMenu("File")
        editmenu = menubar.addMenu("Edit")
        viewmenu = menubar.addMenu("View")

        open = QAction("Öffnen", self)
        save = QAction("Speichern", self)
        quit = QAction("Exit", self)

        quit.setMenuRole(QAction.QuitRole)

        filemenu.addAction(open)
        filemenu.addAction(save)
        filemenu.addSeparator()
        filemenu.addAction(quit)

        open.triggered.connect(self.doOpen)
        quit.triggered.connect(self.doQuit)

        self.show()

    def doOpen(self):
        print("Datei öffnen!!!")

    def doQuit(self):
        exit(0)

app = QApplication([])
fenster = Window()
fenster.raise_()
app.exec()