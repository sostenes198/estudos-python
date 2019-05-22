# coding: UTF-8
# Criado por Sostenes em 09/04/2019

"""

    Tuplas (tuple)

    São bastantes parecidas com listas.

    Existem basicamente duas diferenças básicas:

    1 - As tuplas são representadas por parênteses ()

    2 - As tuplas são imutaveis, isso significa que ao se criar uma tupla ela não muda,
        toda alteração em uma tupla, gera uma nova tupla.



"""

print(type(()))

print("--------------------------------------------")


# Cuidado, as tuplas são representadas por (), mas veja:
print("--------------------------------------------")

tupla1 = (1,2,3,4,5)
print(tupla1)

tupla2 = 1,2,3,4,5, 6
print(tupla2)

# Cuidodo, com tupla de um elemento, pois tupla de um elemento não é uma tupla
print("--------------------------------------------")

tupla1 = (1)
print(type(tupla1)) # Isso não é uma tupla

# Conclusão, Podemos concluir que tuplas são definidas por virgulas

# Podemos gerar uma lista com range
print("--------------------------------------------")

tupla = tuple(range(1,10))
print(tupla)

# Desempacotamento de tupla
print("--------------------------------------------")

tupla = ('Soso', 'Dois', 'Hit')
nome, tipo, so = tupla
print(nome)
print(tipo)
print(so)

# Se os valores forem inteiros ou reais pode se usar:
print("--------------------------------------------")

tupla = (1,2,3,4,5,6)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tupla
print("--------------------------------------------")

tupla1 = (1,2,3,4)
tupla2 = (4,5,6,7)
print(tupla1 + tupla2) # Tuplas são imutaveis
print(tupla1)
print(tupla2)
tupla3 = tupla1 + tupla2
print(tupla3)

# Verificar se a tupla contains determinado elemento
print("--------------------------------------------")

tupla = (1,2,3)
print(3 in tupla)

# Interando em uma tupla
print("--------------------------------------------")

tupla = (tuple(range(1,10)))

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice)
    print(valor)

# Contando elementos dentro da tupla
print("--------------------------------------------")

tupla = ('a', 'a', 1,2,3,2,2)
print(tupla.count('a'))
print(tupla.count(2))

# Dicas, devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados de uma coleção
# Podemos acessar um elemento de uma tupla via indice Exemplo: tuple[1]

# Verificar em qual indice está um elemento da tupla
print("--------------------------------------------")

print(tupla.index(3))

# Porqe utiliza tuplas
# São mais rápidas que listas
# Tuplas deixam seu código mais seguro

