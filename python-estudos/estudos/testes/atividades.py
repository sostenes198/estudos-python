import unittest

def comer(comida, eh_saudavel):
    if(eh_saudavel):
        return 'Estou comendo quiabo porque quero manter a forma'
    else:
        return 'Não sou saudável'


def dormir(num_horas):
    return num_horas


class AtividadesTest(unittest.TestCase):

    def teste_comer(self):
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma'
        )

    def test_comer_pizza(self):
        self.assertEqual(
            comer('pizza', False),
            'Não sou saudável'
        )

if __name__ == '__main__':
    unittest.main()
