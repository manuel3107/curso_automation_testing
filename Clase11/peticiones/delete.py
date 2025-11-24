import requests

encabezado = {"x-api-key": "reqres-free-v1"}
url = 'https://reqres.in/api/users/2'

response = requests.delete(url, headers=encabezado)

print(response.status_code)
print(response.json())
print(response.text) 