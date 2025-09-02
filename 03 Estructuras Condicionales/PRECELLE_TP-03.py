# Ejercicio 1
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Usted es mayor de edad")

# Ejercicio 2
nota = float(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# Ejercicio 3
numero = int(input("Ingrese un numero par: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# Ejercicio 4
numero = int(input("Ingrese su edad: "))

if numero < 12:
    print("Usted es un niño")
elif numero >= 12 and numero < 18:
    print("Usted es un adolescente")
elif numero >= 18 and numero < 30:
    print("Usted es un adulto joven")
else:
    print("Usted es un adulto")

# Ejercicio 5
contraseña = input("Ingrese su contraseña: ")

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
promedio = mean(numeros_aleatorios)

if promedio > mediana and mediana > moda:
    print("Hay sesgo positivo")
elif promedio < mediana and mediana < moda:
    print("Hay sesgo negativo")
else:
    print("No hay sesgo")

# Ejercicio 7
palabra = input("Ingrese una frase o palabra: ")

vocales = ['a', 'e', 'i', 'o', 'u']

if palabra[-1] in vocales:
    print(palabra + "!")
else:
    print(palabra)

# Ejercicio 8
nombre = input("Ingrese su nombre: ")

opcion = int(input("Ingrese el numero de la opcion que desee: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())

# Ejercicio 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte")
else:
    print("Extremo")

# Ejercicio 10
hemisferio = input("Ingrese en que hemisferio se encuentra (N/S): ")
mes = input("Ingrese el mes del año: ")
dia = input("Ingrese el dia del mes: ")

if hemisferio == "N":
    if mes == "12" and dia >= 21 or mes == "1" or mes == "2" or mes == "3" and dia <= 20:
        print("Invierno")
    elif mes == "3" and dia >= 21 or mes == "4" or mes == "5" or mes == "6" and dia <= 20:
        print("Primavera")
    elif mes == "6" and dia >= 21 or mes == "7" or mes == "8" or mes == "9" and dia <= 20:
        print("Verano")
    else:
        print("Otoño")
else:
    if mes == "12" and dia >= 21 or mes == "1" or mes == "2" or mes == "3" and dia <= 20:
        print("Verano")
    elif mes == "3" and dia >= 21 or mes == "4" or mes == "5" or mes == "6" and dia <= 20:
        print("Otoño")
    elif mes == "6" and dia >= 21 or mes == "7" or mes == "8" or mes == "9" and dia <= 20:
        print("Invierno")
    else:
        print("Primavera")

