from romanosBis import *

# print(convertir_a_romano(-1))  # Error
# print(convertir_a_romano(0))  # Error
# print(convertir_a_romano(4000))  # Error
# print(convertir_a_romano(5645))  # Error
# print(convertir_a_romano("ds"))  # Error
# print(convertir_a_romano(56))  # None
# print(convertir_a_romano(3999))  # None
# print(convertir_a_romano(1137))  # None

prueba = ["A", "", 3, "IX", "MCXXIII", "IC"]
for x in prueba:
    print(romano_a_entero(x))
