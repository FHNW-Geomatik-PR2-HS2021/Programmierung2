"""
Ausgehend von Andrian's Lösung mit ein Paar Modifikationen...
"""


from PyQt5.QtCore import *
from PyQt5.QtGui import QDesktopServices, QIntValidator
from PyQt5.QtWidgets import *
import csv
from collections import namedtuple

DELIMITER = ","
MAPS_URL = "https://www.google.ch/maps/place/{address}"

Entry = namedtuple("Entry", [
    'name', 
    'vorname', 
    'geburtstag', 
    'adresse',
    'postleitzahl',
    'ort',
    'land'
    ])

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        # Variabeln Initilaisieren
        self.datalist =[]

        #Windowtitle
        self.setWindowTitle("Adress Form")
        self.setMinimumWidth(400)

        # Menuebar ------------------------------------------------------------
        menuebar = self.menuBar()
        filemenue = menuebar.addMenu("File")
        viewmenue = menuebar.addMenu("View")
        editmenue = menuebar.addMenu("Edit")

        # File -----
        # Save
        menubutton_save = QAction("Save",self)
        menubutton_save.triggered.connect(self.exporttocsv)
        filemenue.addAction(menubutton_save)
        # Exit
        menubutton_exit = QAction("Quit",self)
        menubutton_exit.triggered.connect(self.close_program)       
        filemenue.addAction(menubutton_exit)

        # View ------
        # Karte anzeigen
        menubutton_showmap = QAction("Karte anzeigen",self)
        menubutton_showmap.triggered.connect(self.showmap)
        viewmenue.addAction(menubutton_showmap)

        # Edit ------
        # Clear
        editbutton_clear = QAction("Clear",self)
        editbutton_clear.triggered.connect(self.clearform)
        editmenue.addAction(editbutton_clear)

        #Layout
        layout = QFormLayout()
        layout2 = QVBoxLayout()

        # Widgets erstellen ---------------------------------------------------
        self.name = QLineEdit()
        self.vorname = QLineEdit()
        self.geburtstag = QDateEdit()
        self.geburtstag.setDisplayFormat("dd.MM.yyyy")
        self.adresse = QLineEdit()
        self.postleitzahl = QLineEdit()
        self.ort = QLineEdit()
        self.land = QComboBox()
        self.button_showmap = QPushButton("Auf Karte anzeigen")
        self.button_laden = QPushButton("Laden")
        self.button_save = QPushButton("Save")
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 1)
        self.text = QLabel("Datensatz laden:")


        # Input
        self.landlist = ["--- Auswahl ---","Schweiz", "Deutschland", "Österreich"]
        self.land.addItems(self.landlist)

        # Windgets dem Layout hinzufügen
        layout.addRow("Name:",self.name)
        layout.addRow("Vorname:",self.vorname)
        layout.addRow("Geburtstag:",self.geburtstag)
        layout.addRow("Adresse:",self.adresse)
        layout.addRow("Postleitzahl:",self.postleitzahl)
        layout.addRow("Ort:",self.ort)
        layout.addRow("Land:",self.land)
        layout.addRow(self.button_showmap)              
        layout.addRow(self.button_save)
        layout.addRow(self.text)
        layout.addRow(self.button_laden)  
        layout.addRow(self.slider)
        # Vernküfung zu Button  <- This is where the magic happens
        self.button_save.clicked.connect(self.exporttocsv)
        self.button_laden.clicked.connect(self.loaddata)
        self.button_showmap.clicked.connect(self.showmap)
        self.slider.sliderReleased.connect(self.showdata)

        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)
        self.show()

    # Funktionen --------------------------------------------------------------

    def close_program(self):
        exit()

    def exporttocsv(self):
        with open('data.csv','a') as f:
            writer = csv.writer(f, delimiter=DELIMITER)
            writer.writerow([
                self.name.text(),
                self.vorname.text(),
                self.geburtstag.text(),
                self.adresse.text(),
                self.postleitzahl.text(),
                self.ort.text(),
                self.land.currentText()
            ])
        self.clearform()
    
    def showmap(self):
        if self.land.currentIndex() == 0:
            return
        else:    
            print("Show Map")
            
            query_str = self.adresse.text().split(" ")
            query_str.append(self.postleitzahl.text())
            query_str.append(self.ort.text())
            query_str.append(self.land.currentText())

            url = MAPS_URL.format(address="+".join(query_str))
            print(url)
            QDesktopServices.openUrl(QUrl(url))
    
    def loaddata(self):
        filter = "CSV (*.csv);;TXT (*.txt)"
        filenamen, filter = QFileDialog.getOpenFileNames(self, "Dateien öffnen", "", filter)

        if filenamen == []:
            return
        else:
            with open(filenamen[0]) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=DELIMITER)
                self.datalist = [Entry(*line) for line in csv_reader]
            self.slider.setRange(0, len(self.datalist) - 1)
        self.showdata()
        
    def showdata(self):
        if self.datalist == []:
            return
        else:
            index = self.slider.value()
            self.name.setText(self.datalist[index].name)
            self.vorname.setText(self.datalist[index].vorname)
        
            qd = QDate.fromString(self.datalist[index].geburtstag, "dd.MM.yyyy")
            self.geburtstag.setDate(qd)

            self.adresse.setText(self.datalist[index].adresse)
            self.postleitzahl.setText(self.datalist[index].postleitzahl)
            self.ort.setText(self.datalist[index].ort)
        
            landindex = self.landlist.index(self.datalist[index].land)
            self.land.setCurrentIndex(landindex)

    def clearform(self):
        # LineEdit
        self.name.clear()
        self.vorname.clear()
        self.adresse.clear()
        self.postleitzahl.clear()
        self.ort.clear()
        # DateEdit
        # https://www.geeksforgeeks.org/pyqt5-qdateedit-setting-date-programmatically/
        d = QDate.fromString("01.01.2001", "dd.MM.yyyy")
        # self.geburtstag.displayFormat()
        self.geburtstag.setDate(d)
        
        # CoboBox
        self.land.setCurrentIndex(0) 

## ----------------------------------------------------------------------------
app = QApplication([])
fenster = Fenster()
# fenster.raise_()
app.exec()


