# Faça um programa que leia um número de 0 a 9999
# e mostre na tela cada um dos digitos separados

n = int(input('Insira um número entre 0 e 9999: '))

print('Número analisado: {}'.format(n))

n2 = str(n)

if n > 0 and n <= 9:
    print('Unidade: {}'.format(n2[0]))

elif n >= 10 and n <= 99:
    print('Unidade: {}'.format(n2[1]))
    print('Dezena: {}'.format(n2[0]))

elif n >= 100 and n <= 999:
    print('Unidade: {}'.format(n2[2]))
    print('Dezena: {}'.format(n2[1]))
    print('Centena: {}'.format(n2[0]))

elif n >= 1000 and n <= 9999:
    print('Unidade: {}'.format(n2[3]))
    print('Dezena: {}'.format(n2[2]))
    print('Centena: {}'.format(n2[1]))
    print('Milhar: {}'.format(n2[0]))
