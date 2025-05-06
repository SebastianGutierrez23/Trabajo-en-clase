def agregar_producto(inventario, producto, cantidad):
    if producto in inventario:
        print(f"⚠️ El producto '{producto}' ya existe. Usa 'actualizar_producto' para cambiar la cantidad.")
    else:
        inventario[producto] = cantidad
        print(f"✅ Producto '{producto}' agregado con {cantidad} unidades.")
