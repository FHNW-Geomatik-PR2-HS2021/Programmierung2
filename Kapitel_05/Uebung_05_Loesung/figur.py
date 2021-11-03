import math
from punkt import Punkt

    
class Figur:
    def __init__(self, name='Figur'):
        self.name = name
        
    def umfang(self):
        #return 0
        raise NotImplementedError
        
    def flaeche(self):
        #return 0
        raise NotImplementedError
    
    def __str__(self):
        return self.name
    
class Dreieck(Figur):
    def __init__(self, p1, p2, p3):
        super().__init__('Dreieck')
        self.p1 = p1 if isinstance(p1, Punkt) else Punkt(*p1)
        self.p2 = p2 if isinstance(p2, Punkt) else Punkt(*p2)
        self.p3 = p3 if isinstance(p3, Punkt) else Punkt(*p3)
        
    def __str__(self):
        return super().__str__() + f'({self.p1}, {self.p2}, {self.p3})'
    
    def umfang(self):
        return self.p1.entfernung(self.p2) \
                + self.p2.entfernung(self.p3) \
                + self.p3.entfernung(self.p1)
    
    def flaeche(self):
        return 0.5 * abs(
            (self.p1.x - self.p3.x) * (self.p2.y - self.p1.y) \
            - (self.p1.x - self.p2.x) * (self.p3.y - self.p1.y)
        )
    
    
class Rechteck(Figur):
    def __init__(self, p1=(0,0), breite=1, hoehe=1):
        super().__init__('Rechteck')
        self.p1 = p1 if isinstance(p1, Punkt) else Punkt(*p1)
        self.p2 = Punkt(self.p1.x + breite, self.p1.y)
        self.p3 = Punkt(self.p1.x + breite, self.p1.y + hoehe)
        self.p4 = Punkt(self.p1.x, self.p1.y + hoehe)
        
    def __str__(self):
        return super().__str__() \
                + f'({self.p1}, {self.p2}, {self.p3}, {self.p4})'
    
    def umfang(self):
        return 2 * (self.p1.entfernung(self.p2) + self.p2.entfernung(self.p3))
    
    def flaeche(self):
        return (self.p1.entfernung(self.p2) * self.p2.entfernung(self.p3))
    
class Kreis(Figur):
    def __init__(self, M=(0,0), r=1):
        super().__init__('Kreis')
        self.M = M if isinstance(M, Punkt) else Punkt(*M)
        self.r = r
        
    def __str__(self):
        return super().__str__() + f'(M={self.M}, r={self.r})'
    
    def umfang(self):
        return 2 * math.pi * self.r
        
    def flaeche(self):
        return math.pi * self.r**2
    
    
class Polygon(Figur):
    def __init__(self, *punkte):
        if len(punkte) < 3:
            raise ValueError("Polygon muss mindestens aus 3 Punken bestehen!")
            
        super().__init__('Polygon')
        self.punkte = []
        for x in punkte:
            if isinstance(x, Punkt):
                self.punkte.append(x)
            else:
                try:
                    p = Punkt(*x)
                except ValueError:
                    print(f"Kann keinen Punkt aus {x} machen")
                    raise
                self.punkte.append(p)
        
        # letzte Punkt ist implizit gleicht der erster Punkt
        # wird aber intern nicht gespreichert
        # D.h. dies ist gleich:
        #    Polygon(p1, p2, ..., pn, p1)    # p1 wird aus Ende der Liste entfernt
        #    Polygon(p1, p2, ..., pn) 
        if self.punkte[0] == self.punkte[-1]:
            self.punkte = self.punkte[:-1]
        
    def __str__(self):
        return self.name + f'({[str(p) for p in self.punkte]})'
    
    def __len__(self):
        return len(self.punkte)
    
    def umfang(self):
        umfang = 0
        for i in range(len(self)):
            j = (i + 1) % len(self)
            p1 = self.punkte[i]
            p2 = self.punkte[j]
            umfang += p1.entfernung(p2)
        return umfang
    
    def flaeche(self):
        # https://en.wikipedia.org/wiki/Polygon#Area
        flaeche = 0
        for i in range(len(self)):
            j = (i + 1) % len(self)
            flaeche += self.punkte[i].x * self.punkte[j].y - self.punkte[j].x * self.punkte[i].y
        return abs(0.5 * flaeche)