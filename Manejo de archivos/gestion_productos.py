"""
Programa de gestión de productos con archivos
Permite leer, mostrar, agregar, buscar y guardar productos
"""


def leer_productos():
    """
    Lee el archivo productos.txt y retorna una lista de diccionarios
    con los productos cargados
    """
    productos = []
    try:
        with open('productos.txt', 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                linea = linea.strip()  # Elimina espacios y saltos de línea
                if linea:  # Solo procesa líneas no vacías
                    datos = linea.split(",")  # Separa por comas
                    if len(datos) == 3:  # Verifica que tenga 3 elementos
                        producto = {
                            'nombre': datos[0].strip(),
                            'precio': float(datos[1].strip()),
                            'cantidad': int(datos[2].strip())
                        }
                        productos.append(producto)
    except FileNotFoundError:
        print("El archivo productos.txt no existe. Se creará uno nuevo.")
    except ValueError as e:
        print(f"Error al procesar los datos: {e}")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    
    return productos


def mostrar_productos(productos):
    """
    Muestra todos los productos en el formato especificado
    """
    if not productos:
        print("No hay productos para mostrar.")
        return
    
    print("\n--- Lista de Productos ---")
    for producto in productos:
        print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")


def agregar_producto(productos):
    """
    Permite al usuario agregar un nuevo producto desde teclado
    """
    print("\n--- Agregar Nuevo Producto ---")
    nombre = input("Ingrese el nombre del producto: ").strip()
    
    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return productos
    
    try:
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        
        nuevo_producto = {
            'nombre': nombre,
            'precio': precio,
            'cantidad': cantidad
        }
        
        productos.append(nuevo_producto)
        print(f"\n✓ Producto '{nombre}' agregado exitosamente.")
        
    except ValueError:
        print("Error: Precio debe ser un número y cantidad debe ser un entero.")
    
    return productos


def buscar_producto(productos):
    """
    Busca un producto por nombre y muestra sus datos
    """
    if not productos:
        print("No hay productos para buscar.")
        return
    
    print("\n--- Buscar Producto ---")
    nombre_buscado = input("Ingrese el nombre del producto a buscar: ").strip()
    
    encontrado = False
    for producto in productos:
        if producto['nombre'].lower() == nombre_buscado.lower():
            print("\n✓ Producto encontrado:")
            print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
            encontrado = True
            break
    
    if not encontrado:
        print(f"\n✗ Error: No se encontró el producto '{nombre_buscado}'.")


def guardar_productos(productos):
    """
    Guarda la lista de productos en el archivo productos.txt
    Sobrescribe el contenido anterior
    """
    try:
        with open('productos.txt', 'w', encoding='utf-8') as archivo:
            for producto in productos:
                linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
                archivo.write(linea)
        print("\n✓ Productos guardados exitosamente en productos.txt")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")


def main():
    """
    Función principal que coordina todas las operaciones
    """
    print("=" * 50)
    print("SISTEMA DE GESTIÓN DE PRODUCTOS")
    print("=" * 50)
    
    # 1. Leer productos del archivo
    productos = leer_productos()
    
    # 2. Mostrar productos
    mostrar_productos(productos)
    
    # 3. Menú de opciones
    while True:
        print("\n" + "=" * 50)
        print("MENÚ DE OPCIONES:")
        print("1. Agregar un producto")
        print("2. Buscar un producto por nombre")
        print("3. Mostrar todos los productos")
        print("4. Guardar y salir")
        print("=" * 50)
        
        opcion = input("\nSeleccione una opción (1-4): ").strip()
        
        if opcion == '1':
            productos = agregar_producto(productos)
        elif opcion == '2':
            buscar_producto(productos)
        elif opcion == '3':
            mostrar_productos(productos)
        elif opcion == '4':
            guardar_productos(productos)
            print("\n¡Hasta luego!")
            break
        else:
            print("\n✗ Opción inválida. Por favor, seleccione 1, 2, 3 o 4.")


if __name__ == "__main__":
    main()

