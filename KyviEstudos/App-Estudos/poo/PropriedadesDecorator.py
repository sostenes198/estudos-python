

class A:

    def __init__(self):
        self._var = 0

    @property
    def var(self):
        return self._var

    @property.setter
    def var(self, var):
        self._var = var

a = A()
a.var
