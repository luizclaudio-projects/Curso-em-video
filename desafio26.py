# Crie um programa que leia uma frase e mostre se quantas letra A aparecem
# e em que posição está a primeira e a ultima

frase = input('Digite uma frase:')

print(frase.count('a'))
print(frase.rfind('a'))
