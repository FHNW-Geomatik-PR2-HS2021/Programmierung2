from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.uic import *

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Kapitel_08/webbrowser.ui", self)

        # Cookies erlauben
        defaultProfile = QWebEngineProfile.defaultProfile()
        defaultProfile.setPersistentCookiesPolicy(QWebEngineProfile.ForcePersistentCookies)

        self.show()

        self.pushButton.clicked.connect(self.loadPage)

    def loadPage(self):
        htmlcode = """
        <h1>Hello World</h1>
        Dies ist eine Website<br/>
        Bla bla bla
        """
        #self.webEngineView.setHtml(htmlcode)

        self.webEngineView.load(QUrl("https://www.fhnw.ch"))


app = QApplication([])
fenster = Browser()
app.exec()
