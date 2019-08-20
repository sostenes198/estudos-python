"""
    Herançca multipla

    OBS: Herançca multipla pode ser feita de duas maneiras:
        - Por multiderivação direta;
        - Por multiderivação indireta;
"""

# Exemplo Multiderivação direta

class Base1:
    pass

class Base2:
    pass

class MultiDerivada(Base1, Base2):
    pass

# Exemplo Multiderivação indireta

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class Multiderivada(Base3):
    pass