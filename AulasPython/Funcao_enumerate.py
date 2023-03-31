# Copiado do arquivo For.py

cardapio = ['Carne' , 'Frango', 'Calabresa', 'Pizza' , 'Carne Seca']

print('Pastelaria de EXU')
print('Veja o nosso cardápio')
print('-----------------')
for indice, recheio in enumerate(cardapio):
    print(f'[{indice}]: {recheio}')

opcao = int(input('Digite o número correspondednte ao sabor desejado: '))
if opcao >= 0 and opcao <= len(cardapio):
    print(f'O sabor escolhido foi {cardapio[opcao]}')
else:
    print('Função invalida, tente novamente seguindo a opção correta!')


