'''
Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sua posição na lista. 
'''

lista = []

for n in range(5):
    lista.append(int(input('Digite um número:')))

for n in range(5):
    print(f'lista[{n}] contém {lista[n]}')
