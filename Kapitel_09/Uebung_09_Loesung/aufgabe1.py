"""
Ausgehend von der Loesung von Celina Neumann, mit einigen Modifikationen
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np


class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Uebung 09 Polynomfunktion")

        layout = QVBoxLayout()
        figure = plt.figure(figsize=(16,9))

        form = QFormLayout()
        self.coeffs = QLineEdit("1,0,0")
        self.n_points = QSlider(Qt.Horizontal)
        self.n_points.setRange(5, 100)
        self.n_points.setValue(10)
        self.minx = QLineEdit("-5")
        self.maxx = QLineEdit("+5")
        self.color_cb = QComboBox()
        self.color_cb.addItems(["r", "g", "b", "c", "y", "m", "k"])

        form.addRow("Koeffizienten:", self.coeffs)
        form.addRow("# Punkte:", self.n_points)
        form.addRow("Min. X-Wert:", self.minx)
        form.addRow("Max. X-Wert:", self.maxx)
        form.addRow("Farbe:", self.color_cb)

        form_widget = QWidget()
        form_widget.setLayout(form)

        self.button = QPushButton("Plot")

        # Widgets erstellen
        self.canvas = FigureCanvas(figure)
        
        # Widgets dem Layout hinzufügen
        layout.addWidget(self.canvas)
        layout.addWidget(form_widget)
        layout.addWidget(self.button)

        # connections
        self.button.clicked.connect(self.plot)
        self.color_cb.activated.connect(self.plot)
        self.coeffs.returnPressed.connect(self.plot)
        self.minx.returnPressed.connect(self.plot)
        self.maxx.returnPressed.connect(self.plot)
        self.n_points.valueChanged.connect(self.plot)

        # Hauptlayout setzten und anzeigen        
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)
        self.show()
    

    def create_polynome_label(self):
        def _sign_and_abs(val):
            val = int(val)
            sign = "-" if val < 0 else "+"
            return sign, str(abs(val))

        coeffs = [x.strip() for x in self.coeffs.text().split(',')]
        exps = list(range(len(coeffs)))[::-1]

        label = ""
        for i in range(len(coeffs)-1):
            sign, coef = _sign_and_abs(coeffs[i])
            exp = exps[i]

            if coef == "0":
                continue
            elif coef == "1":
                coef = ''
            if exp == 1:
                exp = "{}"

            label += f"{sign}{coef}x^{exp}"

        last = coeffs[-1]
        if last != "0":
            sign, coef = _sign_and_abs(last)
            label += f"{sign}{coef}"
        
        # wenn erster Koeff. mit "+" anfängt:
        if label.startswith('+'):
            label = label[1:]

        return label


    def plot(self):
        plt.clf()
        try:
            f = eval(f"np.poly1d([{self.coeffs.text()}])")
            minx = float(self.minx.text())
            maxx = float(self.maxx.text())
            x = np.linspace(minx, maxx, self.n_points.value())
            y = f(x)
        except Exception as e:
            msg = "Bitte geben Sie den Wertebereich von 'x' und die Anzahl der zu berechnenden Punkte an."
            msg += "\n\nPython Exception:\n---\n"
            msg += str(e)
            QMessageBox.critical(self, "Error", msg)
        else:
            c = self.color_cb.currentText()
            plt.plot(x, y, "o-", c=c)
            title = self.create_polynome_label()
            print(title)
            plt.title(f"${title}$")
            self.canvas.draw()
    

app = QApplication([])
fenster = Window()
app.exec()

