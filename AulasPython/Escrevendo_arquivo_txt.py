clientes = ['Gustavo','Carlos', 'Lucas', 'Pedro', 'Pasulo', 'Jackson', 'Jose' ]
file = open('clientes.txt', 'w')
for cliente in clientes:
    print(f' Cliente {cliente} adicionado a lista')
    file.write(f'{cliente}\n')

file.close()