velocidade = int(input('A quantos km/h voce estava?'))
if velocidade > 80:
 print('MULTADO! Voce Ultrapassou o Limite de velocidade da via.')
 multa = (velocidade - 80) * 7
 print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um Bom Dia, Dirija com Segurança.')