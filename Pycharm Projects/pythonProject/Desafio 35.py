r1 = float(input('primeiro valor:'))
r2 = float(input('Segundo valor:'))
r3 = float(input('Terceiro valor:'))
if r1 < r2 + r3 and r2 <r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acimas PODEM FORMAR um triangulo!')
else:
    print('OS segmentos acima NAO podem formar um triangulo!')

