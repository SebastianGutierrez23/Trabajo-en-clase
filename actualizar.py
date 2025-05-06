def actualizar_producto(inventario, producto, cantidad):
    if producto in inventario:
        print(f"Actualizando stock de '{producto}' a {cantidad}...")
        inventario[producto] = cantidad
    else:
        print(f"Error: El producto '{producto}' no existe en el inventario.")


