# Exercicio 20 - Exibir a aleatório em ordem
# Faça um programa que leia o nome dos quatro alunos
# e mostre a ordem sorteada.

from random import shuffle

n1 = input('Insira o primeiro nome:')
n2 = input('Insira o segundo nome:')
n3 = input('Insira o terceiro nome:')
n4 = input('Insira o quarto nome:')

lista = [n1, n2, n3, n4]
shuffle(lista)

print('A ordem da apresentação será:')
print(lista)
