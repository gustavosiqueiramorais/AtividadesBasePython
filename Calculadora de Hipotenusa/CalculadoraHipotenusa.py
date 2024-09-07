import math

n1 = int(input('Digite o valor do cateto oposto: '))
n2 = int(input('Digite o valor do cateto adjascente: '))

calculo = n1**2 + n2**2 
hipotenusa = math.sqrt(calculo)

print('O valor da hipotenusa desse triangulo retangulo é de {}'.format(hipotenusa))