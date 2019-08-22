import unittest
from .robo import Robo

class RoboUnitTest(unittest.TestCase):

    def test_carregar(self):
        megamam = Robo()
        self.assertEqual(megamam.bateria, 50)
        megamam.carregar()
        self.assertEqual(megamam.bateria, 100)


if __name__ == '__main__':
    unittest.main()