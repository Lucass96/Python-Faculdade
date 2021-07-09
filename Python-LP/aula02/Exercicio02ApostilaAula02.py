# como eu fiz
km = float(input('Quantos km foram percorridos: '))
dias = float(input('Quantos dias o carro foi alugado: '))

carrodia = 0.15 * km
kmrodado = 60 * dias
res = carrodia + kmrodado

print('Voce utilizou o carro durante {} dias, percorrendo {}km. O valor do seu aluguel e de R${}.'.format(dias, km, res))

'''
# como o professor fez
km = int(input('Quantos Km foram percorridos?'))
dias = int(input('Por quantos dias ele foi alugado?'))

preco = 60 * dias + 0.15 * km
print('Km = {}. Dias: {}'.format{km, dias))
print('Valor a ser pago: {}'.format(preco)
'''