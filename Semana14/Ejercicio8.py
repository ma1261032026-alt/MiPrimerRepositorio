def buscar_producto(lista, producto_buscado):
    if producto_buscado.lower() in [p.lower() for p in lista]:
        print(f"El producto '{producto_buscado}' fue encontrado.")
    else:
        print("Producto no disponible.")


inventario = []
for i in range(5):
    item = input(f"Ingrese el producto {i+1}: ")
    inventario.append(item)

busqueda = input("Ingrese el nombre del producto a buscar: ")
buscar_producto(inventario, busqueda)
