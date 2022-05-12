import requests

url = "https://reqres.in/api/users?page=2"

# Send Get request
response = requests.get(url)

# Display response content
#print("Content: ", response.content)
#print("Headers: ", response.headers)

assert response.status_code == 200, f"Status code is {response.status_code}" # Validating status code

# Fetch Response Header
#print(response.headers)
print("Date is", response.headers.get('Date'))
print("Server is", response.headers.get('Server'))

# Fetch Cookies
print("Cookies is", response.cookies)

# Fetch Encoding
print(response.encoding)

# Fetch Elapsed time
print(response.elapsed)

