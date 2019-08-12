"""
    Decorators com diferentes assinaturas

    # Para resolver utilizamos Decorator Pattern

    Assinatura de uma função é representada, pelo seu retorno nome e parâmetros de entrada.
"""

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá eu sou {nome}'

@gritar
def ordernar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal} e acompanhamento de {acompanhamento}'

print(saudacao('Soso'))
print(ordernar('Picanha', 'Bata Frita'))

@gritar
def lol():
    return 'lol'

print(lol())

#OBS: Vale lembrar que podemos utilizar parâmetros nomeados

print(ordernar(acompanhamento='Batata Frita', principal='Picanha na Brasa'))

# Decorators com parametro

def verifica_primeiro_numero(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna

@verifica_primeiro_numero(10)
def soma(num1, num2):
    return num1 + num2

print(soma(10, 20))
print(soma(1, 20))