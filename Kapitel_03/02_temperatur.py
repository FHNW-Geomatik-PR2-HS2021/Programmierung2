class Temperatur:
    def __init__(self, celsius=0):
        self.setValue(celsius)

    def setValue(self, v):
        if v < -273.15:
            print("Warnung: Temperatur-Wert wurde korrigiert auf -273.15 Celsius")
            v = -273.15
            #raise ValueError("Absoluter Nullpunkt ist -273.15 Celsius")
        self._value = v
    
    def getValue(self):
        return self._value

    def setValueF(self, f):
        self.setValue((f-32) / 1.8)

    def getValueF(self):
        c = self.getValue()
        f = c * 1.8 + 32
        return f

    celsius = property(getValue, setValue)
    fahrenheit = property(getValueF, setValueF)

## ---------------------------------------------------------

t0 = Temperatur(20)
print(t0.celsius)
print(t0.fahrenheit)

t1 = Temperatur()
t1.fahrenheit = 100
print(t1.celsius)
t1.fahrenheit = -1000




