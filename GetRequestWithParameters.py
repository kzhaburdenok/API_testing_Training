import requests

url = "http://httpbin.org/get"

params = {
    'name':'KateTesting',
    'email' : 'email@gmail.com',
    'number' : '+12345678'
}

response = requests.get(url,params=params)
print(response.text)