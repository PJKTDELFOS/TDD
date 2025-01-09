try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                './src'
            )
        )
    )
except:
    raise

import unittest
from calculadora import  soma

class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_igual_10(self):
        self.assertEqual(soma(2,3), 5)
    def test_soma_5_negativo_e_5_igual_0(self):
        self.assertEqual(soma(-5,5), 0)

    def test_soma_varias_entradas(self):
        x_y_saidas=(
            (10,10,20),
            (1, 2, 3),
            (10, 10, 50),
            (1, 1, 2),
            (101, 10, 120),
            (11, 10, 21)
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saidas=x_y_saidas):
                x,y,saida = x_y_saida
                self.assertEqual(soma(x,y), saida)

    def test_soma_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(TypeError):#assertRaises com TypeError para teste de tipagem
            soma('11',2)

if __name__=='__main__':
    unittest.main(verbosity=2)