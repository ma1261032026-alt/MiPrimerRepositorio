def transformar_lista(lista_palabras, opcion):
    nueva_lista = []
    for palabra in lista_palabras:
        if opcion == 1:
            nueva_lista.append(palabra.upper())
        elif opcion == 2:
            nueva_lista.append(palabra.lower())
        elif opcion == 3:
            nueva_lista.append(palabra.capitalize())
    return nueva_lista


# Prueba con una lista
frutas = ["manzana", "pera", "uva"]
print(transformar_lista(frutas, 1))
