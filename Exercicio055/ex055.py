maiorpeso = 0
menorpeso = 2000

for c in range(0,5):
    peso = float(input('Digite o seu peso: '))
    if maiorpeso < peso:
        maiorpeso = peso
    elif peso < menorpeso:
        menorpeso = peso
print('O maior peso registrado foi de {} quilos e o menor foi de {} quilos'.format(maiorpeso,menorpeso))