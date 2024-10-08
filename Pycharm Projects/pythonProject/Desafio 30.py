num = int(input('Digite um numero para saber se é par ou impar:'))
resto = num % 2
if resto == 0:
    print('O numero é par!'.format(num))
else:
    print('O numero é impar!'.format(num))