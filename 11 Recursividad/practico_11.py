"""
Práctico 11: Aplicación de la Recursividad

Este módulo contiene implementaciones recursivas de diversos problemas matemáticos
y algorítmicos, demostrando el uso de la recursividad en Python.
"""


# ============================================================================
# EJERCICIO 1: Factorial Recursivo
# ============================================================================

def factorial(n):
    """
    Calcula el factorial de un número usando recursividad.
    
    Caso base: factorial(0) = 1 y factorial(1) = 1
    Caso recursivo: factorial(n) = n * factorial(n-1)
    
    Args:
        n (int): Número entero positivo
    
    Returns:
        int: El factorial de n
    
    Ejemplo:
        factorial(5) -> 120
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def mostrar_factoriales_hasta(numero):
    """
    Muestra el factorial de todos los números enteros entre 1 y el número indicado.
    
    Args:
        numero (int): Número límite (inclusive)
    """
    print("\n" + "=" * 50)
    print("EJERCICIO 1: Factoriales")
    print("=" * 50)
    for i in range(1, numero + 1):
        resultado = factorial(i)
        print(f"Factorial de {i} = {resultado}")


# ============================================================================
# EJERCICIO 2: Serie de Fibonacci Recursiva
# ============================================================================

def fibonacci(posicion):
    """
    Calcula el valor de la serie de Fibonacci en la posición indicada usando recursividad.
    
    Caso base: fibonacci(0) = 0, fibonacci(1) = 1
    Caso recursivo: fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
    
    Args:
        posicion (int): Posición en la serie de Fibonacci (comenzando desde 0)
    
    Returns:
        int: El valor de Fibonacci en esa posición
    
    Ejemplo:
        fibonacci(7) -> 13
    """
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)


def mostrar_serie_fibonacci(limite):
    """
    Muestra la serie completa de Fibonacci hasta la posición especificada.
    
    Args:
        limite (int): Última posición a mostrar (inclusive)
    """
    print("\n" + "=" * 50)
    print("EJERCICIO 2: Serie de Fibonacci")
    print("=" * 50)
    print("Serie de Fibonacci hasta la posición", limite, ":")
    for i in range(limite + 1):
        valor = fibonacci(i)
        print(f"Posición {i}: {valor}")


# ============================================================================
# EJERCICIO 3: Potencia Recursiva
# ============================================================================

def potencia(base, exponente):
    """
    Calcula la potencia de un número base elevado a un exponente usando recursividad.
    Utiliza la fórmula: n^m = n * n^(m-1)
    
    Caso base: base^0 = 1
    Caso recursivo: base^exponente = base * base^(exponente-1)
    
    Args:
        base (float): Número base
        exponente (int): Exponente (entero no negativo)
    
    Returns:
        float: El resultado de base elevado a exponente
    
    Ejemplo:
        potencia(2, 8) -> 256
    """
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)


# ============================================================================
# EJERCICIO 4: Conversión Decimal a Binario Recursiva
# ============================================================================

def decimal_a_binario(numero):
    """
    Convierte un número entero positivo de base decimal a binario usando recursividad.
    
    El proceso recursivo:
    1. Dividir el número por 2
    2. Guardar el resto (0 o 1)
    3. Repetir con el cociente hasta llegar a 0
    4. Los restos leídos de abajo hacia arriba forman el número binario
    
    Caso base: Si número < 2, retorna el número como string
    Caso recursivo: decimal_a_binario(numero // 2) + str(numero % 2)
    
    Args:
        numero (int): Número entero positivo en base decimal
    
    Returns:
        str: Representación binaria del número
    
    Ejemplo:
        decimal_a_binario(10) -> "1010"
    """
    if numero == 0:
        return "0"
    elif numero == 1:
        return "1"
    else:
        return decimal_a_binario(numero // 2) + str(numero % 2)


# ============================================================================
# EJERCICIO 5: Verificar si es Palíndromo Recursivo
# ============================================================================

def es_palindromo(palabra):
    """
    Verifica si una cadena de texto es un palíndromo usando recursividad.
    
    Un palíndromo es una palabra que se lee igual de izquierda a derecha
    que de derecha a izquierda.
    
    Caso base: Si la palabra tiene 0 o 1 caracter, es palíndromo
    Caso recursivo: Si el primer y último carácter son iguales,
                    verificar recursivamente el substring sin esos caracteres
    
    Args:
        palabra (str): Cadena de texto sin espacios ni tildes
    
    Returns:
        bool: True si es palíndromo, False si no lo es
    
    Ejemplo:
        es_palindromo("anilina") -> True
        es_palindromo("python") -> False
    """
    palabra = palabra.lower()  # Convertir a minúsculas para comparación
    
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])


# ============================================================================
# EJERCICIO 6: Suma de Dígitos Recursiva
# ============================================================================

def suma_digitos(n):
    """
    Calcula la suma de todos los dígitos de un número usando recursividad.
    
    No convierte el número a string, usa operaciones matemáticas (%, //).
    
    Caso base: Si n < 10, retorna n
    Caso recursivo: suma_digitos(n) = (n % 10) + suma_digitos(n // 10)
    
    Args:
        n (int): Número entero positivo
    
    Returns:
        int: Suma de todos los dígitos del número
    
    Ejemplo:
        suma_digitos(1234) -> 10
        suma_digitos(305) -> 8
    """
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)


# ============================================================================
# EJERCICIO 7: Contar Bloques de Pirámide Recursivo
# ============================================================================

def contar_bloques(n):
    """
    Calcula el total de bloques necesarios para construir una pirámide.
    
    En el nivel más bajo hay n bloques, en el siguiente (n-1), y así hasta 1.
    Total = n + (n-1) + (n-2) + ... + 1
    
    Esto es equivalente a la suma triangular: n(n+1)/2
    
    Caso base: Si n == 1, retorna 1
    Caso recursivo: contar_bloques(n) = n + contar_bloques(n-1)
    
    Args:
        n (int): Número de bloques en el nivel más bajo
    
    Returns:
        int: Total de bloques necesarios para toda la pirámide
    
    Ejemplo:
        contar_bloques(4) -> 10  (4 + 3 + 2 + 1)
    """
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)


# ============================================================================
# EJERCICIO 8: Contar Dígito en Número Recursivo
# ============================================================================

def contar_digito(numero, digito):
    """
    Cuenta cuántas veces aparece un dígito dentro de un número usando recursividad.
    
    Caso base: Si numero < 10, comparar directamente
    Caso recursivo: contar_digito(numero, digito) = 
                    (1 si numero % 10 == digito else 0) + contar_digito(numero // 10, digito)
    
    Args:
        numero (int): Número entero positivo
        digito (int): Dígito a buscar (entre 0 y 9)
    
    Returns:
        int: Cantidad de veces que aparece el dígito en el número
    
    Ejemplo:
        contar_digito(12233421, 2) -> 3
        contar_digito(5555, 5) -> 4
    """
    if numero < 10:
        return 1 if numero == digito else 0
    else:
        ultimo_digito = numero % 10
        resto = numero // 10
        conteo_actual = 1 if ultimo_digito == digito else 0
        return conteo_actual + contar_digito(resto, digito)


# ============================================================================
# MENÚ PRINCIPAL
# ============================================================================

def menu_principal():
    """
    Muestra un menú interactivo para probar todas las funciones recursivas.
    """
    while True:
        print("\n" + "=" * 60)
        print("PRÁCTICO 11: APLICACIÓN DE LA RECURSIVIDAD")
        print("=" * 60)
        print("1. Factoriales")
        print("2. Serie de Fibonacci")
        print("3. Potencia Recursiva")
        print("4. Conversión Decimal a Binario")
        print("5. Verificar Palíndromo")
        print("6. Suma de Dígitos")
        print("7. Contar Bloques de Pirámide")
        print("8. Contar Dígito en Número")
        print("0. Salir")
        print("=" * 60)
        
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == '1':
            try:
                numero = int(input("Ingrese el número hasta el cual calcular factoriales: "))
                if numero > 0:
                    mostrar_factoriales_hasta(numero)
                else:
                    print("Error: El número debe ser positivo.")
            except ValueError:
                print("Error: Debe ingresar un número entero válido.")
        
        elif opcion == '2':
            try:
                limite = int(input("Ingrese la posición límite para la serie de Fibonacci: "))
                if limite >= 0:
                    mostrar_serie_fibonacci(limite)
                else:
                    print("Error: La posición debe ser no negativa.")
            except ValueError:
                print("Error: Debe ingresar un número entero válido.")
        
        elif opcion == '3':
            print("\n" + "=" * 50)
            print("EJERCICIO 3: Potencia Recursiva")
            print("=" * 50)
            try:
                base = float(input("Ingrese la base: "))
                exponente = int(input("Ingrese el exponente (entero no negativo): "))
                
                if exponente < 0:
                    print("Error: El exponente debe ser un número entero no negativo.")
                else:
                    resultado = potencia(base, exponente)
                    print(f"\n{base}^{exponente} = {resultado}")
            except ValueError:
                print("Error: Debe ingresar números válidos.")
        
        elif opcion == '4':
            print("\n" + "=" * 50)
            print("EJERCICIO 4: Conversión Decimal a Binario")
            print("=" * 50)
            try:
                numero = int(input("Ingrese un número entero positivo en base decimal: "))
                
                if numero < 0:
                    print("Error: El número debe ser positivo.")
                else:
                    binario = decimal_a_binario(numero)
                    print(f"\n{numero} en binario = {binario}")
            except ValueError:
                print("Error: Debe ingresar un número entero válido.")
        
        elif opcion == '5':
            palabra = input("Ingrese una palabra para verificar si es palíndromo: ").strip()
            if palabra:
                resultado = es_palindromo(palabra)
                print(f"\n'{palabra}' es palíndromo: {resultado}")
            else:
                print("Error: Debe ingresar una palabra.")
        
        elif opcion == '6':
            print("\n" + "=" * 50)
            print("EJERCICIO 6: Suma de Dígitos")
            print("=" * 50)
            try:
                numero = int(input("Ingrese un número entero positivo: "))
                
                if numero < 0:
                    print("Error: El número debe ser positivo.")
                else:
                    resultado = suma_digitos(numero)
                    print(f"\nsuma_digitos({numero}) = {resultado}")
            except ValueError:
                print("Error: Debe ingresar un número entero válido.")
        
        elif opcion == '7':
            print("\n" + "=" * 50)
            print("EJERCICIO 7: Contar Bloques de Pirámide")
            print("=" * 50)
            try:
                nivel = int(input("Ingrese el número de bloques en el nivel más bajo: "))
                
                if nivel <= 0:
                    print("Error: El número de bloques debe ser positivo.")
                else:
                    resultado = contar_bloques(nivel)
                    print(f"\ncontar_bloques({nivel}) = {resultado}")
            except ValueError:
                print("Error: Debe ingresar un número entero válido.")
        
        elif opcion == '8':
            try:
                numero = int(input("Ingrese un número: "))
                digito = int(input("Ingrese el dígito a buscar (0-9): "))
                if numero >= 0 and 0 <= digito <= 9:
                    resultado = contar_digito(numero, digito)
                    print(f"\nEl dígito {digito} aparece {resultado} vez/veces en {numero}")
                else:
                    print("Error: Número debe ser positivo y dígito entre 0 y 9.")
            except ValueError:
                print("Error: Debe ingresar números enteros válidos.")
        
        elif opcion == '0':
            print("\n¡Hasta luego!")
            break
        
        else:
            print("\nOpción inválida. Por favor, seleccione una opción del menú.")


if __name__ == "__main__":
    menu_principal()

