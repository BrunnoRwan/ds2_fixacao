'''
Faça uma lista de compras do mês, não se esqueça de comprar produtos de limpeza e sorvete.
Agora «vá ao mercado» e delete apenas os produtos de limpeza da lista.
Agora «vá à sorveteria» e se empanturre e sorvete e tire o sorvete da lista.
'''

lista_limpeza = ['desinfetante', 'detergente', 'bucha']
lista_aliemntos = ['carne', 'sorvete', 'arroz', 'feijão']
lista_compras = [lista_limpeza, lista_aliemntos]

print('Lista de compras:', lista_compras)

print('Comprou os produtos de limpeza')
lista_compras.remove(lista_limpeza)
print('Lista de compras:', lista_compras)

print('Comprou sorvete')
lista_aliemntos.remove('sorvete')
print('Lista de compras:', lista_compras)
