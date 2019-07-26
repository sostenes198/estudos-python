"""
    Levantando erros com raise

    raise -> Lança exceções

    OBS: O raise não é uma função. É uma palavra reservada,assim como def ou qualquer outra em Python.

    Sua forma gera lde utilização é:
        raise TipoDoErro('Mensagem de erro')
"""

#raise ValueError('Valor incorreto')

# Exemplo real
def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    print(f'O Texto {texto} será impresso na cor {cor}')


colore(1, 'azul')
