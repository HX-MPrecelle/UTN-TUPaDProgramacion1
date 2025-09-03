# Ejercicio 1
for i in range(101):
    print(i)

# Ejercicio 2
num = int(input("Ingrese un número entero: "))
contador = 0
numero_temp = num
while numero_temp > 0:
    contador += 1
    numero_temp = numero_temp // 10
print("Cantidad de dígitos:", contador)

# Ejercicio 3
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
suma = 0
for i in range(min(a, b) + 1, max(a, b)):
    suma += i
print("La suma de los números comprendidos entre", a, "y", b, "es:", suma)

# Ejercicio 4
total = 0
while True:
    n = int(input("Ingrese un número entero (0 para detenerse): "))
    if n == 0:
        break
    total += n
print("La suma total es:", total)

# Ejercicio 5
import random
numero = random.randint(0, 9)
intentos = 0
while True:
    guess = int(input("Adivina el número (0-9): "))
    intentos += 1
    if guess == numero:
        print("¡Correcto! El número era", numero)
        break
print("Número de intentos:", intentos)

# Ejercicio 6
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

# Ejercicio 7
n = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(n + 1):
    suma += i
print("La suma de los números desde 0 hasta", n, "es:", suma)

# Ejercicio 8
cantidad = 100
pares = impares = negativos = positivos = 0
for _ in range(cantidad):
    num = int(input("Ingrese un número entero: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num < 0:
        negativos += 1
    elif num > 0:
        positivos += 1
print("Pares:", pares)
print("Impares:", impares)
print("Negativos:", negativos)
print("Positivos:", positivos)

# Ejercicio 9
cantidad = 100
suma = 0
for _ in range(cantidad):
    num = int(input("Ingrese un número entero: "))
    suma += num
media = suma / cantidad
print("La media de los números ingresados es:", media)

# Ejercicio 10
num = int(input("Ingrese un número: "))
numero_original = num
numero_invertido = 0
while num > 0:
    digito = num % 10
    numero_invertido = numero_invertido * 10 + digito
    num = num // 10
print("Número invertido:", numero_invertido)
