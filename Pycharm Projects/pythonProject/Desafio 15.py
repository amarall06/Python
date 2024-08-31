km = float(input('Quantos km você percorreu com o carro?'))
dia = int(input('E Para quantos dias você alugou ele?'))
carro = 60
kms = 0.15
total = (kms * km) + (carro * dia)
print('Você percorreu {:.0f}km, alugou o carro por {} dias. ira pagar RS{:.2f}'.format(km,dia, total ))