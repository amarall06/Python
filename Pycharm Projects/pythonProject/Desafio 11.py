a = float(input('Quanto de altura tem a parede?'))
l = float(input('Quanto de largura tem a parede?'))
area = a * l
print('A parede tem {}x{} e sua área tem {} m²,'.format(a,l, area))
tinta = area /2
print('Para pintar a área voce vai precisar de {} litros de tinta'.format(tinta))