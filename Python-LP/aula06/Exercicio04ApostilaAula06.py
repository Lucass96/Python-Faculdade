#crie um programa para ler o nome, ano de nascimento e sexo de diferentes pessoas
#armazene os dados em um dicionario com listas
#ao encerrar o cadastro, apresente:
#o total de cadastros efetuados
#a media das idades das pessoas
#uma lista de mulheres com menos de 30 anos
#uma lista de homens com idade acima da media

cadastro = {'nome':[], 'sexo':[], 'ano':[]}

while True:
    terminar = input('Deseja cadastrar uma pessoa? [S/N]: ')
    if terminar.upper() in 'N':
        break
    if terminar.upper() not in 'S':
        print('Digite S para SIM ou N para NAO')
        continue

    nome = input('Qual seu nome: ')
    sexo = input('Qual seu sexo [M/F]: ')
    ano = int(input('Quall seu ano de nascimento: '))
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)

print(cadastro)