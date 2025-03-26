'''
Actividad 3:
Elabore un programa que permita calcular el salario neto de un empleado, despues descontar los 
descuentos por conceptos de:  
Salud, pensón , ARL
1. El progama debe solicitar el tipo de empleado:
a- contrato a termino indefinido
b- Contrato por prestacion de servicio
c- Contrato de aprendizajo
d- Contrato por jornada  (Freelance)
=> Para el caso de jornada:
Se debe solicitar numero de horas trabajadas el valor a pagar por hora
El total del salario se calcula  de multiplicar el numero de horas por el valor 
a pagar por horas
=> Para el caso de restacion de servicio
Se debe solicitar:
-El valor del contrato
-El numero de meses del contrato
-la antiguedad del empleado(años)
El salario neto se calcula de la siguiente manera:
1. - Dividir el valor del contrato por el numero de meses
2. -Restar el 15% del valor del salario mensual 
3. -Restar el 10% del salario mensual, por concepto de pensión
4. -Si el empleado tiene una antiguedad superior a 10 años: se le dara una bodificiacion del 5% 
sobre el salario mensual

=> Para el caso de contrato de a termino indefinido:
-antiguedad(años)
-grado o escalafon (1-5)
-el salario minimo se calcula de la siguiente manera:
-grado 1: 1.5 SM
-grado 2: 1,7 SM
-grado 3: 2,0 SM
-grado 4: 2,5 SM
-grado 5: 3,0 SM
la bonificacion estara de acorde a los siguinetes rangos segun la antigueda:
-Entre 1 y 5 años: 1% del salario minimo
-Entre 6 y 10 años: 2% del salario minimo
-Superior a 10 años: 3% del salario minimo
Para este caso, los decuentos de ley son:
-25% por concepto de salud
-22% por concepto de pensión
-0.1% por concepto de ARL
'''
#Inicializar variables, dar valor inicial de una variable asi no se utilice en ese momento
contrato = input ("Ingrese el tipo de contrato:")
salario_neto= 0

if contrato == "a":
    print ("Eligio: contrato a termino indefinido")
    antiguedad = int(input("Ingrese la antiguedad del empleado (Año):"))
    grado = int(input("Ingrese el grado del empleado:"))
    salario_neto= int(input("Ingrese el salario neto del empleado:"))
    salario_minimo = int(input("Ingrese el salario minimo:"))
    if grado == 1:
        salario_neto = salario_minimo*1.5
    elif grado == 2:
        salario_neto = salario_minimo*1.7
    elif grado == 3:
        salario_neto = salario_minimo*2.0
    elif grado == 4:
        salario_neto = salario_minimo*2.5
    elif grado == 5:
        salario_neto = salario_minimo*3.0
    if antiguedad >= 1 and antiguedad <= 5:
        salario_neto = salario_neto + (salario_minimo*0.01)
    elif antiguedad >= 6 and antiguedad <= 10:
        salario_neto = salario_neto + (salario_minimo*0.02)
    elif antiguedad >= 10:
        salario_neto = salario_neto + (salario_minimo*0.03)
    salario_neto = salario_neto - (salario_neto*0.25) - (salario_neto*0.22) - (salario_neto*0.001)


elif contrato =="b":
    print ("Eligio contrato  por prestación de servicio")
    valor_contrato = int(input("Ingrese el valor del contrato:"))
    numero_meses = int(input("Ingrese el numero de meses del contrato:"))
    antiguedad = int(input("Ingrese la antiguedad del empleado:"))
    salario_mensual = valor_contrato/numero_meses
    salario_neto = salario_mensual - (salario_mensual*0.15) - (salario_mensual*0.10)
    if antiguedad >= 10:
        salario_neto = salario_neto + (salario_neto*0.05)
    
elif contrato =="c":
    print ("Eligio:contrato de aprendizaje")
    salario_minimo= int(input("Ingrese el valor del salario minimo"))
    salario_neto=  salario_minimo-(salario_minimo*0.25)
    
elif contrato == "d":
    print ("Eligio: Contrato por jornada")
    valor_neto =0
    numero_horas = int(input("Ingrese su numero de horas:"))
    valor_hora =int(input("Ingrese el valor a pagar por hora:"))
    salario_neto =  numero_horas* valor_neto
    

else:
 print ("No hay ningun tipo de contraro, colcoa uno si es a,b,c o d ")
print ("El salario neto es:",salario_neto)
print ("Fin de programa")
