#escreva um algoritmo que crie uma tupla com 10 palavras. encontre as vogais de cada palavra, faca um print na tela com o nome da palavra e suas respectivas vogais

palavras = ('Mario', 'Luigi', 'Peach', 'Yoshi', 'Bowser')

for palavra in palavras:
    print('\nPalavra: {}. Vogais: '.format(palavra.upper()), end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')