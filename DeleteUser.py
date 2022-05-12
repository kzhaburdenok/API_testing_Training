import requests


url = "https://reqres.in/api/users/2"

response = requests.delete(url)

# Fetch Response code

print(response.status_code)

assert response.status_code == 204, f"204 expected, but {response.status_code} is received"
