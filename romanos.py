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
"""


def convertir_a_romano(numero):
    if type(numero) != int:
        return "ERROR: debes ingresar un valor numerico"
    # validar el valor del numero
    if not (0 < numero < 4000):
        return f"Error: El numero debe estar entre 1 y 3999 ({numero})"
    return "TODO: convertir a romano"


print(convertir_a_romano(56))
print(convertir_a_romano("lo que quiera"))
print(convertir_a_romano(0))
print(convertir_a_romano(4000))
print(convertir_a_romano(-6))
print(convertir_a_romano(3999))
print(convertir_a_romano({}))
print(convertir_a_romano([]))
