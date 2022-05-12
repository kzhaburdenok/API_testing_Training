from pydoc import resolve
from urllib import response
import requests
import json
import jsonpath

url = "https://reqres.in/api/users"

# Read input Json file
file = open('UserData.json', 'r')
json_input = file.read()
request_body = json.loads(json_input)
response = requests.post(url, request_body)
#print(response.content)

assert response.status_code == 201, f"Response code is {response.status_code}, but 201 is expected"

# Fetch header from response
print(response.headers.get('Content-Length'))

# Parse response to json format
response_json = json.loads(response.text)
print(response_json)

# Pick ID using jsonpath
idValue = jsonpath.jsonpath(response_json, 'id')
print("ID value is", idValue[0])
