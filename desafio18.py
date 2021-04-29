#   Exercício Python 18 - Seno, Cosseno e Tangente
#   Faça um programa que leia um ângulo qualquer e mostre na tela
#   o valor do seno, cosseno e tangente desse ângulo.

from math import radians, cos, sin, tan

ang = float(input('Digite o angulo:'))

s = sin(radians(ang))
c = cos(radians(ang))
t = tan(radians(ang))

print('O angulo de {} tem o seno de {:.2f}, cosseno de {:.2f} e tangente de {:.2f}:'.format(ang,s,c,t))

