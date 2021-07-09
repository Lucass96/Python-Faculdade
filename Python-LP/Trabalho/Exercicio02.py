def pessoa(nome, sobrenome, ru): #funcao que recebe o nome, sobrenome e ru do usuario
    global p1, p2, p3, p4, p5  #deixando todas as variaveis como globais
    p1 = str(input(nome))
    p2 = str(input(sobrenome))
    p3 = p1[0:1] #variavel que pega somente a primeira letra do nome
    p4 = str(input(ru))
    p5 = p3 + p2 + p4 +'@algoritmos.com.br'

#Programa principal
res = pessoa('Digite seu nome: ', 'Digite o seu sobrenome: ', 'Digite os dois ultimos numeros do seu RU: ')
print('Sr {} {}, seu email é {}.'.format(p1, p2, p5.lower()))