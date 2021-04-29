from math import hypot

op = float(input('Insira o tamanho do cateto oposto:'))
ad = float(input('Insira o tamanho do cateto adjacente:'))

hi = hypot(op, ad)
print('O tamanho da hipotenusa é {}'.format(hi))