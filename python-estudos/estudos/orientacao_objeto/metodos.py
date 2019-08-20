"""
    Métodos (funções) -> Representam os comportamentos do objeto

    # Em python, dividimos em 2 grupos: Métodos de instância
    e métodos de classe

    OBS: Todos elementos em Python que inicia e finaliza com duplo underline é chamado dunder (Double Underline)

    OBS: Os métodos/funções dundes em python são chamados de métodos mágicos
"""
print(dir())
print(dir(__builtins__))
# Métodos de intância

class Usuario:

    __contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.__contador} usuários no sistema')

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

user = Usuario('soso', 'souza', 'soso', '123')

print(user.__dict__)
Usuario.conta_usuarios()