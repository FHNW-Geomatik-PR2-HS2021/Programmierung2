import urllib.parse


url = "http://www.fhnw.ch/"

query = 'Hellö Wörld@'
a = urllib.parse.quote(query)

url = url + a
print(url)
