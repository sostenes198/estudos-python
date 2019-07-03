# coding: UTF-8
# Criado por Sostenes em 15/05/2019

"""
    Lambadas

    Conhecidas pro Expressão Lambdas, ou simplesmentes Lambdas, são funções sem nome, ou seja
    funcções anônimas

    # Função em python

    def some(a,b):
        return a + b
"""

# Função em python

def funcao(x):
    return 3 * x + 1

print(funcao(1))
print(funcao(3))
print(funcao(5))

# Função Lambda
print("\n\n\n")

calc = lambda x: 3 * x + 1

# Como utiliza expressão lambda
print(calc(1))
print(calc(3))
print(calc(5))

# Utiliza expressão Lambadas com múltiplas entradas

nome_completo = lambda nome,sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('Soso', 'Dois hit'))

# Lambada sem entrada
amar = lambda : "Como não amara Python"
print(amar())

# Outro exemplo
print('\n\n')
autores = ['Silvane', 'Edmar', 'Soso', 'Majunio', 'Gedson', 'Vanin', 'Junim', 'Raquel', 'Hudson', 'Giovani', 'Rodrigo', 'Iago']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

