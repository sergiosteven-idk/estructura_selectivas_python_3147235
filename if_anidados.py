'''
if aninados:
    if dentro de otros if

syntax:
if condition:
    if condition:
        print("mensaje1")
        if condition2
        print:("mensaje2")
         if condition3
        print:("mensaje3")
         if condition4
        print:("mensaje4")
         if condition5
        print:("mensaje5")

else: 
    print("mensaje5")

no confundir con elif (if en cascada)

'''
#Ejmplo 1:
# Modifique el ejercicio de la edad
# para las siguientes condiciones
# si es mayor de 18 años
# pero no tiene documento, no puede votar
# de lo contrario si puede votar
# si es menor de 18 años
# no puede votar
# utilize estructura if


edad = int(input("ingrese su edad: "))
if edad >= 18:
    documento = input ("tiene documento? (SI/NO): ")
    if documento == "si":
        print("Puede votar , todo en regla")
    else:
        print("No puede votar, no tiene documento")
else:
    print("No puede votar , perdon")