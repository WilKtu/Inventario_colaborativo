import sys
from inventario import *
def separador():
    print("========================================")

def menu():
    mensaje = """    1. Agregar Producto
    2. Listar Productos
    3. Salir
"""
    separador()
    print("      SISTEMA DE INVENTARIO")
    separador()
    print(mensaje)
    

def main():
    while True:
        menu()
        try: 
            op = int(input("Ingrese una opcion: "))
            if op == 1:
                separador()
                print("AGREGAR PRODUCTO")
                separador()
                agregar_producto()
            elif op == 2:
                separador()
                print("LISTAR PRODUCTOS")
                separador()
                listar_productos()
                print("Otro Print HolAAAAA MuuuunDOOOOO")
            elif op == 3: 
                separador()
                print("SALIENDO DEL PROGRAMA ...")
                print("hoLA mUNDop")
                print("Este es otro mensaje HoLAAA MunDDOooo")
                sys.exit(0)
            else:
                separador()
                print("Opción inválida")
        except ValueError as v:
            print("Error: ", v)
            
if __name__ == "__main__": 
    main() 