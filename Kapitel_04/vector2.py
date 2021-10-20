class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Vector2(self.x-other.x, self.y-other.y)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Vector2(self.x * other, self.y * other)
        else:
            return Vector2(self.x*other.x, self.y*other.y)
    
    def __rmul__(self, other):
        if type(other) == int or type(other) == float:
            return Vector2(self.x * other, self.y * other)
        else:
            return Vector2(self.x*other.x, self.y*other.y)

    def __neg__(self):
        return Vector2(-self.x, -self.y)


    def __str__(self):
        return f"VECTOR ({self.x} {self.y})"

#----------------------------------------

a = Vector2(3,4)
b = Vector2(2,3)
c = Vector2(4,5)

resultat = ( a + b + c ) + a + b + a + b + ( c + a ) + a + a
print(resultat)

a = Vector2(4,5)
b = Vector2(2,3)
c = a * b
print(c)

d = a * 2
print(d)

d = 2 * a
print(d)

a = Vector2(1,2)
b = Vector2(2,3)
c = Vector2(2,2)

d = a + (b * c)
print(d)

a = Vector2(1,2)
a += Vector2(1,1)
print(a)

b = -a
print(b)


a = +5