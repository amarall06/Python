valor = int(input('Qual é o valor do imovel?'))
nome = str(input('Qual é o seu nome completo?'))
salario = int(input('Quanto você ganha no mês?'))
anos = int(input('Em quantos anos pretende pagar o Imovel?'))
parc = valor // anos
emprestimo = (parc % 30)
if parc == emprestimo:
    print('Parabéns o senhor(a) {}, o seu financiamento foi aceito!'.format(nome))
else:
 print('Sentimos muito senhor(a), o seu financimento por negador por exceder os 30% do seu salario')
