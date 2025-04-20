sexo = str(input('Digite o seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MmFf':
    print('Por favor, digite termos válidos')
    sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
print('Seu sexo é {}'.format(sexo))