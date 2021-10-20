# Code der Aufgabe 1 hier

class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def len(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5


# folgenden Code nur ausführen, wenn diese Modul direkt ausgeführt wird
# (nicht beim Importieren)
if __name__ == '__main__':
    a = Vector3(1, 1, 0)
    b = Vector3(1, 2, 3)
    print(a.len())
    print(b.len())
