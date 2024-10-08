ano = int(input('Digite o ano que voce quer analisar:'))
if ano % 4 == 0:
    print('O Ano {} é Bissexto!'.format(ano))
else:
    print('O ano {} NAO é Bissexto!'.format(ano))