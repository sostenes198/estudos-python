"""
    Forçando tipos de dados com decoradores

    Relembrando zip

    a = (1, 3, 5)
    b = (2, 4, 6)

    c = zip(a,b)
    (1,2, 3,4,5,6)
"""


def forca_tipo(*tipos):
    def decarador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for(valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
                return funcao(*novo_args, **kwargs)
            return converte
        return decarador


@forca_tipo(str, int)
def repete_mensagem(msg, vezes):
    for vez in range(vezes):
        print(msg)

repete_mensagem('Mensa', 5)

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