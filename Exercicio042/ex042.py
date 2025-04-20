r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triangulo')
    if r1 == r2 == r3:
        print('É um triangulo equilatero')
    if r1 != r2 and r2 != r3 != r1:
        print('É um triangulo escaleno')
    else:
        print('É um triangulo isosceles')
else:
    print('Os segmentos não podem formar um triangulo')