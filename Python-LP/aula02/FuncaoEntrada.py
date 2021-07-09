# Funcao de entrada
idade = input('Qual sua idade?')
print(idade)

nome = input('Qual seu nome?')
print('Ola {}, seja bem-vindo!'.format(nome))

# 'INPUT' faz o usuario interagir com o programa
# INPUT sempre retorna uma STRING
# para utilizar outro tipo, como numero por exemplo, basta converter

# Convertendo dados de entrada
nota = float(input('Qual nota voce recebeu na disciplina? '))
print('Voce tirou nota {}.'.format(nota))