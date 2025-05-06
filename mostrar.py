def mostrar_inventario(inventario):
    print("\nInventario actual:")
    for producto, cantidad in inventario.items():
        print(f"{producto}: {cantidad} unidades")
    print()