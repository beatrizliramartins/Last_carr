'''
mensagem_boasvindas = 'Seja bem-vindo a pastelaria EXU, diga "Laroyê" para agradecer'

nome_pedido1 = 'Carlos'
sabor_pedido1 = 'Frango'

nome_pedido2 = 'Pedro'
sabor_pedido2 = 'Queijo'

print(f'O {nome_pedido1} pediu pastel de {sabor_pedido1}')
print(f'O {nome_pedido2} pediu pastel de {sabor_pedido2}')
'''

def mensagem_boasvindas(nome):
    print(f'Seja bem-vindo a pastelaria {nome}, diga "Laroyê" para agradecer')



def add_pedidos(cliente, sabor):
    novo_pedido = f'O {cliente} pediu pastel de {sabor}'
    return novo_pedido

mensagem_boasvindas(nome='EXU')

add_pedidos(cliente='Robert', sabor='Frango')
add_pedidos('Jose', 'Queijo')