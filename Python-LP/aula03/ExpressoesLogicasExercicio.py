# ler nota final do aluno em cada materia e informar se passou de ano ou nao
m1 = float(input('Digite a nota da 1 materia: '))
m2 = float(input('Digite a nota da 2 materia: '))
m3 = float(input('Digite a nota da 3 materia: '))
if m1 >= 7 and m2 >= 7 and m3 >= 7:
    print('O aluno esta aprovado de ano!')
else:
    print('O aluno nao passou de ano!')