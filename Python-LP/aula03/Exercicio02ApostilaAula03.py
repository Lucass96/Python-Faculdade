#a) se idade e maior que 60
idade = int(input('Qual a sua idade: '))
if (idade > 60):
    print('Voce tem direito aos beneficios.')


#b) se dano e maior que 10 e escudo e igual a 0
dano = int(input('Quanto e o seu dano: '))
if (dano > 10):
    print('Voce esta morto!')


#c) se pelo menos uma das variaveis booleanas norte, sul, leste e oeste resultarem em true
norte = True
sul = True
leste = True
oeste = True
if (norte or sul or leste or oeste):
    print('Voce escapou!')