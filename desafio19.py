# Exercicio Python 19 - Sorteando um nome
# Faça um programa que leia 4 nomes e que escolha um deles

from random import choice

n1 = input('Primero nome:')
n2 = input('Segundo nome:')
n3 = input('Terceiro nome:')
n4 = input('Quarto nome:')

lista = [n1, n2, n3, n4]

print('O nome escolhido é {}'.format(choice(lista)))