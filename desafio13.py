s = float(input('Digite o valor do salário:'))
pa = int(input('Digite a porcentagem de aumento:'))

va = ((pa/100)*s)

print('O salário de {:.2f} com o aumento de {}% é igual a: {:.2f}'.format(s,pa,s+va))