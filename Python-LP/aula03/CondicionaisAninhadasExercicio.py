print('Escolha o que deseja comprar:')
print('1- Maca')
print('2- Laranja')
print('3- Banana')
produto = int(input('Qual a sua escolha? '))
qtd = int(input('Quantas unidades? '))
if (produto == 1):
    pagar = qtd * 2.3
    print('Voce comprou {} macas. Total a pagar: R${}.'.format(qtd, pagar))
else:
    if (produto == 2):
        pagar = qtd = 3.6
        print('Voce comprou {} laranjas. Total a pagar: R${}.'.format(qtd, pagar))
    else:
        if (produto == 3):
            pagar = qtd * 1.85
            print('Voce comprou {} bananas. Total a pagar: R${}.'.format(qtd, pagar))
        else:
            print('Produto inexistente!')