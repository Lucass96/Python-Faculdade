# Exercicio 1
def borda(s1):
    tam = len(s1)
    # so imprime caso exista algum caractere
    if tam:
        print('+','-' * tam,'+')
        print('|',s1,'|')
        print('+', '-' * tam, '+')

#Programa Principal
borda('Ola, Mundo!')
borda('Logica de Programacao e Algoritmos')