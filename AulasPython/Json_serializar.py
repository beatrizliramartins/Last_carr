import json

meus_pedidos = {
    "estabelecimento": "Pastelaria EXU",
    "pedidos":[
    {
        "cliente": "Carlos",
        "valor": 24.00
        },
        {
            "cliente": "Joao",
            "valor": 34.00
        }
    ]
}
print(type(meus_pedidos))

json_data = json.dumps(meus_pedidos, indent=4)
print(type(json_data))
print(json_data)

with open('meus_pedidos.json', 'w') as file:
    json.dump(meus_pedidos, file)

print('Serialização finalizada!')
