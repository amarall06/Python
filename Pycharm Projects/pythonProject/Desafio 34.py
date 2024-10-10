
sal = float(input('Qual é o seu salario?:'))
aum = sal + (sal * 10/100)
novo = sal + (sal * 15/100)
if sal >= 1250:
    print('Voce teve aumento de 10% no seu salario, passando a ganhar agora R${:.2f}'.format(aum))
else:
    print('Voce teve aumento de 15% no seu salario, passando a ganhar agora R${:.2f}'.format(novo))
