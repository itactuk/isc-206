
from testing_python_script.prueba_abstracta_python import MiPruebaAbstracta


class MisPruebas(MiPruebaAbstracta):

    def ConfigVars(self):
        self.nombre_modulo = __name__

    # todas las pruebas tiene que comenzar con test
    def test_suma_positiva(self):
        self.entro(
            '100\n'
            '100\n'
            '50\n'
            '50\n'
            '100\n'
        )
        self.veo(
            'Digite nota examen 1 :'
            'Digite nota examen 2 :'
            'Digite nota examen 3 :'
            'Digite nota examen 4 :'
            'Digite nota examen 5 :'
            'El promedio es: 80.0\n'
        )