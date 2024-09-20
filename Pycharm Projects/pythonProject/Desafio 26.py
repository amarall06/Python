frase = input('Digite uma frase:').strip()
frase = frase.lower()
letras = frase.count('a')
pa = frase.find('a')
pu = frase.rfind('a')
print(f'A Frase tem {letras}x a letras A.')
print(f'A letra [a] Aparece pela Primeira vez na posiçao! {pa}')
print(f'A letra [a] Aparece pela Ultima vez na posiçao! {pu}')

