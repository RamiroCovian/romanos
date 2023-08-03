import unittest
from romanos_funcional import romano_a_entero, convertir_a_romano


class RomanosTest(unittest.TestCase):
    def test_unidades(self):
        self.assertEqual(romano_a_entero("I"), 1)
        self.assertEqual(romano_a_entero("V"), 5)
        self.assertEqual(romano_a_entero("X"), 10)
        self.assertEqual(romano_a_entero("L"), 50)
        self.assertEqual(romano_a_entero("C"), 100)
        self.assertEqual(romano_a_entero("D"), 500)
        self.assertEqual(romano_a_entero("M"), 1000)

    def test_numeros_basicos(self):
        self.assertEqual(romano_a_entero("II"), 2)
        self.assertEqual(romano_a_entero("IV"), 4)
        self.assertEqual(romano_a_entero("IX"), 9)
        self.assertEqual(romano_a_entero("XL"), 40)
        self.assertEqual(romano_a_entero("CCV"), 205)
        self.assertEqual(romano_a_entero("MCXXIII"), 1123)

    def test_no_resta_mas_de_un_orden_de_magnitud(self):
        self.assertRaises(ValueError, romano_a_entero, "IC")
        self.assertRaises(ValueError, romano_a_entero, "XM")

    def test_no_restas_consecutivas(self):
        """
        IIV
        """
        self.assertRaises(ValueError, romano_a_entero, "IIV")
        self.assertRaises(ValueError, romano_a_entero, "IVX")

    def test_no_mas_de_tres_simbolos_consecutivos(self):
        self.assertRaises(ValueError, romano_a_entero, "IIII")
        self.assertRaises(ValueError, romano_a_entero, "XIIII")
        self.assertRaises(ValueError, romano_a_entero, "CCCC")

    def test_no_resta_multiplos_de_cinco(self):
        self.assertRaises(ValueError, romano_a_entero, "VX")
        self.assertRaises(ValueError, romano_a_entero, "VXX")
        self.assertRaises(ValueError, romano_a_entero, "LC")
        self.assertRaises(ValueError, romano_a_entero, "DM")

    def test_es_cadena(self):
        self.assertIsInstance("II", str)
        self.assertIsInstance("XI", str)

    # def test_letras_no_validas(self):
    #     self.assertIn(10, )

    # self.assertRaises(TypeError, romano_a_entero, "II2")
    # self.assertRaises(TypeError, romano_a_entero, int)


# TODO: crear un caso de uso para comprobar que el parametro es una cadena
# TODO: comprobar que el numero romano no tiene letras NO VALIDAS
# TODO: resolver los dos casos de test comentados arriba (resta multiplo de 5(con %5==0 :)) y otro caso)

unittest.main()
