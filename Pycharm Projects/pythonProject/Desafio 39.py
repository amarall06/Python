idade = int(input('Em que ano voce nasceu?'))
res = idade
if idade < 2006:
    print('Ja passou da hora de se alistar!!')
elif idade == 2006:
    print('Ja esta na idade de servir ao exercito!')
else:
    tempo = idade // 18
    print('Você ainda precisa se alistar ao serviço militar. faltam {} anos'.format(tempo))