inventario = {
    'manzanas': 50,
    'naranjas': 30,
    'peras': 20
}


# Función para mostrar el inventario
def mostrar_inventario(inventario):
    print("\nInventario actual:")
    for producto, cantidad in inventario.items():
        print(f"{producto}: {cantidad} unidades")
    print()

# Función para agregar un nuevo producto
def agregar_producto(inventario, producto, cantidad):
    if producto in inventario:
        print(f"⚠️ El producto '{producto}' ya existe. Usa 'actualizar_producto' para cambiar la cantidad.")
    else:
        inventario[producto] = cantidad
        print(f"✅ Producto '{producto}' agregado con {cantidad} unidades.")