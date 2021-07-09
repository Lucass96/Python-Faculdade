# Concatenacao de Strings
s1 = 'Logica de Programacao'
s1 = s1 + 'e Algoritmos'
print(s1)

# Repetindo strings na concatenacao
s1 = 'A' + '-' * 10 + 'B'
print(s1)

# Composicao
nota = 8.5
s1 = 'Voce tirou %f na disciplina de Algoritmos' % nota
print(s1)

# Composicao - limitando as casas decimais
nota = 8.5
s1 = 'Voce tirou %.2f na disciplina de Algoritmos' % nota
print(s1)

# Composicao - varias variaveis
nota = 8.5
disciplina = 'Algoritmos'
s1 = 'Voce tirou %.2f na disciplina de %s' % (nota, disciplina)
print(s1)

# Composicao mais moderna
nota = 8.5
disciplina = 'Algoritmos'
s1 = 'Voce tirou {} na disciplina de {}'.format(nota, disciplina)
print(s1)

# Fatiamento
s1 = 'Logica de Programacao e Algoritmos'
print(s1[0:6])

s1 = 'Logica de Programacao e Algoritmos'
print(s1[24:34])

s1 = 'Logica de Programacao e Algoritmos'
print(s1[:6])

# Tamanho(Length)
s1 = 'Logica de Programacao e Algoritmos'
tamanho = len(s1)
print(tamanho)