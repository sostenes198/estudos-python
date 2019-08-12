"""
    Funções de Maior Grandeza - High Order Functions - HOF

    Oque isso significa?

    - Quando uma linguagem de programação suporte HOF, indica que podemos ter funções que retornam
    outras funções como resultado ou mesmo que podemos passar funções como argumentos para outras funções, e até
    mesmo criar variáveis do tipo de funções no nosso programa

    Em python, as funções são Cidadões de Primeira Classe, First Class Citizien
"""

# Exemplo - Definindo funções

def somar(a, b):
    return a + b

def diminuir(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)


print(calcular(1, 2, somar))

# Nested Functions
"""
    Em python podemos também ter funções dentro de funções, que são conhecidos por Nested Functions
    ou também Inner Functions (Funções Internas).
"""

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa

print(cumprimento('Soso'))


# Retornando funções de outras funções

def faz_me_rir():
    def rir():
        return choice(('hahasudhausd', 'kkkkkkkkkk', 'ashudhaus123'))
    return rir

rindo = faz_me_rir()
print(rindo())
print(faz_me_rir()())