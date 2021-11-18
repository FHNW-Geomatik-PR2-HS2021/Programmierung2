from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import QIntValidator, QDoubleValidator

MAPS_URL = "https://www.google.ch/maps/place/{breite},{laenge}"

ORTE = {
    "Muttenz": (47.534867, 7.641571),    # Name: Breite, Länge
    "Olten"  : (47.346469, 7.910095),
    "Paris"  : (48.860984, 2.327964)
}  


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("showmap.ui", self)

        defaultProfile = QWebEngineProfile.defaultProfile()
        defaultProfile.setPersistentCookiesPolicy(QWebEngineProfile.ForcePersistentCookies)

        # add progress bar to the status bar
        self.progressBar = QProgressBar()
        self.statusbar.addPermanentWidget(self.progressBar)

        self.create_connects()
        self.show()

    def create_connects(self):
        self.pushButton.clicked.connect(self.load_map)
        self.webEngineView.loadFinished.connect(self.clear_status_bar)
        self.webEngineView.loadProgress.connect(self.progressBar.setValue)
        self.comboBox.activated.connect(self.set_coords)

    def load_map(self):
        breite = self.breiteLineEdit.text()
        laenge = self.laengeLineEdit.text()
        breite_valid, laenge_valid = self._validate_breite_laenge(breite, laenge)
        if not (breite_valid and laenge_valid):
            QMessageBox.critical(self, "Fehler!", "Ungültige Werte")
            return

        url = MAPS_URL.format(breite=breite, laenge=laenge)

        self.statusbar.showMessage(f"Loading {url}...")
        self.webEngineView.load(QUrl(url))

        print(url)

    def set_coords(self):
        if self.comboBox.currentIndex() == 0:
            breite = laenge = ""
        else:
            ort = self.comboBox.currentText()
            breite, laenge = ORTE[ort]

        self.breiteLineEdit.setText(str(breite))
        self.laengeLineEdit.setText(str(laenge))

    def clear_status_bar(self):
        # after the web page has loaded, clear the status and the progress bar
        self.statusbar.clearMessage()

    def _validate_breite_laenge(self, breite, laenge):
        def is_number_in_range(num, min_val, max_val):
            try:
                num = float(num)
                return (min_val <= num <= max_val)
            except ValueError:
                return False

        breite_valid = is_number_in_range(breite, -90, 90)
        laenge_valid = is_number_in_range(laenge, -180, 180)

        return breite_valid, laenge_valid




app = QApplication([])
window = MainWindow()
app.exec()