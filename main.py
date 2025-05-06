# main.py

from inventario import mostrar_inventario, agregar_producto, actualizar_producto, eliminar_producto

# Diccionario inicial de inventario
inventario = {
    'manzanas': 50,
    'naranjas': 30,
    'peras': 20
}

# Uso del sistema de inventario
mostrar_inventario(inventario)
actualizar_producto(inventario, 'peras', 25)
agregar_producto(inventario, 'bananas', 40)
eliminar_producto(inventario, 'manzanas')
mostrar_inventario(inventario)
