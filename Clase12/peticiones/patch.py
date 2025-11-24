import requests

url = "https://reqres.in/api/users/2"
encabezado = {"x-api-key": "reqres-free-v1"}

data = {"name":"Jose"}

response = requests.patch(url,headers=encabezado,json=data)

print(response.status_code)
print(response.json())