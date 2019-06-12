
from testing_python_script.prueba_abstracta_python import MiPruebaAbstracta


class MisPruebas(MiPruebaAbstracta):

    def ConfigVars(self):
        self.nombre_modulo = __name__

    # todas las pruebas tiene que comenzar con test
    def test_invierno(self):
        self.entro(
            '1\n'
            '1\n'
        )
        self.veo(
            'Día: '
            'Mes: '
            'La estacion es Invierno\n'
        )
    def test_verano(self):
        self.entro(
            '8\n'
            '7\n'
        )
        self.veo(
            'Día: '
            'Mes: '
            'La estacion es Verano\n'
        )
    def test_primera(self):
        self.entro(
            '20\n'
            '5\n'
        )
        self.veo(
            'Día: '
            'Mes: '
            'La estacion es Primavera\n'
        )
    def test_otono(self):
        self.entro(
            '30\n'
            '9\n'
        )
        self.veo(
            'Día: '
            'Mes: '
            'La estacion es Otoño\n'
        )
    def test_invalida(self):
        self.entro(
            '33\n'
            '2\n'
        )
        self.veo(
            'Día: '
            'Mes: '
            'Fecha Invalida\n'
        )
