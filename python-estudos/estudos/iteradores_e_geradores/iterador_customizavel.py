"""
    Escrevendo iteradores customizados
"""
class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor <= self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration

def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

con = Contador(1, 61)
it = iter(con)
print(meu_for(it))

for n in Contador(1,61):
    print(n)

for n in range(1,61):
    print(n)