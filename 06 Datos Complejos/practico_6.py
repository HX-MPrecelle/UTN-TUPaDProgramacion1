"""
Práctico 6: Estructuras de datos complejas
Objetivo: Dominar el uso de estructuras de datos complejas en Python
"""

print("=" * 60)
print("PRÁCTICO 6: ESTRUCTURAS DE DATOS COMPLEJAS")
print("=" * 60)

# ============================================================================
# EJERCICIO 1: Añadir frutas al diccionario
# ============================================================================
print("\n--- Ejercicio 1: Añadir frutas al diccionario ---")

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
print(f"Diccionario inicial: {precios_frutas}")

# Añadir las nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(f"Diccionario después de añadir frutas: {precios_frutas}")

# ============================================================================
# EJERCICIO 2: Actualizar precios de frutas
# ============================================================================
print("\n--- Ejercicio 2: Actualizar precios de frutas ---")

# Actualizar los precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(f"Diccionario después de actualizar precios: {precios_frutas}")

# ============================================================================
# EJERCICIO 3: Crear lista de frutas sin precios
# ============================================================================
print("\n--- Ejercicio 3: Lista de frutas sin precios ---")

lista_frutas = list(precios_frutas.keys())
print(f"Lista de frutas: {lista_frutas}")

# ============================================================================
# EJERCICIO 4: Agenda telefónica
# ============================================================================
print("\n--- Ejercicio 4: Agenda telefónica ---")

contactos = {}

# Cargar 5 contactos
print("Cargando 5 contactos...")
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número telefónico de {nombre}: ")
    contactos[nombre] = numero

print(f"\nContactos cargados: {contactos}")

# Consultar un contacto
nombre_consulta = input("\nIngrese el nombre a consultar: ")
if nombre_consulta in contactos:
    print(f"El número de {nombre_consulta} es: {contactos[nombre_consulta]}")
else:
    print(f"No se encontró el contacto: {nombre_consulta}")

# ============================================================================
# EJERCICIO 5: Análisis de palabras en una frase
# ============================================================================
print("\n--- Ejercicio 5: Análisis de palabras en una frase ---")

frase = input("Ingrese una frase: ")

# Convertir a minúsculas y dividir en palabras
palabras = frase.lower().split()

# Obtener palabras únicas usando un set
palabras_unicas = set(palabras)
print(f"Palabras únicas: {palabras_unicas}")

# Contar la cantidad de veces que aparece cada palabra
recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print(f"Recuento: {recuento}")

# ============================================================================
# EJERCICIO 6: Promedio de notas de alumnos
# ============================================================================
print("\n--- Ejercicio 6: Promedio de notas de alumnos ---")

alumnos = {}

# Ingresar datos de 3 alumnos
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    print(f"Ingrese las 3 notas de {nombre}:")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    alumnos[nombre] = (nota1, nota2, nota3)

print(f"\nDatos de alumnos: {alumnos}")

# Calcular y mostrar el promedio de cada alumno
print("\nPromedios:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

# ============================================================================
# EJERCICIO 7: Análisis de estudiantes que aprobaron parciales
# ============================================================================
print("\n--- Ejercicio 7: Análisis de estudiantes que aprobaron parciales ---")

# Definir los sets de estudiantes
aprobados_parcial1 = {101, 102, 103, 104, 105}
aprobados_parcial2 = {102, 104, 106, 107, 108}

print(f"Estudiantes que aprobaron Parcial 1: {aprobados_parcial1}")
print(f"Estudiantes que aprobaron Parcial 2: {aprobados_parcial2}")

# Los que aprobaron ambos parciales
aprobados_ambos = aprobados_parcial1 & aprobados_parcial2
print(f"\nEstudiantes que aprobaron ambos parciales: {aprobados_ambos}")

# Los que aprobaron solo uno de los dos
solo_parcial1 = aprobados_parcial1 - aprobados_parcial2
solo_parcial2 = aprobados_parcial2 - aprobados_parcial1
solo_uno = solo_parcial1 | solo_parcial2
print(f"Estudiantes que aprobaron solo uno de los dos: {solo_uno}")
print(f"  - Solo Parcial 1: {solo_parcial1}")
print(f"  - Solo Parcial 2: {solo_parcial2}")

# Lista total de estudiantes que aprobaron al menos un parcial
total_aprobados = aprobados_parcial1 | aprobados_parcial2
print(f"\nEstudiantes que aprobaron al menos un parcial: {total_aprobados}")

# ============================================================================
# EJERCICIO 8: Gestión de stock de productos
# ============================================================================
print("\n--- Ejercicio 8: Gestión de stock de productos ---")

productos_stock = {
    'Laptop': 15,
    'Mouse': 50,
    'Teclado': 30,
    'Monitor': 20
}

print(f"Stock inicial: {productos_stock}")

while True:
    print("\nOpciones:")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades al stock")
    print("3. Agregar un nuevo producto")
    print("4. Salir")
    
    opcion = input("\nSeleccione una opción (1-4): ")
    
    if opcion == '1':
        producto = input("Ingrese el nombre del producto a consultar: ")
        if producto in productos_stock:
            print(f"Stock de {producto}: {productos_stock[producto]} unidades")
        else:
            print(f"El producto '{producto}' no existe en el inventario.")
    
    elif opcion == '2':
        producto = input("Ingrese el nombre del producto: ")
        if producto in productos_stock:
            unidades = int(input(f"Ingrese las unidades a agregar a {producto}: "))
            productos_stock[producto] += unidades
            print(f"Stock actualizado. {producto} ahora tiene {productos_stock[producto]} unidades.")
        else:
            print(f"El producto '{producto}' no existe. Use la opción 3 para agregarlo.")
    
    elif opcion == '3':
        producto = input("Ingrese el nombre del nuevo producto: ")
        unidades = int(input(f"Ingrese el stock inicial de {producto}: "))
        productos_stock[producto] = unidades
        print(f"Producto '{producto}' agregado con {unidades} unidades.")
    
    elif opcion == '4':
        print("\nSaliendo del sistema de gestión de stock...")
        print(f"Stock final: {productos_stock}")
        break
    
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

# ============================================================================
# EJERCICIO 9: Agenda con tuplas como claves
# ============================================================================
print("\n--- Ejercicio 9: Agenda con tuplas como claves ---")

agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "09:00"): "Cita médica",
    ("jueves", "14:30"): "Entrega de proyecto"
}

print(f"Agenda actual: {agenda}")

# Consultar actividad
dia = input("\nIngrese el día a consultar (lunes, martes, etc.): ").lower()
hora = input("Ingrese la hora a consultar (formato HH:MM): ")

clave = (dia, hora)
if clave in agenda:
    print(f"El {dia} a las {hora} hay: {agenda[clave]}")
else:
    print(f"No hay actividad programada el {dia} a las {hora}")

# ============================================================================
# EJERCICIO 10: Invertir diccionario países-capitales
# ============================================================================
print("\n--- Ejercicio 10: Invertir diccionario países-capitales ---")

paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Perú": "Lima",
    "Colombia": "Bogotá",
    "Brasil": "Brasilia"
}

print(f"Diccionario original: {paises_capitales}")

# Crear el diccionario invertido
capitales_paises = {}
for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

print(f"Diccionario invertido: {capitales_paises}")

print("\n" + "=" * 60)
print("PRÁCTICO 6 COMPLETADO")
print("=" * 60)
