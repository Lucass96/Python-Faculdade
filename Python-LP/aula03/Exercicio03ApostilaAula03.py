#a) se ano e divisivel por 4
ano = int(input('Digite um ano: '))
if (ano / 4 == 0):
    print('Pode ser um ano bissexto.')
else:
    print('Definitivamente nao e um ano bissexto.')

#b) se cima e baixo forem true
cima = True
baixo = True
if (cima or baixo):
    print('Decida-se!')
else:
    print('Voce escolheu um caminho!')