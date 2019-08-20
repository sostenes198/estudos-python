"""
    Herançca (Inheritance)

    A ideia de herançca é a de reaproveitar código. Também extender nossas classses

    OBS: Com a herançca, a partir de uma classe existentes, nos extendemos outra classe
    que passa a herdar atributos e métodos da classe herdada.

    Quando uma classe herda de outra classe, a classe herdada é conhecida como:
        - Super classe;
        - Classe mãe
        - Classe pai
        - Classe base
        - Classe genérica

    Quando uma classe herda de outra classe, ela é chamada:
        [Cliente, funcionário]
        - Sub classe
        - Clsse filha
        - Classe específica
"""

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


class Cliente(Pessoa):

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda

class Funcionario(Pessoa):

    def __init__(self, nome, sobrenome, cpf, matricula):
        Pessoa.__init__(self, nome, sobrenome, cpf)
        self.__renda = matricula

    def nome_completo(self):
        print(super().nome_completo())
        return f'Funcionario {self.nome} {self.sobrenome}'

cliente = Cliente('Soso', 'Souza', '123', 125)
funcionario = Funcionario('Ed', 'Souza', '123', '42134')
print(cliente.nome_completo())
print(funcionario.nome_completo())