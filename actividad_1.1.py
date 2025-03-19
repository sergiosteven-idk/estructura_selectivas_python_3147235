temperatura_motor= int(input("ingrese la temperatura del motor: "))
motor_encendido= input("El motor esta encendido? (SI/NO): ")

if temperatura_motor >= 80 and motor_encendido=="SI":
    print("El motor debe apagagarse")
else:
    print("El motor no debe apagarse")
    print("O no esta encendido")
