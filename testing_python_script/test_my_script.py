
from testing_python_script.prueba_abstracta_python import MiPruebaAbstracta


class MisPruebas(MiPruebaAbstracta):

    def ConfigVars(self):
        self.nombre_modulo = __name__

    # todas las pruebas tiene que comenzar con test
    def test_suma_positiva(self):
        self.entro('1\n2\n')
        self.veo('Digita un número: Digita otro número: Mi total es :3\n')

    def test_suma_negativa(self):
        self.entro("""-2
        -3""")
        self.veo('Digita un número: Digita otro número: Mi total es :-5\n')

    def test_suma_pos_neg(self):
        self.entro("""-2
        3""")
        self.veo('Digita un número: Digita otro número: Mi total es :1\n')
