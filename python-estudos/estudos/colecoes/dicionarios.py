# coding: UTF-8
# Criado por Sostenes em 10/04/2019

"""

    Dicionários:

    São coleções do tipo chave valor,
    São representados por chave {}

    Obs:
        - Chave e valor são representados por 'chave': 'valor',
        - Tanto chave quanto valor podem ser de qualquer tipo de dados,
        - Podemos misturar tipos de dados


"""

print(type({}))

# Criação de dicionarios

# Forma 1
print("------------------------------------------------------")

paisesForma1 = {"br": "brasil", "eua": "USA", "py": "Paraguai"}
print(paisesForma1)

# Forma 2
print("------------------------------------------------------")

paisesForma2 = dict(br='Brasil', eua='Estados Unidos', py='Paraguia')
print(paisesForma2 )

# Acessando elementos

# Forma 1
print("------------------------------------------------------")

print(paisesForma1['br'])
print(paisesForma2['eua'])

# Forma 2
print("------------------------------------------------------")

print(paisesForma1.get('br'))
print(paisesForma2.get('eua'))

# Pode ser definir um valor padrão, para caso não se encontre o objeto com a chave informada
print("------------------------------------------------------")

pais = paisesForma1.get('xl', "pais não encontrado")

print('br' in paisesForma1)

if 'py' in paisesForma1:
    print("Tem o pais")


# Pode se utilizar qualquer tipo de dados (int, float, string, boolean), inclusive lista, tupla, dicionario como chave
print("------------------------------------------------------")

localidade = {
    (35.6656565, 35.656565): "São paulo",
    (36.6656565, 36.656565): "Braizl",
    (37.6656565, 37.656565): "Aqui",
}

print(localidade)

# Adicionar elementos em um dicionario
print("------------------------------------------------------")

dicionario = {'jan': 100, 'fev': 120, 'marc': 300}

# Forma 1 - Mais comum
dicionario['abr'] = 100

# Forma 2
novo_dado = {'mai': 500}
dicionario.update(novo_dado)

# Atualizando dados em um dicionario
print("------------------------------------------------------")

# Forma 1
dicionario['mai'] = 550

# Forma 2
dicionario.update({'mai': 600})

# Conclusão
# Dicionarios não podem ter chaves repetidas

# Remover dados de um dicionario
print("------------------------------------------------------")

# Forma 1
dicionario.pop('mar')

# Obs ao remover um objeto, o valor deste objeto é sempre retornado

#Forma 2
del dicionario['jan']

#Obs: desta forma não é retornando o objeto excluido


