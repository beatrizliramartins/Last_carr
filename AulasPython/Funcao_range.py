numeros = range(11)
print(numeros)
print(type(numeros))
print(list(numeros))

numeros_impar = []
numeros_par = []
print('')

for numero in numeros:
    print(f'O valor do range agora é: {numero}')
    if numero % 2 == 0:
        numeros_par.append(numero)
    else:
        numeros_impar.append(numero)

print(numeros_par)
print(numeros_impar)