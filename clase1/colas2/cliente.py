import requests

url = 'https://verbose-system-97jqjjvxgwfpxvg-8080.app.github.dev/'

# ejemplo request en GET
r = requests.get(url, timeout=5)
print(r.text)

# ejemplo request en POST
r = requests.post(url + 'encolar', json={'tipo': 'moto', 'matricula': 'ABC123', 'color': 'rojo', 'marca': 'yamaha', 'kilometraje': 1000}, timeout=5)
print(r.text)