n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
r = ''
while r != 5:
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair do programa')
    r = int(input('Digite o numero desejado: '))
    if r == 1:
        print('A soma entre {} e {} é de {}'.format(n1,n2,n1+n2))
    elif r == 2:
        print('A multiplicação entre {} e {} é de {}'.format(n1,n2,n1*n2))
    elif r == 3:
        if n1 > n2:
            maior = n1
        else: 
            maior = n2
        print('O maior numero entre os dois é {}'.format(maior))
    elif r == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
print('Saindo do programa...')


