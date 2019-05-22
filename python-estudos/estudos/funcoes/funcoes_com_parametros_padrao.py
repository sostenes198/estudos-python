# coding: UTF-8
# Criado por Sostenes em 08/05/2019

"""
    Funções com parâmetros padrão

    Funções onde a passagem de parâmetros seja opcional

    OBS: Em Python, os parâmetros opcionais de uma função devem sempre estar ao final da declaração
"""

def exponencial(numero, potencial=2):
    return numero ** potencial

#Exemplo de utilização de variaveis globais
# PS: Sempre que puder evitar sua utilização EVITE !!!

total = 0

def incrementar():
    global total
    total += 1
    return total


print(incrementar())
print(total)

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável

def fora():
    contador = 0
    def dentro():
        nonlocal  contador
        contador += contador + 1
        return contador
    return dentro()

print(fora())