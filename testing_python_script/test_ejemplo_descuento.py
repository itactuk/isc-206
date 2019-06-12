
from testing_python_script.prueba_abstracta_python import MiPruebaAbstracta


class MisPruebas(MiPruebaAbstracta):

    def ConfigVars(self):
        self.nombre_modulo = __name__

    # todas las pruebas tiene que comenzar con test
    def test_A(self):
        self.entro(
            '100\n'
            '10\n'
        )
        self.veo(
            'Digite precio: '
            'Digite porcentaje descuento: '
            'El nuevo precio es 90.0\n'
        )
    def test_B(self):
        self.entro(
            '500\n'
            '10\n'
        )
        self.veo(
            'Digite precio: '
            'Digite porcentaje descuento: '
            'El nuevo precio es 450.0\n'
        )
