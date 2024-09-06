def tabuada(n1):
    n2 = 1
    while n2 <= 10:
        print('\n',n1,'x',n2,'=',n1*n2)
        n2 = n2 +1

numero = int(input('Digite um numero inteiro qualquer: '))
tabuada(numero)