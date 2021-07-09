#Escreva um algoritmo que permita cadastrar jogos informando o nome e a qual videogame ele pertence
#Alem disso, armazene todos os dados em um arquivo de texto que deve ser salvo em disco e manter os dados cadastrados

def valida_int(pergunta, min, max):
    x =int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criacao do arquivo.')
    else:
        print('Arquivo {} foir criado com sucesso!\n'.format(nomeArquivo))

def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        print(a.read())
    finally:
        a.close()

def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        a.write('{}; {}\n'.format(nomeJogo, nomeVideogame))
    finally:
        a.close()

#Programa principal
arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no sistema.')
else:
    print('Arquivo inexistente.')
    criaArquivo(arquivo)

while True:
    print('MENU')
    print('1 - Cadastrar novo item')
    print('2 - Listar cadastros')
    print('3 - Sair')

    op = valida_int('Escolha a opcao desejada: ', 1, 3)
    if op == 1:
        print('Opcao de cadastrar novo item selecionada.\n')
        nomeJogo = input('Nome do Jogo: ')
        nomeVideogame = input('Nome do Videogame: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)
    elif op == 2:
        print('Opcao de listar selecionada.\n')
        listarArquivo(arquivo)
    elif op == 3:
        print('Encerrando o programa...')
        break