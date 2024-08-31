carteira = float(input('Quanto voce tem na carteira? R$'))
dolar = carteira / 5.65
euro = carteira /6.23
print('Com R${:.2f}, voce pode comprar US${:.2f} dolares. ja em EUR$ {}'.format(carteira,dolar,euro))
