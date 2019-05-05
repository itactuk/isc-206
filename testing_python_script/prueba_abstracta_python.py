import io
import sys
import time
import unittest
import runpy
from threading import Thread


class MiHilo(Thread):
    def __init__(self, nombre_modulo):
        self.nombre_modulo = nombre_modulo
        super().__init__()

    def run(self):
        runpy.run_module(mod_name=self.nombre_modulo)


class MiPruebaAbstracta(unittest.TestCase):

    def setUp(self):
        self.ConfigVars()
        # Store the reference, in case you want to show things again in standard output
        self.old_stdout = sys.stdout
        # This variable will store everything that is sent to the standard output
        self.result = io.StringIO()
        self.h = MiHilo(self.nombre_modulo[5:])
        self.h.start()
        sys.stdout = self.result

    def ConfigVars(self):
        pass

    def tearDown(self):
        # Redirect again the std output to screen
        sys.stdout = self.old_stdout

    def entro(self, string_val):
        for i in range(12):
            string_val += '\n'
        sys.stdin = io.StringIO(string_val)
        time.sleep(0.05)

    def veo(self, str_val):
        result_string = self.result.getvalue()
        self.assertEqual(result_string, str_val)
