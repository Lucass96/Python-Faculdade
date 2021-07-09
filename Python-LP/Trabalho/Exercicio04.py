from operator import itemgetter

#Programa principal
#FAZENDO PARA QUE AS INFORMACOES SEJAM INSERIDAS NO DICIONARIO VIA TECLADO

codigo = {}
lista = []

while True:
    terminar = int(input('Digite o codigo: '))
    if terminar == 0:
        print('Encerrando o programa..')
        break #O programa encerra quando o usuario digitar o codigo 0
    else: # se o usuario nao digitar 0 no codigo, o programa continuara funcionando
        codigo['codigo'] = terminar
        codigo['estoque'] = int(input('Digite o valor do estoque: '))
        codigo['minimo'] = int(input('Digite o valor minimo: '))
        lista.append(codigo.copy()) #adiciona o dicionario na lista
        continue

listaOrdenada = sorted(lista, key=itemgetter('codigo')) #ordenando a lista por ordem crescente por meio de uma bibllioteca
print(listaOrdenada)