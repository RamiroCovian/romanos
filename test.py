import unittest
from romanos import RomanNumber


class RomanosTest(unittest.TestCase):
    def test_crear_numero_romano_desde_entero(self):
        numero = RomanNumber(1)
        self.assertEqual(numero.valor, 1)
        self.assertEqual(numero.cadena, "I")
        numero = RomanNumber(1745)
        self.assertEqual(numero.valor, 1745)
        self.assertEqual(numero.cadena, "MDCCXLV")

    def test_crear_numero_desde_cadena(self):
        numero = RomanNumber("I")
        self.assertEqual(numero.cadena, "I")
        self.assertEqual(numero.valor, 1)
        numero = RomanNumber("MDCCXLV")
        self.assertEqual(numero.cadena, "MDCCXLV")
        self.assertEqual(numero.valor, 1745)

    def test_numero_romano_tiene_representacion_de_cadena(self):
        numero = RomanNumber(1745)
        self.assertEqual(str(numero), "MDCCXLV")

    def test_comprobar_igualdad(self):
        numeroUno = RomanNumber(1)
        otro_numeroUno = RomanNumber(1)
        numeroDos = RomanNumber(2)
        self.assertEqual(numeroUno, otro_numeroUno)
        self.assertNotEqual(numeroUno, numeroDos)
        self.assertNotEqual(otro_numeroUno, numeroDos)

    def test_suma(self):
        numeroUno = RomanNumber(10)
        numeroDos = RomanNumber(5)
        numeroTres = RomanNumber("VII")
        self.assertEqual(numeroUno + numeroDos, 15)
        self.assertEqual(numeroUno + numeroTres, 17)
        self.assertEqual(numeroUno + 4, 14)
        self.assertEqual(numeroUno + "III", 13)
        self.asse


unittest.main()
