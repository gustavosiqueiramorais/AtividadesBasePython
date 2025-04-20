anonasc = int(input('Digite o ano de nascimento do atleta: '))
idade = 2025 - anonasc

if idade<=9:
    print('A categoria desse atleta é a mirim')

elif idade > 9 and idade <= 14:
    print('A categoria desse atleta é a infantil')

elif idade > 14 and idade <= 19:
    print('A categoria desse atleta é a junior')

elif idade > 19 and idade == 20:
    print('A categoria desse atleta é a senior')

else:
    print('A categoria desse atleta é a master')