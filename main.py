import json
import os

ARCHIVO_JSON = 'inventario.json'

def cargar_datos():
    with open(ARCHIVO_JSON, 'r') as file:
        return json.load(file)

def guardar_datos(datos):
    with open(ARCHIVO_JSON, 'w') as file:
        json.dump(datos, file, indent=4)

def registrar_item(datos):
    print("\n--- Registrar Nuevo Item ---")
    codigo = input("Ingrese el código del ítem: ")
    titulo = input("Ingrese el título: ")
    autor = input("Ingrese el autor: ")
    cantidad = int(input("Ingrese la cantidad total: "))

    nuevo_item = {
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "cantidad_total": cantidad,
        "cantidad_disponible": cantidad
    }
    datos.append(nuevo_item)
    guardar_datos(datos)
    print(f"Ítem '{titulo}' registrado exitosamente.")

def listar_items(datos):
    print("\n--- Listado de Ítems ---")
    for item in datos:
        print(f"Código: {item['codigo']}, Título: {item['titulo']}, Autor: {item['autor']}, Disponible: {item['cantidad_disponible']}/{item['cantidad_total']}")

def mostrar_menu():
    print("\n==========================================")
    print("BIBLIOSTOCK CLI - BIBLIOTECA HORIZONTE") 
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
        elif opcion == '6':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción en desarrollo o no válida.")

if __name__ == "__main__":
    main()