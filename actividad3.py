'''
actividad 3:
Elabore un programa que permita calcular el salarion despues
netp de un empleado,
despues de descontar los
descuentos por conceptos:
salud, pension, ARL
1. el programa debe solicitar
el tipo de empleado:
a - contrato a termino indefinido
b - contrato por prestacion de servicio
c - contrato de aprendiaje
d - contrato por jornal(freelance)

-> para el caso de jornal
- se debe solicitar numero de horas trabajadas
-y el valor a pagar por hora    
-y el total del se calcula
-de multiplicar el numero de horas
-por el valor a pagar por horas   
'''

contrato = input("ingrese el tipo de de contrato: ")
#inicializacion
salario_neto= 0
if contrato == "a":
    print("eligio: contrato a termino indefinido:")
elif contrato == "b":
    print("eligio: contrato por prenstacion:")
elif contrato == "c":
    print("eligio: contrato de aprendizaje:")
    salario_minimo = int (input("ingrese valor del salario  minimo:"))
    salario_neto = salario_minimo - (salario_minimo * 0.25)
elif contrato == "d" :
    print("eligio jornal:") 
    #variable local:
    #variable que solo se piede utilizar
    #en un bloque de codigo
    numero_horas = (input("ingrese un numro de horas:"))
    valor_hora = int (input("ingrese valor por hora a pagar:"))
    salario_neto = numero_horas * numero_horas
else:
    print("tipo de contrato no existente")
print("el salario neto es:" , salario_neto)     
print("fin del programa")  


        
