# =============================================================================
# EJERCICIO 1
# =============================================================================

# Crear lista con las notas de 10 estudiantes
notas = [8, 7, 9, 6, 8, 7, 9, 8, 6, 7]

# Mostrar la lista completa
print("Lista de notas de los 10 estudiantes:")
for i in range(len(notas)):
    print(f"Estudiante {i+1}: {notas[i]}")

# Calcular y mostrar el promedio
promedio = sum(notas) / len(notas)
print(f"\nPromedio de las notas: {promedio}")

# Indicar la nota más alta y la más baja
nota_maxima = max(notas)
nota_minima = min(notas)
print(f"Nota más alta: {nota_maxima}")
print(f"Nota más baja: {nota_minima}")

# =============================================================================
# EJERCICIO 2
# =============================================================================

# Pedir al usuario que cargue 5 productos en una lista
productos = []
print("\nIngrese 5 productos:")
for i in range(5):
    producto = input(f"Producto {i+1}: ")
    productos.append(producto)

# Mostrar la lista ordenada alfabéticamente
productos_ordenados = sorted(productos)
print("\nLista de productos ordenada alfabéticamente:")
for producto in productos_ordenados:
    print(f"- {producto}")

# Preguntar al usuario qué producto desea eliminar
print("\nProductos disponibles para eliminar:")
for i, producto in enumerate(productos):
    print(f"{i+1}. {producto}")

indice_eliminar = int(input("Ingrese el número del producto a eliminar: ")) - 1
producto_eliminado = productos.pop(indice_eliminar)

# Mostrar la lista actualizada
print(f"\nSe eliminó: {producto_eliminado}")
print("Lista actualizada:")
for producto in productos:
    print(f"- {producto}")

# =============================================================================
# EJERCICIO 3
# =============================================================================

import random

# Generar lista con 15 números enteros al azar entre 1 y 100
numeros_aleatorios = []
for i in range(15):
    numero = random.randint(1, 100)
    numeros_aleatorios.append(numero)

print("\nLista de 15 números aleatorios:")
for numero in numeros_aleatorios:
    print(numero, end=" ")
print()

# Crear lista con los pares y otra con los impares
numeros_pares = []
numeros_impares = []

for numero in numeros_aleatorios:
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

# Mostrar cuántos números tiene cada lista
print(f"\nNúmeros pares ({len(numeros_pares)} elementos):")
for numero in numeros_pares:
    print(numero, end=" ")
print()

print(f"\nNúmeros impares ({len(numeros_impares)} elementos):")
for numero in numeros_impares:
    print(numero, end=" ")
print()

# =============================================================================
# EJERCICIO 4
# =============================================================================

# Lista con valores repetidos
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

print("\nLista original con repetidos:")
for elemento in datos:
    print(elemento, end=" ")
print()

# Crear nueva lista sin elementos repetidos
lista_sin_repetidos = []
for elemento in datos:
    if elemento not in lista_sin_repetidos:
        lista_sin_repetidos.append(elemento)

# Mostrar el resultado
print("\nLista sin elementos repetidos:")
for elemento in lista_sin_repetidos:
    print(elemento, end=" ")
print()

# =============================================================================
# EJERCICIO 5
# =============================================================================

# Crear lista con los nombres de 8 estudiantes presentes en clase
estudiantes = ["Ana", "Carlos", "María", "Pedro", "Laura", "Juan", "Sofia", "Diego"]

print("\nLista de estudiantes presentes en clase:")
for i, estudiante in enumerate(estudiantes):
    print(f"{i+1}. {estudiante}")

# Preguntar al usuario qué acción desea realizar
print("\n¿Qué desea hacer?")
print("1. Agregar un nuevo estudiante")
print("2. Eliminar un estudiante existente")
opcion = int(input("Ingrese su opción (1 o 2): "))

if opcion == 1:
    nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo_estudiante)
    print(f"Se agregó: {nuevo_estudiante}")
elif opcion == 2:
    print("\nEstudiantes disponibles para eliminar:")
    for i, estudiante in enumerate(estudiantes):
        print(f"{i+1}. {estudiante}")
    indice_eliminar = int(input("Ingrese el número del estudiante a eliminar: ")) - 1
    estudiante_eliminado = estudiantes.pop(indice_eliminar)
    print(f"Se eliminó: {estudiante_eliminado}")

# Mostrar la lista final actualizada
print("\nLista final de estudiantes:")
for i, estudiante in enumerate(estudiantes):
    print(f"{i+1}. {estudiante}")

# =============================================================================
# EJERCICIO 6
# =============================================================================

# Lista con 7 números
numeros = [1, 2, 3, 4, 5, 6, 7]

print("\nLista original:")
for numero in numeros:
    print(numero, end=" ")
print()

# Rotar todos los elementos una posición hacia la derecha
ultimo_elemento = numeros.pop()
numeros.insert(0, ultimo_elemento)

print("Lista rotada una posición hacia la derecha:")
for numero in numeros:
    print(numero, end=" ")
print()

# =============================================================================
# EJERCICIO 7
# =============================================================================

# Crear matriz 7x2 con temperaturas mínimas y máximas de una semana
temperaturas = [
    [5, 15],   # Lunes
    [3, 12],   # Martes
    [7, 18],   # Miércoles
    [4, 14],   # Jueves
    [6, 16],   # Viernes
    [8, 20],   # Sábado
    [9, 22]    # Domingo
]

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

print("\nTemperaturas de la semana:")
for i in range(len(temperaturas)):
    print(f"{dias[i]}: Mínima {temperaturas[i][0]}°C, Máxima {temperaturas[i][1]}°C")

# Calcular promedio de las mínimas y el de las máximas
minimas = [fila[0] for fila in temperaturas]
maximas = [fila[1] for fila in temperaturas]

promedio_minimas = sum(minimas) / len(minimas)
promedio_maximas = sum(maximas) / len(maximas)

print(f"\nPromedio de temperaturas mínimas: {promedio_minimas}°C")
print(f"Promedio de temperaturas máximas: {promedio_maximas}°C")

# Mostrar en qué día se registró la mayor amplitud térmica
amplitudes = []
for i in range(len(temperaturas)):
    amplitud = temperaturas[i][1] - temperaturas[i][0]
    amplitudes.append(amplitud)

mayor_amplitud = max(amplitudes)
dia_mayor_amplitud = amplitudes.index(mayor_amplitud)

print(f"Mayor amplitud térmica: {mayor_amplitud}°C el día {dias[dia_mayor_amplitud]}")

# =============================================================================
# EJERCICIO 8
# =============================================================================

# Crear matriz con las notas de 5 estudiantes en 3 materias
notas_materias = [
    [8, 7, 9],  # Estudiante 1
    [6, 8, 7],  # Estudiante 2
    [9, 9, 8],  # Estudiante 3
    [7, 6, 8],  # Estudiante 4
    [8, 8, 9]   # Estudiante 5
]

materias = ["Matemática", "Física", "Química"]

print("\nNotas de los estudiantes:")
for i in range(len(notas_materias)):
    print(f"Estudiante {i+1}: ", end="")
    for j in range(len(notas_materias[i])):
        print(f"{materias[j]}={notas_materias[i][j]}", end=" ")
    print()

# Mostrar el promedio de cada estudiante
print("\nPromedio de cada estudiante:")
for i in range(len(notas_materias)):
    promedio_estudiante = sum(notas_materias[i]) / len(notas_materias[i])
    print(f"Estudiante {i+1}: {promedio_estudiante}")

# Mostrar el promedio de cada materia
print("\nPromedio de cada materia:")
for j in range(len(materias)):
    notas_materia = [notas_materias[i][j] for i in range(len(notas_materias))]
    promedio_materia = sum(notas_materia) / len(notas_materia)
    print(f"{materias[j]}: {promedio_materia}")

# =============================================================================
# EJERCICIO 9
# =============================================================================

# Inicializar tablero 3x3 con guiones
tablero = []
for i in range(3):
    fila = []
    for j in range(3):
        fila.append("-")
    tablero.append(fila)

def mostrar_tablero():
    print("\nTablero actual:")
    print("  0 1 2")
    for i in range(3):
        print(f"{i} ", end="")
        for j in range(3):
            print(tablero[i][j], end=" ")
        print()

# Mostrar tablero inicial
mostrar_tablero()

# Permitir que dos jugadores ingresen posiciones
jugador_actual = "X"
for turno in range(9):  # Máximo 9 turnos
    print(f"\nTurno del jugador {jugador_actual}")
    fila = int(input("Ingrese fila (0-2): "))
    columna = int(input("Ingrese columna (0-2): "))
    
    # Verificar que la casilla esté vacía
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador_actual
        mostrar_tablero()
        
        # Cambiar de jugador
        if jugador_actual == "X":
            jugador_actual = "O"
        else:
            jugador_actual = "X"
    else:
        print("Casilla ocupada, intente de nuevo")
        turno -= 1  # Repetir el turno

print("\n¡Juego terminado!")

# =============================================================================
# EJERCICIO 10
# =============================================================================

# Matriz 4x7 con ventas de 4 productos durante 7 días
ventas = [
    [10, 15, 12, 8, 20, 18, 14],   # Producto 1
    [5, 8, 6, 10, 12, 9, 7],       # Producto 2
    [20, 25, 22, 18, 30, 28, 24],  # Producto 3
    [12, 10, 15, 20, 16, 14, 18]   # Producto 4
]

productos = ["Laptop", "Mouse", "Teclado", "Monitor"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

print("\nVentas de productos durante la semana:")
for i in range(len(ventas)):
    print(f"{productos[i]}: ", end="")
    for j in range(len(ventas[i])):
        print(f"{ventas[i][j]}", end=" ")
    print()

# Mostrar el total vendido por cada producto
print("\nTotal vendido por cada producto:")
for i in range(len(ventas)):
    total_producto = sum(ventas[i])
    print(f"{productos[i]}: {total_producto} unidades")

# Mostrar el día con mayores ventas totales
ventas_por_dia = []
for j in range(len(dias)):
    total_dia = sum(ventas[i][j] for i in range(len(ventas)))
    ventas_por_dia.append(total_dia)

mayor_venta = max(ventas_por_dia)
dia_mayor_venta = ventas_por_dia.index(mayor_venta)

print(f"\nDía con mayores ventas totales: {dias[dia_mayor_venta]} con {mayor_venta} unidades")

# Indicar cuál fue el producto más vendido en la semana
total_por_producto = [sum(ventas[i]) for i in range(len(ventas))]
producto_mas_vendido = total_por_producto.index(max(total_por_producto))

print(f"Producto más vendido en la semana: {productos[producto_mas_vendido]} con {max(total_por_producto)} unidades")
