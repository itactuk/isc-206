import unittest
import P2.torneo.es_primo as lib

class PruebaPrimo(unittest.TestCase):
    def test_primo_2(self):
        self.assertEqual(lib.es_primo(2), True)
    def test_primo_3(self):
        self.assertEqual(lib.es_primo(3), True)
    def test_primo_4(self):
        self.assertEqual(lib.es_primo(4), False)