num = (input('Digite um numero de 0 a 9999:'))
r = '000' + num
print(f'Unidade {r[-1]}')
print(f'Dezena {r[-2]}')
print(f'Centena {r[-3]}')
print(f'Milhar {r[-4]}')