# coding: UTF-8
# Criado por Sostenes em 08/04/2019

"""

    Listas em python

    Listas em python funciona como vetores/matrizes (arrays) em outras linguagens, com a diferença
    de serem DINAMICO e também de  de podermos colocar QUALQUER tipo de dado.

    --  Lista em python é dinâmica e não possui tamanho fixo, ou seja, podemos criar  a lista e simplesmente
        ir adicionando elementos
    --  Qualquer tipo de dado
    -- Listas em python são representadas por []

"""

type([])

lista1 = [1, 2, 3, "", 4, {}, []]

lista2 = ['s','o','s','o']

lista3 = []

lista4 = list(range(11))

lista5 = list('Soso')

# Verificando valores contidos na lista

if 8 in lista4:
    print("Encontrei o numero 8")

if 18 not in lista4:
    print("Não encontrei o numero 18")

# Ordernar lista

print("====================================================================")

lista6 = [1, 1, 1,  10, 9, 2, 4, 3, 5, 6, 7, 8]
lista7 = ['d', 'c', 'b', 'a', 'd', 'd']
lista6.sort()
lista7.sort()
print(lista6)
print(lista7)

# Contar ocorrencias de repeticoes em uma lista

print("====================================================================")

print(lista6.count(1))
print(lista7.count('d'))

# Adicionar elementos em listas
# para adicionar elementos em uma lista utiliza-se append
print("====================================================================")

print(lista1)
lista1.append("abc")
print(lista1)

lista1.append(['1', 2, 3]) # Cria uma nova lista dentro da lista
print(lista1)

lista1.extend([1, 2,3, 4]) # Coloca a lista como elemento adicional a lista principal
print(lista1)

# Lista insert, insert

print("====================================================================")

lista2.insert(2, 55)
print(lista2)

# Juntas duas listas

print("====================================================================")

lista1.extend(lista2)
print(lista1)

# Inverter uma lista

print("====================================================================")

lista1.reverse()
print(lista1)
print(lista1[::-1])

# Remover ultimo elemento de uma lista e o retorna

print("====================================================================")

print(lista6)
lista6.pop()
print(lista6)

# Remover elemento pelo indice
# Obs: elementos a direita do indice são deslocados para esquerda,
# Se não ouver elemento no indice informado teremos o erro index error
print("====================================================================")

print(lista5)
lista5.pop(2)
print(lista5)

# Repetir elementos em uma lista
print("====================================================================")

nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Converter string para lista
print("====================================================================")

# Forma 1
stringLista = "Soso dois hit"
print(stringLista)
stringLista = stringLista.split()
print(stringLista)

# Forma 2
stringLista = "Soso.Sosodois.hit"
print(stringLista)
stringLista = stringLista.split('.')
print(stringLista)

# Converter uma lista em string
print("====================================================================")

stringLista = ''.join(stringLista)
print(stringLista)

# interando em lisra
print("====================================================================")

#Forma 1
for  elemento in lista1:
    print(elemento)

#Forma
i = 0
lista_while = []
while i < 10:
    lista_while.append(i)
    i += 1

print(lista_while)

# Fazemos acesso aos elementos de forma indexada
print("====================================================================")

lista_cores = ['amarelo', 'vermelho', 'rosa']
print(lista_cores[0])
print(lista_cores[1])
print(lista_cores[2])

# Encontar o indice de um elemento na lista
print("====================================================================")

lista_indice_elemento = [1,2,3,4,5]
print(lista_indice_elemento)
print(lista_indice_elemento.index(1))
print(lista_indice_elemento.index(4))
print(lista_indice_elemento.index(5))

# Pode ser fazer buscar de indixes em ranger
print("====================================================================")

# Realizar operações em lista
print("====================================================================")
lista_valores = [1,2,3,4,5,6]
print(lista_valores)
print(sum(lista_valores))
print(max(lista_valores))
print(min(lista_valores))

# Converter para tupla
print("====================================================================")

print(lista_valores)
tuple = tuple(lista_valores)
print(tuple)

# Desempacotamento de lista
print("====================================================================")

lista_valores_3 = [1,2,3]
num1, num2, num3 = lista_valores_3
print(num1)
print(num2)
print(num3)

# Copiando uma lista para outra (Shallow copy e Deep copy)
# Deep copy
print("====================================================================")

lista = [1,2,3]
nova = lista.copy()

nova.append(4)
print(lista)
print(nova)

# Forma shallow copy
print("====================================================================")

lista = [1,2,3]
print(lista)

nova = lista

nova.append(4)
print(lista)
print(nova)