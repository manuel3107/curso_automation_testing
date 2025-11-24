import requests

encabezado = {"x-api-key": "reqres-free-v1"}
url = "https://reqres.in/api/users"

data = {"name":"Jose","job":"Profesor"}

response = requests.post(url,headers=encabezado,json=data)

print(response.status_code)
print(response.json())
