"""
    Propriedades -> properties
"""

class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f'Seu extrato é {self.__saldo}'


conta1 = Conta('Soso', 123, 999)
conta2 = Conta('Raquel', 123, 999)


print(f'{conta1.titular} {conta1.limite} {conta1.saldo}')
print(f'{conta2.titular} {conta2.limite} {conta2.saldo}')

conta1.limite = 456
conta1.limite = 678

print(f'{conta1.titular} {conta1.limite} {conta1.saldo}')
print(f'{conta2.titular} {conta2.limite} {conta2.saldo}')

conta1.saldo= 456
conta1.saldo = 678