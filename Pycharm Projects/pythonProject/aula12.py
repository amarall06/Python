nome = str(input('Qual é seu nome?'))
if nome == 'Felipe':
    print('Que nome bonito!')
elif nome == 'Pedro' or 'Ana' or 'Maria' or 'Jula':
    print('Seu nome é bem comum no Brasil!')
elif nome == 'Ana Claudia Fernanda Luana':
    print('Que belo nome feminino!')
else:
    print('Que nome estranho.')
print('Muito prazer em te conehcer, {}!'.format(nome))