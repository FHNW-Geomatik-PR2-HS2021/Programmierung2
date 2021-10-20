class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"POINT ({self.x} {self.y})"


# -------------------------------------

a = Punkt(2,3)
print(a) # <__main__.Punkt object at 0x000002851A29D190>

b = Punkt(4,5)
print(b)

print(str(b))
