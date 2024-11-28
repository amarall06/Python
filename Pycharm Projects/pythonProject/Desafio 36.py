imovel = float(input('Qual é o valor do imovel?'))
salario = float(input('Salário do Comprador: R$'))
anos = int(input('Quantos anos de financimento?'))
min = salario * 30 / 100
parc = imovel / (anos * 12) # porcentagem
print('Para pagar a casa de R${:.2f} em {} anos'.format(imovel, anos), end='')
print('A prestação será de {:.2f}'.format(parc))
if parc <= min:
    print('O Emprestimo foi ACEITO!')
else:
    print('O Emprestimo foi NEGADO!')


