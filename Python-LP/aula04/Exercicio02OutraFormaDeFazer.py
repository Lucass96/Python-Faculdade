print('CALCULADORA')
print('+ Adicao')
print('- Subtracao')
print('* Multiplicacao')
print('/ Divisao')
print('Digite "sair" para finalizar.')

op = input('Qual operacao deseja fazer? ')
if op == '+' or op == '-' or op == '*' or op == '/':
    x = int(input('Digite o primeiro valor: '))
    y = int(input('Digite o segundo valor: '))

while True:
    op = input('Qual operacao deseja fazer? ')
    if op == '+' or op == '-' or op == '*' or op == '/':
        x = int(input('Digite o primeiro valor: '))
        y = int(input('Digite o segundo valor: '))

    if (op == '+'):
        res = x + y
        print('Resultado: {} + {} = {}.'.format(x, y, res))
        continue
    elif (op == '-'):
        res = x - y
        print('Resultado: {} - {} = {}.'.format(x, y, res))
        continue
    elif (op == '*'):
        res = x * y
        print('Resultado: {} * {} = {}.'.format(x, y, res))
        continue
    elif (op == '/'):
        res = x / y
        print('Resultado: {} / {} = {}.'.format(x, y, res))
        continue
    elif (op == 'sair'):
        break
    else:
        print('Operacao invalida.')

print('Encerrando o programa...')