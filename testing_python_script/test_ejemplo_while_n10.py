
from testing_python_script.prueba_abstracta_python import MiPruebaAbstracta


class MisPruebas(MiPruebaAbstracta):

    def ConfigVars(self):
        self.nombre_modulo = __name__

    # todas las pruebas tiene que comenzar con test
    def test_suma_positiva(self):
        self.entro(
            ''
        )
        self.veo(
            '1\n'
            '2\n'
            '3\n'
            '4\n'
            '5\n'
            '6\n'
            '7\n'
            '8\n'
            '9\n'
            '10\n'
        )
