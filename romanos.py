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

    millares = ["", "M", "MM", "MMM"]
    centenas = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    decenas = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    unidades = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    # descomposicion en millares, decenas, centenas y unidades
    millar = numero // 1000
    resto = numero % 1000

    centena = resto // 100
    resto = resto % 100

    decena = resto // 10
    resto = resto % 10

    unidad = resto
    # RETO: podemos simplificar el proceso en lugar dde copiar/pegar las operaciones de division y modulo?

    # mapear el cociente (diccionario)
    # si hay resto, repetimos....
    romano = millares[millar] + centenas[centena] + decenas[decena] + unidades[unidad]
    print([romano])

    return "TODO: convertir a romano"


print(convertir_a_romano(56))
print(convertir_a_romano("lo que quiera"))
print(convertir_a_romano(0))
print(convertir_a_romano(4000))
print(convertir_a_romano(-6))
print(convertir_a_romano(3999))
print(convertir_a_romano({}))
print(convertir_a_romano([]))
