class Robo(object):

    def __int__(self, nome, bateria = 100):
        self.__nome = nome
        self.__bateria = bateria

    @property
    def nome(self):
        return self.__nome

    @property
    def bateria(self):
        return self.__bateria

    def carregar(self):
        self.__bateria = 100

    def dizer_nome(self):
        if self.bateria > 0:
            self.bateria -= 10
            return f'BEEP BOOP BEEP BOOP. EU SOU UM ROBO {self.__nome.upper()}'
        return f'Bateria fraca, por favor, recarregue o {self.__nome} e tente novamente'

