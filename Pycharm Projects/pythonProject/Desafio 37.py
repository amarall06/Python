num = int(input('Digite um numero inteiro:'))
print('''Escolha uma das bases para a conversao:
[1] converter para BINARIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opçao = int(input('Sua oppção: '))
if opçao == 1:
    print('{} convertiro para BINARIO é igual a {}'.format(num, bin(num)))
elif opçao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)))
elif opçao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num,hex(num)))
else:
    print('Opção Invalida, Tente novamente.')
