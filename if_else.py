'''
if else:
sirve para determinar 2 caminos de ejecucion 
basados en la evaluaion de una condicional

sintaxis:

    instruccion1
    instruccion2
else:

     instruccion3
     instruccion4
    
     
'''

#Ejemplo:
# elabore un programa en python
# q determine si una persona
# es mayor o menor de edad
# por lo tanto puede votar

edad= int(input("ingrese su edad: "))
documento = input("tiene documento (SI/NO): ")
if edad >= 18 and documento==SI:
    print("Usted es mayor de edad")
    print("Puede votar")
else: 
    print("Usted es menor de edad")
    print("o")
    print("No puede votar")
print("fin del programa")