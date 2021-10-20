class Fahrzeug:
    def __init__(self, farbe, räder):
        self.farbe = farbe
        self.räder = räder
        self.fahrgestellnummer = ""
        self.sitzplätze = 0

    def fahren(self):
        print("fährt weg...")

## --------------------------------------------

class PKW(Fahrzeug):
    def __init__(self, schiebedach, farbe, räder):
        super().__init__(farbe, räder)
        self.schiebedach = schiebedach

    def __str__(self):
        return f"**PKW** Schiebedach: {self.schiebedach}, Farbe {self.farbe}, Räder: {self.räder}"

##--------------------------------------------

class Fahrrad(Fahrzeug):
    def __init__(self, rahmengrösse, farbe):
        super().__init__(farbe, 2)
        self.rahmengrösse = rahmengrösse

    def __str__(self):
        return f"**FAHRRAD** Rahmengrösse: {self.rahmengrösse}, Farbe {self.farbe}"

##----------------------------------------------

tesla = PKW(True, "grün", 4)
print(tesla)
tesla.fahren()

fiat = PKW(False, "schwarz", 3)
print(fiat)

scott = Fahrrad(54, "grau")
print(scott)