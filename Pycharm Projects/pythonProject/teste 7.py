
nome = int(input('Digite um numero para saber se é par ou impar:'))
resto = nome % 2
if resto == 0:
    print('O numero é par!')
else:
    print('O numero é impar!')