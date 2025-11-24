import requests
api_key = {"x-api-key": "reqres-free-v1"}
url = 'https://reqres.in/api/users/2'
payload = {"name":"Valentina","job":"Tutora"}
response = requests.put(url, headers=api_key,json=(payload))
print(requests.status_codes)
print(response.json())