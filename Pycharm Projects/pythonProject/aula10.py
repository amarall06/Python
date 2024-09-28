nome = int(input('Digite um numero para saber se é par ou impar:'))
resto = nome % 2
if resto == 0:
    print('O Número é par!')
else:
    print('O Número é impar!')