
vproduto = int(input('Digite o valor do produto:R$ '))
print('--------------Formas de Pagamento-------------------')
print('| Digite 1 para pagar a vista no dinheiro ou cheque |')
print('| Digte 2 para pagar a vista no cartão              |')
print('| Digite 3 para pagar em até 2 vezes  no cartão     |')
print('| Digite 4 para pagar em 3 vezes ou mais no cartão  |')
print('-----------------------------------------------------')
fpagamento = int(input('Digite a forma que deseja pagar: '))

if fpagamento == 1:
    vproduto = vproduto - (vproduto * 0.10)
    print('Voce ganhou 10 porcento de desconto e o valor a ser pago será de R${}'.format(vproduto))

elif fpagamento == 2:
    vproduto = vproduto - (vproduto * 0.05)
    print('Voce ganhou 5 porcento de desconto e o valor a ser pago será de R${}'.format(vproduto))

elif fpagamento == 3:
    print('O valor a ser pago será de R${}'.format(vproduto))

elif fpagamento == 4:
    vproduto = vproduto + (vproduto * 0.20)
    print('O valor a ser pago será de R${} devido a um juros de 20 porcento'.format(vproduto))

else:
    print('Por favor digite um numero válido')
