nome = ''
while not nome:
    nome = input('Digite seu nome: ')
valor = int(input('Digite um numero qualquer: '))
if valor:
    print('Voce digitou um valor diferente de zero.')
else:
    print('Voce digitou zero.')