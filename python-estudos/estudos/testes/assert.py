"""
    Assertion
"""

def soma_numeros_positovios(a, b):
    assert a > 0 and b > 0, 'Ambos números precisam ser positivos'
    return a + b

print(soma_numeros_positovios(2,4))
#print(soma_numeros_positovios(0,4))