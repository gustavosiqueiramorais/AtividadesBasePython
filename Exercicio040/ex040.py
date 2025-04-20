nota1 = float(input('Digite o valor da sua primeira nota: '))
nota2 = float(input('Digite o valor da sua segunda nota: '))
media = (nota1 + nota2) / 2

if media <= 5.0:
    print('Voce foi reprovado')
    print(media)

elif media > 5.0 and  media <= 6.9:
    print('Voce esta de recuperação')
    print(media)

else: 
    print('Voce foi aprovado')
    print(media)
 