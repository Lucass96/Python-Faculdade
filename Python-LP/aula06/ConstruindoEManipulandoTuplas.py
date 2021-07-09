mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
print(mochila)

print(mochila[0]) #print do Elemento 1 - Indice 0
print(mochila[2]) #print do Elemento 3 - Indice 2
print(mochila[0:2]) #print dos Elementos 1 e 2 - Indice 0 e 1
print(mochila[2:]) #print dos Elementos a partir do Indice 2
print(mochila[-1]) #print do ultimo

#mochila[2] = 'Ovos' // vai dar erro pois nao tem como alterar um elemento de uma tupla ja existente
for item in mochila:
    print('Na minha mochila tem: {}'.format(item))

tam = len(mochila)
for i in range (0, tam, 1):
    print('Na minha mochila tem: {}'.format(mochila[i]))


mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
upgrade = ('Queijo', 'Canivete')
mochila_grande = mochila + upgrade

print(mochila)
print(upgrade)
print(mochila_grande)

mochila_grande_invertida = upgrade + mochila
print(mochila_grande)
print(mochila_grande_invertida)