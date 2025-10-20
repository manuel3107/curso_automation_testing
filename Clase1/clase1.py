#Actvidad 1: Escribir un programa que solicite al usuario su nombre, edad y profesión, y luego imprima un mensaje personalizado con esa información.
nombre = input("Cual es tu nombre? ")
edad = input("Cual es tu edad? ")
profesion = input("Cual es tu profesion? ")
print("Hola " + nombre + ", tienes " + edad + " años y tu profesion es " + profesion)

#Actividad 2: crear un bucle que imprima los 10 primeros numeros pares.
contador = 0
for i in range(0, 21):
    if i % 2 == 0:
        contador += 1
    print(f"hay {contador} numeros pares:")