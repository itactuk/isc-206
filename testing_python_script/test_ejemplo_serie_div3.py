
from testing_python_script.prueba_abstracta_python import MiPruebaAbstracta


class MisPruebas(MiPruebaAbstracta):

    def ConfigVars(self):
        self.nombre_modulo = __name__

    # todas las pruebas tiene que comenzar con test
    def test_suma_positiva(self):
        self.entro(
            '5\n'
            '3\n' # n1
            '6\n' # n2
            '8\n' # n3
            '2\n' # n4
            '3\n' # n5
        )
        self.veo(
            'Cantidad de numeros: '
            'n1: '
            'Es divisible\n'
            'n2: '
            'Es divisible\n'
            'n3: '
            'No es divisible\n'
            'n4: '
            'No es divisible\n'
            'n5: '
            'Es divisible\n'
        )