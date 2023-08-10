'''
Ler uma lista de 10 números reais e mostre-os na ordem inversa. 
'''

lista = []

for n in range(10):
    lista.append(float(input('Digite um número:')))

lista.reverse

print(lista)