def div():
    try:
        num1 = int(input('Digite um numero: '))
        num2 = int(input('Digite um numero: '))
        res = num1 / num2
    except ZeroDivisionError:
        print('Oops! Erro de divisao por zero..')
    except:
        print('Algo de errado aconteceu..')
    else:
        return res
    finally:
        print('Executara sempre!')

#Programa principal
print(div())