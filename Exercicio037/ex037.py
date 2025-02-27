numero = int(input('Digite um numero inteiro qualquer: '))

print('-----Base de conversão-----')
print('| Digite 1 para binário    |')
print('| Digite 2 para octal      |')
print('| Digite 3 para hexadecimal|')
print('----------------------------')

option = int(input('Digite a opcao que deseja converter: '))

if option == 1:
    print('{} convertido para binário é igual a {}'.format(numero, bin(numero)))

elif option == 2:
    print('{} convertido para octal é igual a {}'.format(numero, oct(numero)))

elif option == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(numero, hex(numero)))

else:
    print('Por favor digite um numero válido para continuar')