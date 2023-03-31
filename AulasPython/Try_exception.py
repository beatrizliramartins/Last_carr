try:
    with open('tentativa.txt') as file:
        print('Arquivo aberto com sucesso, vamos começar o processamento')
except Exception as err:
    print('Falha ao acessar o arquivo')

print('Continuando o código')
print('...')