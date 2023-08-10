'''
Duas palavras são um “par inverso” se uma for o contrário da outra. Escreva uma função que dado duas palavras,retorne True caso sejam.
'''

def verifcar_par_inverso(palavra1, palavra2):
    lista_string1 = list(palavra1)
    lista_string2 = list(palavra2)

    if lista_string1.remove() == lista_string2:
        return True