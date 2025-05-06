def eliminar_producto(inventario, producto):
    if producto in inventario:
        print(f"Eliminando '{producto}' del inventario...")
        del inventario[producto]
    else:
        print(f"Error: El producto '{producto}' no se encuentra en el inventario.")
