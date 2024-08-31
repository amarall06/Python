from math import hypot
op = float(input('Digite o valor do cateto Oposto:'))
ad = float(input('Digite o valor do cateto adjacente:'))
hi = hypot(op, ad)
print('O Comprimento da Hipotenusa é de: {:.2f}'.format(hi))