from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

style = """* {font-size: 48px;}
                    QPushButton { font-size: 48px; background-color: #00AA00; }
                   QPushButton:pressed {font-size: 48px; background-color: #AA0000}"""

class Dialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        label = QLabel("Dies ist ein Label")
        button = QPushButton("Ok")
        layout = QVBoxLayout()

        layout.addWidget(label)
        layout.addWidget(button)
        self.setLayout(layout)
        self.setStyleSheet(style)
        button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.close()
#---------------------------------------------------------------------------------------

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dialog Beispiele")
        layout = QVBoxLayout()

        buttons = []

        buttons.append(QPushButton("QMessageBox: Information"))
        buttons.append(QPushButton("QMessageBox: About"))
        buttons.append(QPushButton("QMessageBox: Warning"))
        buttons.append(QPushButton("QMessageBox: Critical"))
        buttons.append(QPushButton("QMessageBox: Question"))
        buttons.append(QPushButton("Open Dialog"))
        buttons.append(QPushButton("Open multiple files Dialog"))
        buttons.append(QPushButton("Save Dialog"))
        buttons.append(QPushButton("Input Dialog"))
        buttons.append(QPushButton("QColorDialog"))
        buttons.append(QPushButton("QFontDialog"))
        buttons.append(QPushButton("Custom Dialog"))

        # Mit getattr kann die Mathode in der Klasse direkt gesucht werden (Advanced)
        # Man könnte sich auch die untere for-Schleife sparen und alles in eine for-Schleife packen
        for i in range(0,len(buttons)):
            function = getattr(self,f"button{i+1}_clicked")
            buttons[i].clicked.connect(function)

       

        for button in buttons:
            button.setStyleSheet(style)
            layout.addWidget(button)
       
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

    def button6_clicked(self):
        dateifilter = "Textdatei (*.txt *.ttt);;Python File (*.py)"

        path = QStandardPaths.standardLocations(QStandardPaths.DesktopLocation)[0]

        filename, filter = QFileDialog.getOpenFileName(self, "Datei öffnen", path, dateifilter)

        if filename != "":
            QMessageBox.information(self, "File", f"<h1>{filename}</h1><h2>{filter}</h2>")
        else:
            QMessageBox.warning(self, "Kein File", "Es wurde kein File ausgewählt")
        

    def button7_clicked(self):
        filenamen, filter = QFileDialog.getOpenFileNames(self, "Dateien öffnen", "", "Text (*.txt)")
        print(filenamen)

    def button8_clicked(self):
        filename, filter = QFileDialog.getSaveFileName(self, "Speichern", "", "Python (*.py)")
        print(filename, filter)

    def button9_clicked(self):
        wert, ok = QInputDialog.getItem(self, "Auswahl", "Welches Land ist schöner ?", ["Schweiz", "Deutschland", "Österreich"], 1, True)

        wert, ok = QInputDialog.getDouble(self, "Titel", "Text")

        wert, ok = QInputDialog.getInt(self, "Titel", "Text", 20, 10, 30)
        if ok:
            print(wert)

    def button10_clicked(self):
        farbe = QColorDialog.getColor(initial=QColor(0,0,255))
        print(farbe.red(), farbe.green(), farbe.blue())

    def button11_clicked(self):
        font = QFontDialog.getFont()

    def button12_clicked(self):
        d = Dialog(self)
        d.exec()

app = QApplication([])
f = Fenster()
app.exec()