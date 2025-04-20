soma = 0
for c in range(1,6):
    numero = int(input('Digite um numero inteiro: '))
    if numero % 2 == 0:
        soma = soma + numero
print('A soma dos numeros pares digitados é de {}'.format(soma))