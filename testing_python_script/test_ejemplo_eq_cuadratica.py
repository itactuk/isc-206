
from testing_python_script.prueba_abstracta_python import MiPruebaAbstracta


class MisPruebas(MiPruebaAbstracta):

    def ConfigVars(self):
        self.nombre_modulo = __name__

    # todas las pruebas tiene que comenzar con test
    def test_valores_positiva(self):
        self.entro(
            '1\n'
            '4\n'
            '4\n'
        )
        self.veo(
            'Digita a: '
            'Digita b: '
            'Digita c: '
            'El resultado es x1=-2.0 y x2=-2.0\n'
        )

    # todas las pruebas tiene que comenzar con test
    def test_b0(self):
        self.entro(
            '1\n'
            '0\n'
            '-4\n'
        )
        self.veo(
            'Digita a: '
            'Digita b: '
            'Digita c: '
            'El resultado es x1=2.0 y x2=-2.0\n'
        )
