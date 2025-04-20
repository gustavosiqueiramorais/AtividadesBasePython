maior = 0
menor = 0
for c in range(1,8):
    ano = int(input('Digite o ano de seu nascimento: '))
    if 2025 - ano >=18:
        maior = maior + 1
    else:
        menor = menor + 1
print('A quantidade de menores é de {} e a quantidade de maiores de idade é de {}'.format(menor,maior))