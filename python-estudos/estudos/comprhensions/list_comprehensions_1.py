# coding: UTF-8
# Criado por Sostenes em 15/05/2019


"""
    List Comprehensions

    - Utilizando list comprehension nós podemos gerar novas listas com dados processados a paratir de outro
    interável.

    # Sintaxe
        [ dado for dado in interável ]
"""

#Exemplos

numeros = [1,2,3,4,5]

res = [numero * 10 for numero in numeros]
print(res)

"""
    Para entender melhor oque esta acontecendo, devemos dividir a expressão em duas partes:
    
    - Primeira parte: for numero in numeros
    - Segunda parte: numero * 10
"""

res = [numero / 2 for numero in numeros]
print(res)

def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in numeros]
print(res)

#List comprehensions vs LOOP

print("\n\n")

numeros = [1,2,3,4,5]
numeros_dobrados = []

# LOOP
for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

# List comprehensions
print([numero * 2 for numero in numeros])

# Exemplos
print("\n\n")

#1
nome = 'Sóstenes Gonçalves de Souza'
print([letra.upper() for letra in nome])

#2
amigos = ['majunio', 'hudson', 'raquel']
print([amigo.title() for amigo in amigos])

#3
print([numero * 3 for numero in range(1,10)])

#4
print([bool(valor) for valor in [0, [], '', True, 1, 3.14] ])

#5
print([str(numero) for numero in [1,2,3,4,5]])
