# coding: UTF-8
# Criado por Sostenes em 02/07/2019

"""
    Reduce

    OBS: A partir do Python3 a função reduce() não é mais uma função integrada (built-in). Agora temos
    que importar e utilizar esta função a partir do módulo 'functools'

    Guido van Rossun (Criador do python): Utilize a função reduce() se você realmente precisar dele. Em todo caso,
    99% das vezes um loop é mais legível

    Para entender o reduce()

    # Imagine que você tem uma coleção de dados:

    dados = [a1,a2,a3...an]

    # E você tem uma função que recebe dois parâmetros:

    def funcao(x,y):
        return x * y

    Assim como map() e filter(), a função reduce() recebe dois parâmetros: a função e o iterável

    A função reduce(), funciona da seguinte forma:
        Passo 1: res1 = f(a1,a2) # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado
        Passe 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passo 1 mais o terceiro elemento e guarda o resultado
        E isso é repetido até o final
"""

from functools import reduce


dados = [2,3,4,5,6,7,8,9,10,1]

#Utilizando reduce

soma = lambda x,y: x+y

res = reduce(soma, dados)
print(res)

print("\n\n")

# Utilizando for
res = 0
for n in dados:
    res = res + n

print(res)

print("\n\n")