

class Retangulo:

    def __init__(self, largura = 0, altura = 0):
        self._altura = largura
        self._largura = altura

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        if(not(isinstance(altura, int) and altura > 0)):
            raise ValueError("Altura é inválida: {}".format(altura))
        self._altura = altura

    @property
    def largura(self):
        return self.largura

    @largura.setter
    def largura(self, largura):
        if (not (isinstance(largura, int) and largura> 0)):
            raise ValueError("Larguraé inválida: {}".format(largura))
        self.largura = largura

    @property
    def area(self):
        return self.largura * self.altura

r0 = Retangulo()
r1 = Retangulo(5, 10)
r2 = Retangulo(10, 5)
