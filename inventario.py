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
    
def listar_productos():
    for producto in inventario:
        print(f"{producto['nombre']} - Precio: {producto['precio']} - Cantidad: {producto['cantidad']}")