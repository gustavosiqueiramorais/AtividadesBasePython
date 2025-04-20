anonasc = int(input('Digite o ano de seu nascimento: '))
idade = 2025 - anonasc

if idade <=17:
    print('Voce ainda vai se alistar no exercito')

elif idade > 18:
    print('Ja passou seu tempo de alistamento')

else:
    print('Prepare-se, chegou a hora de fazer seu alistamento')
