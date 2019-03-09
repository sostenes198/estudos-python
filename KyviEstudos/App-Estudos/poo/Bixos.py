

class Bichos:
    quant_bichos = 0

    def __init__(self):
         self.add_bicho()

    def __del__(self):
        self.del_bicho()
        if(self.quant_bichos == 0):
            print("Todos bixos morreram!!! :'( ")

    @classmethod
    def add_bicho(cls):
        cls.quant_bichos+= 1

    @classmethod
    def del_bicho(cls):
        cls.quant_bichos-= 1

    #add_bicho = classmethod(add_bicho)
    #del_bicho = classmethod(del_bicho)

b1 = Bichos()
b2 = Bichos()
b3 = Bichos()

print(Bichos.quant_bichos)