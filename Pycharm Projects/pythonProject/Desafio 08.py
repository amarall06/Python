m = float(input('Digite o valor em metros:'))
km = m / 1000
hm = m/ 100
dm = m / 10
cm = m * 100
mm = m *1000
print('{} metros corresponde a {}cm \n Em milimetros {}mm\n Em decametro {:.0f} \n em hectometro {} \n em kilometro {}'.format(m, cm, dm,cm, mm, km))
