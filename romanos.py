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
    if type(numero) != int:
        return "ERROR: debes ingresar un valor numerico"
    # validar el valor del numero
    if not (0 < numero < 4000):
        return f"Error: El numero debe estar entre 1 y 3999 ({numero})"

    # descomposicion en millares, decenas, centenas y unidades
    conversores = [
        ["", "M", "MM", "MMM"],
        ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
        ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
        ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
    ]
    divisores = [1000, 100, 10, 1]

    resultado = ""
    contador = 0

    for divisor in divisores:
        cociente = numero // divisor
        numero = numero % divisor
        resultado = resultado + conversores[contador][cociente]
        contador = contador + 1

    return resultado


def romano_a_entero(romano):
    """
    MCXXIII +> 1123

        -recorrer la cadena de entrada (romano) de izquierda a derecha
        -para cada letra, obtenemos su valor como numero decimal
        -vamos sumando los valores obtenidos
        -cuando no quedan letras, el valor acumulado de la suma es el resultado

        - buble for para recorrar las letras
        PARA CADA LETRA:
            -validar que la letra es validas como numero romano( I, V, X, L, C, D, M)
    """

    digitos_romanos = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    if not isinstance(romano, str):
        return "ERROR: tiene que ser un numero romano en formato cadena de texto"

    resultado = 0

    for letra in romano:
        if letra not in digitos_romanos:
            return f"ERROR: {letra} no es un digito romano valido (I, V, X, L, C, D, M)"
        resultado = resultado + digitos_romanos.get(letra)

    return resultado


errores = ["A", "", 3, ["X", "X", "I"]]
pruebas = ["I", "MCXXIII", "VIII", "LVI"]
for valor in pruebas:
    print(romano_a_entero(valor))
