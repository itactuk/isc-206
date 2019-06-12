
from testing_python_script.prueba_abstracta_python import MiPruebaAbstracta


class MisPruebas(MiPruebaAbstracta):

    def ConfigVars(self):
        self.nombre_modulo = __name__

    # todas las pruebas tiene que comenzar con test
    def test_mediana_en_orden(self):
        self.entro(
            '1\n'
            '2\n'
            '6\n'
            '7\n'
        )
        self.veo(
            'Introduzca 1 numero: '
            'Introduzca 2 numero: '
            'Introduzca 3 numero: '
            'Introduzca 4 numero: '
            'La mediana es: 4.0\n'
        )

    def test_mediana_bmin_dmax(self):
        self.entro(
            '2\n'
            '1\n'
            '6\n'
            '7\n'
        )
        self.veo(
            'Introduzca 1 numero: '
            'Introduzca 2 numero: '
            'Introduzca 3 numero: '
            'Introduzca 4 numero: '
            'La mediana es: 4.0\n'
        )
    def test_mediana_cmin_dmax(self):
        self.entro(
            '2\n'
            '6\n'
            '1\n'
            '7\n'
        )
        self.veo(
            'Introduzca 1 numero: '
            'Introduzca 2 numero: '
            'Introduzca 3 numero: '
            'Introduzca 4 numero: '
            'La mediana es: 4.0\n'
        )
    def test_mediana_amin_cmax(self):
        self.entro(
            '1\n'
            '2\n'
            '7\n'
            '6\n'
        )
        self.veo(
            'Introduzca 1 numero: '
            'Introduzca 2 numero: '
            'Introduzca 3 numero: '
            'Introduzca 4 numero: '
            'La mediana es: 4.0\n'
        )

    def test_mediana_bmin_cmax(self):
        self.entro(
            '2\n'
            '1\n'
            '7\n'
            '6\n'
        )
        self.veo(
            'Introduzca 1 numero: '
            'Introduzca 2 numero: '
            'Introduzca 3 numero: '
            'Introduzca 4 numero: '
            'La mediana es: 4.0\n'
        )