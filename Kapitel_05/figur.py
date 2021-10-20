from punkt import Punkt
import math

class Figur:
    def __init__(self, name="Figur"):
        self.name = name

    def umfang(self):
        return 0

    def __str__(self):
        return self.name

#-------------------------------------------

class Kreis(Figur):
    def __init__(self, M=Punkt(0,0), r=1):
        super().__init__("Kreis")
        if type(M) != Punkt:
            raise TypeError("M muss Klasse Punkt sein")
        
        self.Mittelpunkt = M
        self.radius = r
    
    def umfang(self):
        return 2*self.r*math.pi

    def __str__(self):
        return f"{self.name}: Mittelpunkt: {self.Mittelpunkt}, Radius: {self.radius}"


k1 = Kreis()
k2 = Kreis(Punkt(1,1), 4)

print(k1)
print(k2)