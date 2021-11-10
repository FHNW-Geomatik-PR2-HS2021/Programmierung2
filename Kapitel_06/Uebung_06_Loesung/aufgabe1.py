import csv
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GUI - Programmierung")
        self._menuBar = None
        self.initUI()
        self.show()

    def initUI(self):
        self.create_menubar()
        self.add_menu(
            "File", [("Save", self.save_file), ("-", None), ("Quit", exit)]
        )
        self.add_menu(
            "Edit", [("Undo", lambda: print("Undoing...")),
                     ("Redo", lambda: print("Re-doing..."))]
        )

        layout = QFormLayout()

        self.form_vorname = QLineEdit()
        self.form_nachname = QLineEdit()
        self.form_gbttag = QDateEdit()
        self.form_gbttag.setDisplayFormat("dd.MM.yyyy")
        self.form_adresse = QLineEdit()
        self.form_plz = QLineEdit()
        self.form_ort = QLineEdit()
        self.form_land = QComboBox()
        self.form_land.addItems(
            ["Schweiz", "Deutschland", "Österreich", "Frankreich", "Dänemark"]
        )

        self.save_btn = QPushButton("Save")
        self.save_btn.pressed.connect(self.save_file)

        layout.addRow("Vorname:", self.form_vorname)
        layout.addRow("Name:", self.form_nachname)
        layout.addRow("Geburtstag:", self.form_gbttag)
        layout.addRow("Adresse:", self.form_adresse)
        layout.addRow("Postleitzahl:", self.form_plz)
        layout.addRow("Ort:", self.form_ort)
        layout.addRow("Land:", self.form_land)
        layout.addRow(self.save_btn)

        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)


    def create_menubar(self):
        if self._menuBar is None:
            self._menuBar = self.menuBar()


    def add_menu(self, name, menu_items):
        menu = self._menuBar.addMenu(name)

        for action_name, action_func in menu_items:
            # action_name = '-' => addSeparator
            if action_name == "-":
                menu.addSeparator()
            else:
                action = QAction(action_name, self)
                menu.addAction(action)
                action.triggered.connect(action_func)


    def save_file(self):
        filename, filter = QFileDialog.getSaveFileName(
            self,
            caption="Datei speichern",
            directory=QDir.currentPath(),
            filter="Text files (*.txt *.csv)",
        )
        if filename:
            with open(filename, "w") as file:
                writer = csv.writer(file, delimiter=",")
                writer.writerow(
                    [
                        self.form_vorname.text(),
                        self.form_nachname.text(),
                        self.form_gbttag.text(),
                        self.form_adresse.text(),
                        self.form_plz.text(),
                        self.form_ort.text(),
                        self.form_land.currentText(),
                    ]
                )


def main():
    app = QApplication([])
    fenster = MainWindow()
    fenster.show()
    app.exec()


if __name__ == "__main__":
    main()
