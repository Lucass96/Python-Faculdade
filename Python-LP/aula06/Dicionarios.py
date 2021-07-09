game = {'nome':'Super Mario', 'desenvolvedora':'Nintendo', 'ano':1990}
print(game)
print(game['nome'])
print(game['desenvolvedora'])
print(game['ano'])
print(game.values())
print('================')

#values = obtem somente os dados
#keys = obtem somente as chaves
#items = obtem o par chade:dado

for i in game.values():
    print(i)
print('================')

print(game.keys())
print('================')

for i in game.keys():
    print(i)
print('================')

print(game.items())
print('================')

for i,j in game.items():
    print('{} = {}'.format(i, j))
print('================')