from random import randint
print('Sou seu computador...')
print('Pensei em um numero entre 0 e 10')
r = 0
qtdn = 0

computador = randint(0,10)
while r != computador:
    r = int(input('Qual é o seu palpite?: '))
    qtdn += 1
    if r > computador:
        print('Menos... Tente novamente')
    elif r < computador:
        print('Mais... Tente novamente')
print('Parabéns, voce acertou o numero que eu pensei')
print('Voce precisou de {} palpites para vencer'.format(qtdn))

    

