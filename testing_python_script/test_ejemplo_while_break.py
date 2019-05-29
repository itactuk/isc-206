
from testing_python_script.prueba_abstracta_python import MiPruebaAbstracta


class MisPruebas(MiPruebaAbstracta):

    def ConfigVars(self):
        self.nombre_modulo = __name__

    # todas las pruebas tiene que comenzar con test
    def test_suma_positiva(self):
        self.entro(
            '1\n'
            '4\n'
            '7\n'
            '3\n'
        )
        self.veo(
            'Menu:\n'
            '1. Suma\n'
            '2. Resta\n'
            '3. Salir\n'
            'Digite opcion: '
            'Digite primer numero: '
            'Digite segunto numero: '
            'El resultado es: 11\n'
            'Menu:\n'
            '1. Suma\n'
            '2. Resta\n'
            '3. Salir\n'
            'Digite opcion: '
        )