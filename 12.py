'''
Escreva uma função que imprime todos os números primos entre 1 e 50
'''

def imprimir_numeros_primos():
    for num in range(2, 51):
        if verificar(num):
            print(num)

def verificar(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

imprimir_numeros_primos()

