"""
    Decoradores (Decorators)

    O que são decorators ?

    - Decorators são funções
    - Decorators enlvovem outras funções e aprimoram seus comportamentos;
    - Decorators também são exemplos de High Order Functions;
    - Decorators tem uma sintaxe própria, usando "@" (Syntact Suga/ Açucar Sintático)

"""

# Exemplo: Decorators como função (Syntaxe não recomendada / Sem açucar sintático)

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um ótimo dia')
    return sendo

def saudacao():
    print('Seja bem-vindo soso')

teste = seja_educado(saudacao)
teste()

# Decorators com Syntax Sugar

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer')
        funcao()
        print('tenha um excelente dia')
    return sendo_mesmo

@seja_educado_mesmo
def apresentado():
    print('meu nome é pedro')

print(apresentado())
