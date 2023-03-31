'''

Sistema de calculo IMC

O IMC é calculado dividindo o peso (em kg) pela altura ao quadrado (em metros)

- Menor que 18.5 = Magreza
- Entre 18.5 e 24.9 = Normal
- Entre 25.0 e 29.9 = Sobrepeso
- Entre 30.0 e 39,9 = Obesidade grave

'''

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
print('')

'''

imc = peso / (altura ** 2)

imc = round(imc, 2)
'''

imc = peso / (altura ** 2)
imc = round(imc, 2)

if imc < 18.5:
    print(f'Seu IMC {imc} está categorizado como Magreza')
elif imc >= 18.5 and imc <= 24.9:
    print(f'Seu IMC {imc} está categorizado como Normal')
elif imc >= 25.0 and 29.9:
    print(f'Seu IMC {imc} está categorizado como Sobrepeso')
elif imc >= 30.0 and 39.9:
    print(f'Seu IMC {imc} está categorizado como Obesidade')
elif imc > 40:
    print(f'Seu IMC {imc} está categorizado como Obesidade grave, se cuide')

else:
    print('Padrão não definido')




