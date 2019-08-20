"""
    Atributos

    Represntam as caracteristicas do objeto.

    Em Python, dividimos os atributos em 3 grupos:

        - Atributos de instância;
        - Atributos de classes;
        - Atributos dinâmicos


    # Atributos de instância: são atributos declarados dentro do método construtor.

    # OBS: Métodos construtor: É um método especial utilizado para construção do objeto.

    # Em python por convenção, ficou estabelecido que todos os atributos de uma classe é público, ou seja,
    pode ser acessado em todo o projeto.
    Caso queiramos demonstrar que um determinado atributo deve ser tratado como privado, utiliza-se
    '__' duplo underscore no início do seu nome.
    Isso é conhecido como Name Mangling.
"""

class Produto:

    # Atributo de classe (Atributos estáticos em outras linguages de programação)
    imposto = 0.5

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto.imposto


class Lampada:

    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False

    @property
    def voltagem(self):
        return self.__voltagem

    @property
    def cor(self):
        return self.__cor

    @property
    def ligada(self):
        return self.__ligada


# Atributos dinâmicos -> Um atributo de instância que pode ser criado em tempo de execução
# OBS: Atributos dinâmicos será excluido da instância que o criou

p1 = Produto("ps1", "ps", 1)
p2 = Produto("ps1", "ps", 2)

p2.peso = 5
p1.peso = 1

print(p1.peso)
print(p2.peso)

# Deletando atributos
print(p2.__dict__)
print(p1.__dict__)

del p1.peso
del p2.peso

print(p2.__dict__)
print(p1.__dict__)