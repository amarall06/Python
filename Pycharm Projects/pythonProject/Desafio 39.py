from datetime import date
atual = date.today().year
nasc = int(input('Em que ano voce nasceu?'))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos  em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Voce tem que se alistar, IMEDIATAMENTE!')

elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
elif idade > 18:
    saldo = idade - 18
    print('Voce ja deveria ter se alsitado há {} anos'.format(saldo))
    ano =  atual - saldo
