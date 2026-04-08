def transformar_texto(texto, opcion):
    if opcion == 1:
        return texto.upper()
    # Todo a MAYÚSCULAS
    elif opcion == 2:
        return texto.lower()
    # Todo a minúsculas
    elif opcion == 3:
        return texto.capitalize()
    # Primera en Mayúscula
    else:
        return texto  # Si no es 1, 2 o 3, devuelve el texto original


# Ejemplo de uso
resultado = transformar_texto("hola mundo", 1)
print(resultado)
