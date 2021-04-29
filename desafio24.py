# Crie um programa que leia o nome de uma cidade
# e diga se ela comeca com o nome `SANTO`

cidade = input('Digite o nome da cidade: ').split()

print(cidade[:5] == 'SANTO')

if cidade[0] == 'SANTO' or cidade[0] == 'santo':
    print('A cidade informa começa com "SANTO"')
else:
    print('A cidade informa não começa com "SANTO"')
