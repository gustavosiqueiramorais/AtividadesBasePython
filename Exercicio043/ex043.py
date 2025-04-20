peso = float(input('Digite o seu peso atual: '))
alt = float(input('Digite sua altura: '))

imc = peso /(alt ** 2)

print(imc)

if imc < 18.5:
    print('Voce esta abaixo do peso ideal')

elif imc == 18.5 and imc < 25:
    print('Voce esta no peso ideal')

elif imc >=25 and imc < 30:
    print('Voce esta com sobrepeso')

elif imc >= 30 and imc <= 40:
    print('Voce esta obeso')

elif imc > 40:
    print('Cuidado, voce esta com obesidade mórbida')
