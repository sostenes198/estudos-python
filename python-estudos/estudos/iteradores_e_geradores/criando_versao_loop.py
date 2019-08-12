"""
    Criando sua própria versão do loop
"""

for num in [1,2,3,4,5]:
    print(num)

def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


print(meu_for('abcdefgh'))
print(meu_for([1,2,3,4,5]))