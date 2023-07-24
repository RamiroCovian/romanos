"""
Escribir una funcion en python que sea capaz de recibir un numero entre 0 y 3999
y devuelva el numero como una cadena en su representacion en numero romano.

*Restriccion*
El numero 0 devolvera una cadena vacia.
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
    elif type(numero) == int:
        return "TODO: convertir a romano"

    # if not isinstance(numero, int):
    #     return "ERROR: debes ingresar un valor numerico"
    # return "TODO: convertir a romano"


# def comprobar_entero(numero):
#     try:
#         num = int(numero)
#         return "TODO: convertir a romano"
#     except ValueError:
#         print(f"Error: debes introducion un valor entero ({numero})")
#         return ""


print(convertir_a_romano(56))
print(convertir_a_romano("lo que quiera"))
print(convertir_a_romano(51.3))
print(convertir_a_romano({}))
print(convertir_a_romano([]))
# print("---" * 21)
# print(comprobar_entero(56))
# print(comprobar_entero("lo que quiera"))
# print(comprobar_entero(51.3))
# print(comprobar_entero({}))
# print(comprobar_entero([]))
