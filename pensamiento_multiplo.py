anterior = 10
actual = 50

multiplo_ant = anterior % 5
print(f"MULTIPLO ANTERIOR {multiplo_ant}")
multiplo_act = actual % 5
print(f"MULTIPLO ACTUAL {multiplo_act}")

multiplo = anterior % actual
print(multiplo)  #  = 5 NO LO PERMITE


multiplos_de_5 = [1, 10, 100, 1000]
if anterior < actual and multiplo in multiplos_de_5:
    print("PERMITIDO CONTINUAR")
else:
    print("ERROR TIENE QUE LANZAR MULTIPLO DE 5")
# if multiplo in multiplos_de_5:
#     print("PERMITIDO CONTINUAR")
#  and multiplo < 5
