import requests

header_data = {
    'T1':'First_Header',
    'T2':'Second_Header'
}

url = "http://httpbin.org/get"

response = requests.get(url, headers=header_data)
print(response.text)