def transformaciones_multiples(texto, lista_opciones):
    resultado = texto
    for opcion in lista_opciones:
        if opcion == 1:
            resultado = resultado.upper()
        elif opcion == 2:
            resultado = resultado.lower()
        elif opcion == 3:
            resultado = resultado.capitalize()
    return resultado


# Ejemplo: primero a mayúsculas y luego a minúsculas
print(transformaciones_multiples("Hola Mundo", [1, 2]))
