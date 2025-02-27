valorc = float(input('Digite o valor da casa desejada:R$ '))
salario = int(input('Digite o valor do seu salário: '))
anos = int(input('Digite em quantos anos deseja pagar: '))

qtdparcela = 12 * anos
mensalidade = valorc / qtdparcela

if mensalidade < salario * 0.30:
    print('Sua proposta foi aceita')
    print('Voce pagara {} parcelas no valor de R${} durante {} anos '.format(qtdparcela,mensalidade,anos))
else:
    print('Sua proposta infelizmente foi negada')
