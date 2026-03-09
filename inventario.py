inventario = [
    {"nombre": "Manzanas", "precio": 0.5, "cantidad": 50},
    {"nombre": "Naranjas", "precio": 0.7, "cantidad": 30},
    {"nombre": "Plátanos", "precio": 0.3, "cantidad": 100},
    {"nombre": "Leche", "precio": 1.2, "cantidad": 20},
    {"nombre": "Pan", "precio": 1.0, "cantidad": 15}
]

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