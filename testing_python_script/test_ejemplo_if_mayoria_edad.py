
from testing_python_script.prueba_abstracta_python import MiPruebaAbstracta


class MisPruebas(MiPruebaAbstracta):

    def ConfigVars(self):
        self.nombre_modulo = __name__

    # todas las pruebas tiene que comenzar con test
    def test_es_mayor(self):
        self.entro(
            '21\n'
        )
        self.veo(
            'Digite edad: \n'
            'Es mayor\n'
        )

    def test_tiene_18(self):
        self.entro(
            '18\n'
        )
        self.veo(
            'Digite edad: \n'
            'Es mayor\n'
        )

    def test_es_menor(self):
        self.entro(
            '17\n'
        )
        self.veo(
            'Digite edad: \n'
            'Es menor\n'
        )