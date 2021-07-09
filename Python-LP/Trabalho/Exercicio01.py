while True:  # este while esta servindo para validar se o usuario quer inserir os dados ou nao
    dados = input('Inserir dados? 0- Nao           1- Sim ')
    if dados in '0': # caso o usuario digite 0, o programa sera encerrado.
        print('encerrando programa...')
        break
    if dados not in '1': # caso o usuario digite qualquer coisa que nao seja o 1, o laco se repete e aparecec uma mensagem de alerta.
        print('Digite 1 para SIM ou 0 para NAO')
        continue

    #Programa principal
    nome = input('Nome do aluno: ')
    nota = float(input('Nota final: '))
    if nota >= 0.0 and nota <= 2.9:
        print('O aluno {} tirou a nota {} e se enquandra no conceito E.'.format(nome, nota))
    else:
        if nota >= 3.0 and nota <= 4.9:
            print('O aluno {} tirou a nota {} e se enquandra no conceito D.'.format(nome, nota))
        else:
            if nota >= 5.0 and nota <= 6.9:
                print('O aluno {} tirou a nota {} e se enquandra no conceito C.'.format(nome, nota))
            else:
                if nota >= 7.0 and nota <= 8.9:
                    print('O aluno {} tirou a nota {} e se enquandra no conceito B.'.format(nome, nota))
                else:
                    if nota >= 9.0 and nota <= 10.0:
                        print('O aluno {} tirou a nota {} e se enquandra no conceito A.'.format(nome, nota))
                    else:
                        if nota > 10.0:
                            print('Nota invalida!')