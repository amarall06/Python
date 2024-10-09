vel = int(input('Digite a velocidade que voce estava:'))
if vel > 80:
    print('Voce passou do limite da via, voce foi MULTADO!')
    multa = (vel - 80) * 7
    print('A sua multa vai custar R$7,00 por cada km, ou seja, voce vai pagar {:.2f} de multa'.format(multa))
print('Tenha um Bom dia! Dirija com segurança!')

