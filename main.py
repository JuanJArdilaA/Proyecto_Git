import json
import os

ARCHIVO_JSON = 'inventario.json'

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
    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            print("En desarrollo: Registrar ítem")
        elif opcion == '2':
            print("En desarrollo: Listar ítems")
        elif opcion == '6':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción en desarrollo o no válida.")

if __name__ == "__main__":
    main()