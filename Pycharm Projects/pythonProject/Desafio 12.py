produto = float(input('Digite o preço do produto: RS'))
novo = produto - (produto*5/ 100)
print('O Produto que custa R${}, vai custar R${:.2f} com 5% de desconto'.format(produto,novo))
