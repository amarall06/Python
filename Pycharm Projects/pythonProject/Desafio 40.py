not1 = float(input('Primeira nota:'))
not2 = float(input('Segunda nota:'))
med = (not1 + not2) / 2
if med < 5.0:
    print('Sua média foi abaixo de 5.0: REPROVADO!')
elif med == 5.0 and 6.9:
    print('Você esta em Recuperação')
else:
    print('Sua media foi superior a 7: APROVADO!')
print('')