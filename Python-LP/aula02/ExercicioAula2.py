valor1 = int(input('Digite um numero:'))
valor2 = int(input('Digite outro numero:'))
#Maneira Classica
soma = 'O resultado da soma de %i com %i e %i.' % (valor1, valor2, valor1 + valor2)
print(soma)
#Maneira Moderna
soma = 'O resultado da soma de {} com {} e {}.'.format(valor1, valor2, valor1 + valor2)
print(soma)