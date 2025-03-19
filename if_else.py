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

edad=20
documento = False
if edad >= 18 and documento==True:
    print("Usted es mayor de edad")
    print("Puede votar")
else:
    print("Usted es menor de edad")
    print("o")
    print("No puede votar")
print("fin del programa")