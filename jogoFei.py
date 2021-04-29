# sortear um número de 1 a 100, e o usuário vai ter 10 tentativas para aceitar

import random

n = random.randrange(1, 101)
print(n)

chute = 0
while chute != n:
    for i in range(1, 11):
        chute = int(input('Digite o numero:'))

        if i > 10:
            print('Número de tentativas esgotas!')
            break
        else:
            if(n == chute):
                print('Parabéns, você acertou!!')
                break
            elif(n > chute):
                print('numero digitado é menor do que o sorteado')
            elif(n < chute):
                print('numero digitado é maior do que o sorteado')
            else:
                print('valor inválido')
