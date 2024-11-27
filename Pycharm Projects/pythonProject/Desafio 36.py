imovel = float(input('Qual é o valor do imovel?'))
salario = float(input('Salário do Comprador: R$'))
anos = int(input('Quantos anos de financimento?'))
min = 
parc = imovel / (anos * 12)
print('Para pagar a casa de R${:.2f} em {} anos'.format(imovel, anos), end='')
print('A prestação será de {:.2f}'.format(parc))

