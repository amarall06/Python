salário = float(input('Digite quanto você ganha no mês:'))
aumento = salário + (salário*15/ 100)
print('Antes voce ganhava RS{:.2f}, com 15% de aumento vai passar a ganhar RS{:.2f}!'.format(salário, aumento))