d = int(input('Digite a quantidade de dias alugados:'))
km = float(input('Digite a quantidade de km rodados:'))

pagar = (d * 60) + (km * 0.15)

print('O total a pagar é de: R${:.2f}'.format(pagar))