while True:
    try:
        x = int(input('Por favor digite um numero: '))
        break
    except ValueError:
        print('Ooops! Numero invalido. Tente novamente...')