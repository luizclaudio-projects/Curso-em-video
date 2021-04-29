p = float(input('Digite o valor do produto:'))
pd = int(input('Digite a porcentagem de desconto:'))

vd = ((pd/100)*p)

print('O valor {} com {}% de desconto é: {}'.format(p,pd,p-vd))