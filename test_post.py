import requests

url = 'http://3.89.121.108:8000'
body = {'city': 'Faridabad'}

x = requests.post(url, json=body)

print(x)