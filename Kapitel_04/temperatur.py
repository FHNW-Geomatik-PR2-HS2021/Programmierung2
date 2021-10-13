class Temperatur:
    def __init__(self, c):
        self.celsius = c

    def __str__(self):
        return str(self.celsius) + chr(8451) 

    def __gt__(self, other):
        return self.celsius > other.celsius

    def __lt__(self, other):
        return self.celsius < other.celsius

    def __eq__(self, other):
        return self.celsius == other.celsius

t_muttenz = Temperatur(9.0)
t_zurich = Temperatur(11)

print(t_muttenz)

if t_zurich > t_muttenz:
    print("😡😡😡😡😡😡😡😡")
else:
    print("HAHAHA")

if t_zurich == t_muttenz:
    print("ok")