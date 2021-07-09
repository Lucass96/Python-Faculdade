games = []
game1 = {'nome':'Super Mario', 'videogame':'Super Nintendo', 'ano':1990}
game2 = {'nome':'Zelda Ocarina of Time', 'videogame':'Nintendo 64', 'ano':1998}
game3 = {'nome':'Pokemon Yellow', 'videogame':'Game Boy', 'ano':1999}
games = [game1, game2, game3]
print(games)

print('============================')

game = {}
games = []
for i in range(3):
    game['nome'] = input('Qual o nome do jogo: ')
    game['videogame'] = input('Para qual videogame ele foi lancado: ')
    game['ano'] = input('Qual o ano de lancamento: ')
    games.append(game.copy())
print('-' * 20)
for e in games:
    for i,j in e.items():
        print('O campo {} tem o valor {}.'.format(i, j))