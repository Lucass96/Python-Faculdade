games = {'nome':['Super Mario', 'Zelda Ocarina of Time', 'Pokemon Yellow'], 'videogame':['Super Nintendo','Nintendo 64', 'Game Boy'], 'ano':[1990, 1998, 1999]}
print(games)

print('==============')


games = {'nome':[], 'videogame':[], 'ano':[]}
for i in range(3):
    nome = input('Qual o nome do jogo: ')
    videogame = input('Para qual videogame ele foi lancado: ')
    ano = input('Qual o ano de lancamento: ')
    games['nome'].append(nome)
    games['videogame'].append(videogame)
    games['ano'].append(ano)
print('-' * 20)
print(games)