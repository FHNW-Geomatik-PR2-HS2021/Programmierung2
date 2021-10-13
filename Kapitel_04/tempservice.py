import requests
import apikey

class Temperatur:
    def __init__(self, city):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey.api_key}&units=metric"
        data = requests.get(url)
        x = data.json()["main"]
        self.celsius = x["temp"]
        self.city = city

    def __str__(self):
        return f"Temperatur in {self.city} ist {self.celsius} {chr(8451)}"
    
    def __gt__(self, other):
        return self.celsius > other.celsius

    def __ge__(self, other):
        return self.celsius >= other.celsius
    
    def __lt__(self, other):
        return self.celsius < other.celsius

    def __le__(self, other):
        return self.celsius <= other.celsius
    
    def __eq__(self, other):
        return self.celsius == other.celsius

    def __ne__(self, other):
        return self.celsius != other.celsius
    


t_zurich = Temperatur("Zürich,Switzerland")
t_basel = Temperatur("Basel,Switzerland")

print(t_zurich)
print(t_basel)

if t_zurich > t_basel:
    print("oh, nein!!!!!! ARGH!!!!")
else:
    print("Juhuuuu!!!!")