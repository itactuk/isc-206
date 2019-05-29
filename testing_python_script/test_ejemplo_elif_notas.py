
from testing_python_script.prueba_abstracta_python import MiPruebaAbstracta


class MisPruebas(MiPruebaAbstracta):

    def ConfigVars(self):
        self.nombre_modulo = __name__

    # todas las pruebas tiene que comenzar con test
    def test_A(self):
        self.entro(
            '90\n'
        )
        self.veo(
            'Digita un nota númerica: '
            'Su calificación es: A\n'
        )
    def test_B(self):
        self.entro(
            '80\n'
        )
        self.veo(
            'Digita un nota númerica: '
            'Su calificación es: B\n'
        )
    def test_C(self):
        self.entro(
            '75\n'
        )
        self.veo(
            'Digita un nota númerica: '
            'Su calificación es: C\n'
        )
    def test_D(self):
        self.entro(
            '60\n'
        )
        self.veo(
            'Digita un nota númerica: '
            'Su calificación es: D\n'
        )
    def test_F(self):
        self.entro(
            '50\n'
        )
        self.veo(
            'Digita un nota númerica: '
            'Su calificación es: F\n'
        )
