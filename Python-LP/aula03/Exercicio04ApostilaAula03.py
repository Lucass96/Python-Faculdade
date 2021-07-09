A = int(input('Digite o primeiro valor: '))
B = int(input('Digite o segundo valor: '))
C = int(input('Digite o terceiro valor: '))

if (A > 0) and (B > 0) and (C > 0):
    if (A + B > C) and (A + C > B) and (B + C > A):
        #se voce chegou ate aqui, e porque o triangulo e valido!
        if A != B and A != C and B != C:
            print('Triangulo escaleno!')
        else:
            if A == B and B == C:
                print('Triangulo equilatero!')
            else:
                print('Triangulo isosceles!')
    else:
        print('Ao menos um dos valores indicados nao servem para formar um triangulo.')

else:
    print('Ao menos um dos valores indicados nao servem para formar um triangulo.')