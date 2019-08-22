"""
    Doctests

    São testes que colocamos nas docsstring das funções/métodos do python

    para rodar: python -m doctest -v nome_do_modulo.py
"""

def soma(a,b):
    """Soma os números a e b

        >>> soma(1,2)
        3
    """
    return a + b

print(soma(1,2))