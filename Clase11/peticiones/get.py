import requests

encabezado = {"x-api-key": "reqres-free-v1"}
url = "https://reqres.in/api/users?page=2"

response = requests.get(url,headers=encabezado,verify=False)

print(response.status_code)
data = response.json()
print(data)
