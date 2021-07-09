def comida():
    print(ovos)

#Programa principal
ovos = 12
comida()

#----------------------------------------------

def comida():
    ovos = 12
    bacon()
    print(ovos)
def bacon():
    ovos = 6

#Programa principal
comida()

#----------------------------------------------

def comida():
    ovos = 'variavel local de comida'
    print(ovos)

def bacon():
    ovos = 'variavel local de bacon'
    print(ovos)
    comida()
    print(ovos)

#Programa Principal
ovos = 'variavel global'
bacon()
print(ovos)