def actualizar_producto(inventario, producto, cantidad):
    if producto in inventario:
        print(f"Actualizando stock de '{producto}' a {cantidad}...")
        inventario[producto] = cantidad
    else:
        print(f"Error: El producto '{producto}' no existe en el inventario.")


def eliminar_producto(inventario, producto):
    if producto in inventario:
        print(f"Eliminando '{producto}' del inventario...")
        del inventario[producto]
    else:
        print(f"Error: El producto '{producto}' no se encuentra en el inventario.")
