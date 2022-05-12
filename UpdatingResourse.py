from pydoc import resolve
from urllib import response
import requests
import json
import jsonpath

url = "https://reqres.in/api/users/2"

file = open('UpdateUserData.json', 'r')
json_input = file.read()
request_body = json.loads(json_input)
response = requests.put(url, request_body)
assert response.status_code == 200, f"Response code is {response.status_code}, but 200 is expected"

response_json = json.loads(response.text)
updated_li = jsonpath.jsonpath(response_json, 'name')
print(updated_li[0])

