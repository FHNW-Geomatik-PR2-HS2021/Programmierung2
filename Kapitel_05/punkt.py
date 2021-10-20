class Punkt:
    def __init__(self, x=0, y=0):
        if isinstance(x, (int, float)) and isinstance(y, (int,float)):
            self.x = x
            self.y = y
        else:
            raise ValueError("Die x,y-Koordinaten müssen reale Zahlen sein!")
        
    def __str__(self):
        return f'Punkt({self.x},{self.y})'
    
    def entfernung(self, other):
        if isinstance(other, Punkt):
            return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
        raise NotImplementedError
        
    def __eq__(self, other):
        if isinstance(other, Punkt):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, (list, tuple)) and len(other) == 2:
            return self.x == other[0] and self.y == other[1]
        else:
            raise NotImplementedError("Kann einen Punkt-Objekt nur mit einem anderen, oder mit einer (x,y) Liste / Tuple vergleichen")