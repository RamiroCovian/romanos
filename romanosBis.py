"""
Escribir una funcion en python que sea capaz de recibir un numero entre 0 y 3999
y devuelva el numero como una cadena en su representacion en numero romano.

*Restriccion*
El numero 0 no es un numero romano valido.
1. definir una funcion
2. La funcion recibe un parametro
3. El parametro es numerico
    3.1 No puede ser menor que 0
    3.2 No puede ser mayor que 3999
4. Devolver un cadena

I  ---> 1
V  ---> 5
X  ---> 10
L  ---> 50
C  ---> 100
D  ---> 500
M  ---> 1000

1137 ==> MCXXXVII
||||_____________ VII ---- 7 * 10⁰
|||______________ XXX ---- 3 * 10¹
||_______________ C   ---- 1 * 10²
|________________ M   ---- 1 * 10³

1M 1C 3D 7U

1137 / 1000 = 1 ----- diccionario: M
1137 % 1000 = 137

137 / 100 = 1 ------- diccionario: C
137 % 100 = 37

37 / 10 = 3 --------- diccionario: XXX
37 % 10 = 7 

7 / 1 = 7 ----------- diccionario: VII
7 % 1 = 0
"""


def convertir_a_romano(numero):
    if not isinstance(numero, int):
        return "ERROR: Debe ingresar un valor numerico "
    if not (0 < numero < 4000):
        return f"ERROR: Debe ingresar un valor entre 0 y 3999 ({numero})"

    CONVERSORES = [
        ["", "M", "MM", "MMM"],
        ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
        ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
        ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
    ]

    DIVISORES = [1000, 100, 10, 1]

    resultado = ""
    contador = 0

    for divisor in DIVISORES:
        cociente = numero // divisor
        numero = numero % divisor
        resultado = resultado + CONVERSORES[contador][cociente]
        contador += 1

    return resultado


def romano_a_entero(romano):
    """
    MCXXIII => 1123

        - recorrer la cadena de entrada (romano) de izquierda a derecha
        - para cada letra, obtenemos su valor como número decimal
        - vamos sumando los valores obtenidos
        - cuando no quedan letras, el valor acumulado de la suma es el resultado

        - bucle for para recorrer las letras
        - Para cada letra:
            - validar que la letra es válidas como número romano (I, V, X, L, C, D, M)

    IV / VI  --->  comparar el valor de los dos dígitos

    IX, DCIV

    letra
    D           --- 500
    C           --- 100 + 500 = 600
    I           --- 1 + 600 = 601
    V           --- [601 - 1] + (5 - 1) = 604
    """

    DIGITOS_ROMANOS = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    if not isinstance(romano, str):
        return f"ERROR: {romano} no es una cadena de texto valida"

    resultado = 0
    anterior = 0

    for letra in romano:
        if not letra in DIGITOS_ROMANOS:
            return (
                f"ERROR: {romano} no es un digito romano valido (I, V, X, L, C, D, M)"
            )
        actual = DIGITOS_ROMANOS.get(letra)

        if anterior < actual:
            if anterior > 0 and len(str(actual)) - len(str(anterior)) > 1:
                return f"ERROR: resta no es posible (ant:{anterior}, act:{actual})"
            resultado = resultado - anterior
            resultado = resultado + (actual - anterior)
        else:
            resultado = resultado + actual
        anterior = actual

    return resultado
