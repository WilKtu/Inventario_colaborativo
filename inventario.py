inventario = []

def agregar_producto():
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio"))
    cantidad = int(input("Cantidad: "))

    inventario.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })