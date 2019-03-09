

class A:

    def __init__(self):
        self._var = 0

    def _get_var(self):
        return self._var

    def _set_var(self, var):
        self._var = var

    var = property(fget=_get_var(), fset=_set_var())


a = A()
a.var
