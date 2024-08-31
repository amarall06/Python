from random import choice
aluno1 = input('Digite seu nome:')
aluno2 = input('Digite seu nome:')
aluno3 = input('Digite seu nome:')
lista = [aluno1, aluno2, aluno3]
escolhido = choice(lista)
print('Que Azar aluno {}, voce foi o escolhido para limpar o quadro.'.format(escolhido))