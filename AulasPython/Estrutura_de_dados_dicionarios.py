cardapio = {}

pastel1 = {'Sabor': 'Queijo', 'Valor': 6.00, 'Status': True, 'Quantidade': 200, 'Unidade':'KGs'}
print(pastel1)

print(pastel1['Sabor'])
print(pastel1['Valor'])
print(pastel1['Status'])
print(pastel1['Quantidade'])
print(pastel1['Unidade'])

pastel1['Valor'] = 7.00
print(pastel1)

print(pastel1.get('Quantidade'))
if pastel1.get('Quantidade'):
    print(pastel1.get('Quantidade'))
else:
    pastel1['Quantidade'] = 10

keys = pastel1.keys()
for key in keys:
    if key == 'Status':
        print(f'A chave: {key} foi encontrada no dicionário')
    else:
        pass

values = pastel1.values()
print(values)
for value in values:
    print(f'O elemento {value} está no dicionário')

dict_values = pastel1.items()
print(dict_values)
for info in dict_values:
    print(f'A chave {key} possui o valor {value}')

pastel1.pop('Status')
print(pastel1)