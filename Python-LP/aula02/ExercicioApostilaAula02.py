# como eu fiz
produto = float(input('Qual o preco do produto? '))

porcentagem = float(input('Qual o percentual de desconto?'))
print('O desconto em porcentagem e {}%.'.format(porcentagem))

valor = produto * (porcentagem/100)
print('O desconto sera de R$%.2f.'% valor)

desconto = abs(produto - valor)
print('O valor do seu produto e R$%.2f com desconto de %i por cento o valor final ficara R$%.2f.'% (produto, porcentagem, desconto))


'''
#Como o professor fez

preco = float(input('Digite o preco do produto:'))
p = float(input('Digite o percentual de desconto (0-100)%:'))

desconto = preco * (p / 100)
final = preco - desconto

print('O preco do produto e {}. Desconto de {}%.'.format(preco, p))
print('O valor calculado de desconto: {}. Valor final do produto: {}.'.format(desconto, final))

'''