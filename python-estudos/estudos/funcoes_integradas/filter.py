# coding: UTF-8
# Criado por Sostenes em 01/07/2019

"""
    Filter

    filter() -> Serve para filtrar dados de uma determinada coleção

    Diferenças entre map e filter

    map() -> Recebe dois parâmetros, uma função e uma iterável e retorna um objeto mapeando a função para cada elemento iterável
    filter() -> Recebe dois parâmetros, uma função e uma iterável e retorna um objeto filtrando apenas os elementos de acordo
                com o filtro da função (ou lambda) informada.
"""

# Biblioteca para trabalhar com dados estatícos
import statistics


#Exemplo 1

valores = 1,2,3,4,5,6

media = (sum(valores) / len(valores))
print(media)

print("\n\n")

#Exemplo 2

dados = [1,2,3,4,5,6.2,7.1,0.4]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(media)

print("\n\n")


"""
    OBS: Assim como a função map(), a função filter() recebe dois parâmetros, sendo
    uma função e um iterável
"""

# Utilizando Filter

res = filter(lambda x: x > media, dados)
print(list(res))
print(list(res))

print("\n\n")

"""
    OBS: Assim como na função map(), após ser utilizadod as informações de filter() eles são excluídos da memória.
"""
