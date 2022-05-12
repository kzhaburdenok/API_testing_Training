import re
import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"

# Send Get request
response = requests.get(url)

# Parce response to Json format
json_response = json.loads(response.text)
#print(json_response)

# Fetch value using jsonpath
#pages = jsonpath.jsonpath(json_response, 'total_pages')
pages = json_response['total_pages']
assert pages == 2, f"Qty of pages is {pages}"

qtyOfData = len(json_response['data'])
firstName = jsonpath.jsonpath(json_response, 'data[0].first_name')

for i in range(qtyOfData):
    firstName = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
    print(*firstName)

