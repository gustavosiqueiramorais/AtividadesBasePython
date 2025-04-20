numero = int(input('Digite o numero da tabuada desejada: '))

for c in range(1,11):
    print('{}X{}={}'.format(numero,c,numero*c))
print('Esta é a tabuada do numero que escolheu')