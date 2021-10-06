# Klassendefinition
class Punkt:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def ausgabe(self, untereinander):
        if untereinander:
            print("x=", self.x)
            print("y=", self.y)
        else:
            print(f"Punkt: [{self.x},{self.y}]")

    def distanz(self, b):
        return ((self.x-b.x)**2 + (self.y-b.y)**2)**0.5
        
if __name__ == "__main__":
    a = Punkt(3,4)
    b = Punkt(2,4)
    a.ausgabe(False)
    b.ausgabe(False)
    print(a.distanz(b))
