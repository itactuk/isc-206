
from testing_python_script.prueba_abstracta_python import MiPruebaAbstracta


class MisPruebas(MiPruebaAbstracta):

    def ConfigVars(self):
        self.nombre_modulo = __name__

    # todas las pruebas tiene que comenzar con test
    def test_suma_positiva(self):
        self.entro(
            'Hola Como estas?\n'
        )
        self.veo(
            'Digite una palabra:'
            'Hol Como ests?\n'
        )