"""
    Preservando metadados com wraps

    Metadados -> São dados intrísecos em arquivos.
    Wrap -> São funções que envolvem elementos com diversas finalizadas (Empacotadores)
"""

# Problema

def ver_log(funcao):
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a,b):
    """Soma dois números"""
    return a + b

print(soma(1,2))
help(soma)
print(soma.__name__)
print(soma.__doc__)
print('\n\n')

# Resolução do problema

from functools import wraps

def ver_log_resolucao(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log_resolucao
def soma_resolucao(a,b):
    """Soma dois números"""
    return a + b

print(soma_resolucao(1,2))
help(soma_resolucao)
print(soma_resolucao.__name__)
print(soma_resolucao.__doc__)