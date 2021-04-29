# Faça um programa que leio o nome completo de uma pessoa
# e mostre em seguida o primeiro e o último nome separadamente

nome = input('Digite o nome completo: ').split()

print('Primeiro: {}'.format(nome[0]))
print('Último: {}'.format(nome[len(nome)-1]))
