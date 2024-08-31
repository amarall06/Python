from random import shuffle
n1 = input('Digite seu nome aqui:')
n2 = input('Digite seu nome aqui:')
n3 = input('Digite seu nome aqui:')
n4 = input('Digite seu nome aqui:')
alunos = [n1, n2, n3, n4]
shuffle(alunos)
print(f'Ordem de apresentação é:')
print(alunos)

