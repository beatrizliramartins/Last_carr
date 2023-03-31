import json

with open('meus_pedidos.json') as file:
    json_data = json.load(file)

print(type(json_data))
print(json_data)

json_data_dumps = json.dumps(json_data)
print(type(json_data_dumps))
print(json_data_dumps)

json_string = '{"estabelecimento": "Pastelaria EXU", "pedidos": [{"cliente": "Carlos", "valor": 24.0}, {"cliente": "Joao", "valor": 34.0}]}'


print(type(json_string))
json_data_s = json.loads(json_string)
print(type(json_data_s))
print(json_data_s)