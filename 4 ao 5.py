'''
Ler um vetor com 20 idades e exibir a maior e menor.
Utilizando o del, remova todos os elementos da lista criada anteriormente até a lista ficar vazia. 
'''

import random

#4

listIdades = [int(input('Digite uma idade: ')) for _ in range(20)]

#listIdades = [random.randint(1, 99) for _ in range(20)]
    
listIdades.sort()

print(f'lista: {listIdades}')

print(f'O maior é: {max(listIdades)} e o menor é: {min(listIdades)}')

#5

for n in range(20):
    del listIdades[0]

if len(listIdades) == 0:
    print('A lista foi totalmente deletada')