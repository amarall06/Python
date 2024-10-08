distancia = int(input('Qual a Distancia da sua viagem?:'))
kmbaixo = distancia * 0.50
kmalto = distancia * 0.45
if distancia <= 200:
    print('Caso sua Viagem seja menor que 200KM, Voce pagará R$0,50 por cada KM. Totalizando: {:.2f}'.format(kmbaixo))
else:
    print('Caso sua viagem seja maior que 200KM, Voce pagará R$0,45 por cada KM. Totalizando: {:.2f}'.format(kmalto))
