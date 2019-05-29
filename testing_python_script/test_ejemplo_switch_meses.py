
from testing_python_script.prueba_abstracta_python import MiPruebaAbstracta


class MisPruebas(MiPruebaAbstracta):

    def ConfigVars(self):
        self.nombre_modulo = __name__

    # todas las pruebas tiene que comenzar con test
    def test_febrero(self):
        self.entro(
            '2\n'
        )
        self.veo(
            'Digita mes numerico: '
            'El mes es Febrero\n'
        )

    def test_mayo(self):
        self.entro(
            '5\n'
        )
        self.veo(
            'Digita mes numerico: '
            'El mes es Mayo\n'
        )

    def test_mes_invalido(self):
        self.entro(
            '0\n'
        )
        self.veo(
            'Digita mes numerico: '
            'No es un mes\n'
        )