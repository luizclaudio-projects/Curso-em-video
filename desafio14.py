import emoji

gc = float(input('Informe a temperatura em ºC:'))

gf = ((gc*1.8) + 32)

print(emoji.emojize('A temperatura de {}ºC corresponde a :penguin:{}ºF!'.format(gc, gf)))