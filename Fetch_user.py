import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"

response = requests.get(url)

json_response = json.loads(response.text)

pages = jsonpath.jsonpath(json_response, 'data')
print(pages[0])
assert pages[0] == 2, "error"


'''file = open('file/path', 'r')
json_input = file.read()
request_json = json.loads(json_input)

response = requests.post(url, request_json)

assert response.status_code == 201

print(response.headers.get('Content-Length'))

response_json = json.loads(response.text)

id = json.__path__(response_json, 'id')
print(id[0])
'''
