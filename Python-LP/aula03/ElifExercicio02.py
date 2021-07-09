nome = input('Qual seu nome?')
idade = int(input('Qual sua idade?'))
if nome == 'Vinicius':
    print('Ola, Vinicius!')
elif idade < 18:
    print('Voce nao e o Vinicius! E e menor de idade!')
elif idade > 100:
    print('Diferente de voce, o Vinicius nao e imortal!')