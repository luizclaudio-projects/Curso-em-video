# Faça um programa que leia um nome e mostre:
# todas as letras maiusculas;
# todas as letras minusculas;
# quantas letras ao todo (sem considerar os espaços);
# quantas letras tem o primeiro nome;

nome = input('Digite o nome: ')

print(nome.upper())
print(nome.lower())

x = nome.replace(" ", "")
print(len(x))

p = nome.split()
print(len(p[0]))
