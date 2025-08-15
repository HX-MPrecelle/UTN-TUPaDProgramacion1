###############
# Ejercicio 1
###############

print("Hoa Mundo!")

###############
# Ejercicio 2
###############

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

###############
# Ejercicio 3
###############

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
lugar_de_residencia = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_de_residencia}")

###############
# Ejercicio 4
###############

radio = float(input("Ingrese el radio de un circulo: "))
pi = 3.141592653589793
area = pi * radio ** 2
perimetro = 2 * pi * radio

print(f"El area del circulo es {area} y el perimetro es {perimetro}")

###############
# Ejercicio 5
###############

segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600

print(f"La cantidad de segundos ingresada equivale a {horas} horas")

###############
# Ejercicio 6
###############

numero = int(input("Ingrese un numero: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

###############
# Ejercicio 7
###############

numero1 = int(input("Ingrese un numero distinto de 0: "))
numero2 = int(input("Ingrese otro numero distinto de 0: "))

if numero1 == 0 or numero2 == 0:
    print("Error: los numeros ingresados son 0")
else:
    print(f"La suma de {numero1} y {numero2} es {numero1 + numero2}")
    print(f"La division de {numero1} y {numero2} es {numero1 / numero2}")
    print(f"La multiplicacion de {numero1} y {numero2} es {numero1 * numero2}")
    print(f"La resta de {numero1} y {numero2} es {numero1 - numero2}")

###############
# Ejercicio 8
###############

altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))
imc = peso / (altura ** 2)

print(f"Su indice de masa corporal es {imc}")

###############
# Ejercicio 9
###############

temperatura = float(input("Ingrese una temperatura en grados celsius: "))
fahrenheit = (temperatura * 9/5) + 32

print(f"La temperatura ingresada equivale a {fahrenheit} grados fahrenheit")

###############
# Ejercicio 10
###############

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
numero3 = int(input("Ingrese otro numero: "))

promedio = (numero1 + numero2 + numero3) / 3

print(f"El promedio de los tres numeros ingresados es {promedio}")