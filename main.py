import json
import os

ARCHIVO_JSON = 'inventario.json'

def cargar_datos():
    if not os.path.exists(ARCHIVO_JSON):
        return []
    try:
        with open(ARCHIVO_JSON, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def guardar_datos(datos):
    with open(ARCHIVO_JSON, 'w') as file:
        json.dump(datos, file, indent=4)

def registrar_item(datos):
    print("\n--- Registrar Nuevo Ítem ---")
    codigo = input("Ingrese el código del ítem: ")
    titulo = input("Ingrese el título: ")
    autor = input("Ingrese el autor: ")
    cantidad = int(input("Ingrese la cantidad total: "))
    
    nuevo_item = {
        "codigo": codigo, "titulo": titulo, "autor": autor,
        "cantidad_total": cantidad, "cantidad_disponible": cantidad
    }
    datos.append(nuevo_item)
    guardar_datos(datos)
    print(f"Ítem '{titulo}' registrado exitosamente.")

def listar_items(datos):
    print("\n--- Lista de Ítems ---")
    for item in datos:
        print(f"[{item['codigo']}] {item['titulo']} por {item['autor']} - Disponibles: {item['cantidad_disponible']}/{item['cantidad_total']}")

# NUEVA FUNCIÓN AGREGADA POR JUAN
def buscar_item(datos):
    print("\n--- Buscar Ítem ---")
    termino = input("Ingrese el título o código del ítem a buscar: ").lower()
    encontrados = False
    for item in datos:
        if termino in item['codigo'].lower() or termino in item['titulo'].lower():
            print(f"[{item['codigo']}] {item['titulo']} por {item['autor']} - Disponibles: {item['cantidad_disponible']}/{item['cantidad_total']}")
            encontrados = True
    
    if not encontrados:
        print("No se encontraron ítems que coincidan con la búsqueda.")

def registrar_prestamo(datos):
    codigo = input("Ingrese el código a prestar: ")
    for item in datos:
        if item['codigo'] == codigo and item['cantidad_disponible'] > 0:
            item['cantidad_disponible'] -= 1
            guardar_datos(datos)
            print("Préstamo exitoso.")
            return
    print("Ítem no disponible.")

def registrar_devolucion(datos):
    codigo = input("Ingrese el código a devolver: ")
    for item in datos:
        if item['codigo'] == codigo and item['cantidad_disponible'] < item['cantidad_total']:
            item['cantidad_disponible'] += 1
            guardar_datos(datos)
            print("Devolución exitosa.")
            return
    print("Error en devolución.")

def mostrar_menu():
    print("\n==========================================")
    print("--- BIBLIOSTOCK CLI - BIBLIOTECA HORIZONTE ---")
    print("==========================================")
    print("1. Registrar ítem")
    print("2. Listar ítems")
    print("3. Buscar ítem")
    print("4. Registrar préstamo")
    print("5. Registrar devolución")
    print("6. Salir")
    print("==========================================")
    return input("Seleccione una opción: ")

def main():
    datos = cargar_datos()
    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            registrar_item(datos)
        elif opcion == '2':
            listar_items(datos)
        elif opcion == '3':
            buscar_item(datos) # AQUÍ SE ACTUALIZÓ LA OPCIÓN 3
        elif opcion == '4':
            registrar_prestamo(datos)
        elif opcion == '5':
            registrar_devolucion(datos)
        elif opcion == '6':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()