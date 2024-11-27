pnum = int(input('Primeiro numero:'))
snum = int(input('Segundo numero:'))

if pnum >  snum:
    print('O primeiro numero é maior'.format(pnum, snum))
elif snum > pnum:
    print('O segundo numero é maior'.format(snum, pnum))
else:
    print('Nao existe valor maior, os dois sao iguais!')