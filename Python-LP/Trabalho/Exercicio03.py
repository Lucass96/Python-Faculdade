import random

def valida_int(pergunta, min, max):  #VALIDACAO DE DADO
    x =int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

#Programa principal
listaSorteio = []
while True:  #condicao para saber se o usuario vai querer participar do sorteio ou nao
    terminar = input('Deseja participar do sorteio? [S/N]: ')
    if terminar.upper() in 'N': # if para caso ele digite N, o programa sera encerrado
        break
    if terminar.upper() not in 'S': # if para caso ele digite qualquer coisa q n seja S ou N, a pergunta se repetira
        print('Digite S para SIM ou N para NAO')
        continue

    print('=== Sorteio para doacao ===') #painel para usuario escolher de doacao
    print('A cada R$10, 1 nome na lista!')
    print('1- Para doar R$10')
    print('2- Para doar R$20')
    print('3- Para doar R$30')
    print('4- Para doar R$40')
    print('5- Para doar R$50')
    print('6- Para doar R$60')
    print('7- Para doar R$70')

    nome = input('Digite seu nome: ')
    doacao = valida_int('Digite sua opcao: ',1 , 7)
    if doacao == 0 and doacao > 5: #if para caso o usuario escolher outro numero que nao esteja na tabela, ele retornar a pergunta de digitar valor de doacao
        continue

    for i in range(doacao):  # for para adicionar o nome do usuario na lista de acordo com o valor doado
        listaSorteio.append(nome)

print(listaSorteio)
random.shuffle(listaSorteio) #random.shuffle embaralha a lista
sorteado = random.choice(listaSorteio) #random.choice pega aleatoriamente um nome
print('Ganhador do sorteio: {}. Parabens!'.format(sorteado))