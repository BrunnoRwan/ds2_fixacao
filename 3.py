'''
Ler uma lista com 4 notas, em seguida o programa deve exibir as notas e a média. 
'''

#fiz desse jeito:

notas = []

for n in range(4):
    notas.append(float(input('Digite uma nota:')))

nota_total = 0

for n in range(4):
    nota_total += notas[n]

media = nota_total / 4

print(f'Sua média é: {media}')

#aprendi a melhorar desse jeito:

'''
notas = [float(input('Digite uma nota:')) for _ in range(4)]

media = sum(notas) / 4

print(f'Média: {media}')
'''